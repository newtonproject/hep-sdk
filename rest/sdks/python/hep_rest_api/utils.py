"""The utility of HEP REST SDK

"""

__copyright__ = """ Copyright (c) 2019 Newton Foundation. All rights reserved."""
__version__ = '1.0'
__author__ = 'xiawu@newtonproject.org'

import json
import hashlib
import collections
import base58
import binascii
import logging
from fastecdsa import curve, ecdsa, keys
from sha3 import keccak_256

logger = logging.getLogger(__name__)
SUPPORT_SIGNATURE_METHODS = ['HMAC-MD5', ]
PREFIX = 'NEW'


def generate_md5(data):
    return hashlib.md5(data.encode('utf-8')).hexdigest()


def generate_signature_base_string(data, joint):
    """Generate the concatenated base string for signature

    :param dict data: The data for signature
    :param str joint: The joint string for concatenation
    :rtype: str
    :return: The concatendated base string
    """
    ordered_data = collections.OrderedDict(sorted(data.items()))
    sign_string = ''
    sign_fields = ['dapp_signature_method', 'dapp_signature', 'signature', 'sign_type']
    n = 0
    for k, v in ordered_data.items():
        if k in sign_fields:
            continue
        if n != 0:
            sign_string += joint
        n += 1
        if isinstance(v, list) or isinstance(v, dict):
            sign_string += u'%s=%s' % (k, json.dumps(v, sort_keys=True, separators=(',', ':'), ensure_ascii=False))
        else:
            sign_string += u'%s=%s' % (k, v)
    return sign_string

def sign_hmac(data, secret, prefix='', use_urlencode=False, joint='&', signature_method='HMAC-MD5'):
    """Generate the HMAC signature string

    :param dict data: The data for signature
    :param str secret: The HMAC secret
    :param str prefix: The concatendated prefix
    :param bool use_urlencode: Whether use urlencode
    :param str joint: The joint string for concatenation
    :param str signature_method: The signature method
    :rtype: str
    :return: The HMAC signature string
    """

    if signature_method not in SUPPORT_SIGNATURE_METHODS:
        raise Exception('Unsupported signature method')
    sign_string = prefix
    sign_string += generate_signature_base_string(data, joint)
    sign_string += secret
    if use_urlencode:
        sign_string = urllib.quote_plus(sign_string)
    signed_string = generate_md5(sign_string)
    return signed_string

def generate_secp256r1_key_pairs(save_path):
    """Generate the key pairs of secp256r1
    
    :param str save_path: The save file path of private key
    :rtype:tuple
    :return: The hex string of public key
    """
    private_key, public_key = keys.gen_keypair(curve.P256)
    keys.export_key(private_key, curve.P256, filepath=save_path)
    x = str(hex(public_key.x))[2:]
    y = str(hex(public_key.y))[2:]
    if len(x) < 64:
        x = '0' * (64 - len(x)) + x
    if len(y) < 64:
        y = '0' * (64 - len(y)) + y
    public_key =  '0x' + x + y
    return public_key

def sign_secp256r1(message, private_key_path, hashfunc=keccak_256):
    """Sign the message by secp256r1
    
    :param str message: The message for sign
    :param str private_key_path: The file path of private key
    :param function hashfunc: The hash function
    :rtype: tuple
    :return: The r and s part of signature
    """
    private_key = keys.import_key(private_key_path)[0]
    r, s = ecdsa.sign(message, private_key, hashfunc=hashfunc)
    return str(hex(r)), str(hex(s))

def extract_secp256r1_public_keys(r, s, message):
    """Extract the public keys from r, s, message which generated by secp256r1

    :param str r: The r part of signature
    :param str s: The s part of signature
    :param str message: The message for signature
    :rtype: list
    :return: The public keys    
    """    
    public_key_point = keys.get_public_keys_from_sig((int(r, 16), int(s, 16)), message, curve.P256, hashfunc=keccak_256)
    public_key_list = []
    for i in public_key_point:
        x = str(hex(i.x)[2:])
        y = str(hex(i.y)[2:])
        if len(x) < 64:
            x = '0' * (64 - len(x)) + x
        if len(y) < 64:
            y = '0' * (64 - len(y)) + y
        public_key = '0x' + x + y
        public_key_list.append(public_key)
    return public_key_list

def validate_secp256r1_signature(r, s, message, valid_public_keys):
    """Validate the secp256r1 signature

    :param str r: The r part of signature
    :param str s: The s part of signature
    :param str message: The message for signature
    :param list valid_public_keys: The public key list for validation
    :rtype: bool
    :return: True if it is valid signature, otherwise False    
    """
    public_keys = extract_secp256r1_public_keys(r, s, message)
    logger.debug("public_keys:%s, valid_public_keys:%s" % (public_keys, valid_public_keys))
    for public_key in public_keys:
        if public_key in valid_public_keys:
            return True
    return False


def newid_encode_by_public_key(public_key, chain_id):
    """ generate newid by public key

    :param str public_key: The public key of newid
    :param int chain_id: The blockchain ID
    :rtype: str
    :return: The encoded newid
    """
    if public_key.startswith('0x'):
        public_key = public_key[2:]
    if len(public_key) < 64:
        public_key = '0' * (64 - len(public_key)) + public_key
    k = keccak_256()
    k.update(bytearray.fromhex(public_key))
    data = k.hexdigest()
    hex_chainID = hex(chain_id)[2:][-8:]
    if (len(hex_chainID) % 2) == 1:
        hex_chainID = '0' + hex_chainID
    num_sum = hex_chainID + data
    data = base58.b58encode_check(b'\0' + binascii.a2b_hex(num_sum))
    newid = PREFIX + 'ID' + data.decode()
    return newid


def validate_newid(r, s, message, newid, chain_id):
    """Validate the newid signature

    :param str r: The r part hex string for signature
    :param str s: The s part hex string for signature
    :param str message: The message which signed
    :param str newid: The user's newid
    :param int chain_id: The NewChain id. The dev environment is 1002, test is 1007, main is 1012
    :rtype: bool
    :return: True if it is valid signature, otherwise False
    """
    public_keys = extract_secp256r1_public_keys(r, s, message)
    for public_key in public_keys:
        temp = newid_encode_by_public_key(public_key, chain_id)
        if temp == newid:
            return True
    return False


def split_signature(signature):
    """Split the given signature

    :param signature:
    :rtype: str, str
    :return: The r part for signature, The s part for signature
    """
    if not signature:
        raise ValueError(
            "Missing the required parameter 'signature' when calling split_signature"
        )
    if signature.startswith("0x"):
        signature = signature[2:]
    sig_half_len = int(len(signature) / 2)
    r = '0x' + signature[: sig_half_len]
    s = '0x' + signature[sig_half_len:]
    return r, s
