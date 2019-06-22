# -*- coding: utf-8 -*-
"""
Cryptography, address, transaction manipulation for newchain.
"""
__copyright__ = """ Copyright (c) 2018 Newton Foundation. All rights reserved."""
__version__ = '1.0'
__author__ = 'yanhang@diynova.com'

import base58
import binascii
import logging
from sha3 import keccak_256


logger = logging.getLogger(__name__)


PREFIX = 'NEW'


def newid_encode_by_public_key(public_key, chainID):
    if public_key.startswith('0x'):
        public_key = public_key[2:]
    if len(public_key) < 64:
        public_key = '0' * (64 - len(public_key)) + public_key
    k = keccak_256()
    k.update(bytearray.fromhex(public_key))
    data = k.hexdigest()
    hex_chainID = hex(chainID)[2:][-8:]
    if (len(hex_chainID) % 2) == 1:
        hex_chainID = '0' + hex_chainID
    num_sum = hex_chainID + data
    data = base58.b58encode_check(b'\0' + binascii.a2b_hex(num_sum))
    newid = PREFIX + 'ID' + data.decode()
    return newid


if __name__ == "__main__":
    pub = "0x7b474af73e15932dbd14cf3f8fd3ad84ecea0afad13c6a4853536b6f41b2e0c4b769cc26632f2a3ee9651ceb184fd64d7e4ddc82056e5f590f88118df48da2c9"
    chainID = 1002
    newid = newid_encode_by_public_key(pub, chainID)
    print(newid)
