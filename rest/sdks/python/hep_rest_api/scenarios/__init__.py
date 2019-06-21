"""The abstract layer of HEP scenarios

"""

__copyright__ = """ Copyright (c) 2019 Newton Foundation. All rights reserved."""
__version__ = '1.0'
__author__ = 'xiawu@zeuux.org'

import logging
import copy
import datetime
import uuid
from hep_rest_api import utils

logger = logging.getLogger(__name__)

class BaseHelper(object):
    def __init__(self, api_client, base_parameters, dapp_secret, key_path, api_version='1'):
        """Initialize the basic parameters

        :param hep_rest_api.RestApi api_client: The api client instance
        :param dict base_parameters: The base parameters for HMAC authentication
        :param str key_path: The private key path for dapp owner's signature
        """
        self.api_client = api_client
        self.base_parameters = base_parameters
        self.key_path = key_path
        self.api_version = api_version
        self.dapp_secret = dapp_secret
        self.action_auth_login = 'hep.auth.login'
        self.action_auth_pay = "hep.pay.order"
        self.action_auth_proof = "hep.proof.submit"

    def get_default_trust_oracle(self):
        """Retrieve the public key of default trust oracle from hep node
        
        :rtype: str
        :return: The public key of default trust oracle
        """
        pass

    def generate_sign_data(self, data):
        sign_data = copy.deepcopy(data)
        sign_data.update(self.base_parameters)
        # dynamic fields
        sign_data['ts'] = int(datetime.datetime.now().timestamp())
        sign_data['nonce'] = uuid.uuid4().hex
        return sign_data

    def sign_hmac(self, data, dapp_signature_method='HMAC-MD5'):
        dapp_signature = utils.sign_hmac(data, self.dapp_secret, signature_method=dapp_signature_method)
        data['dapp_signature'] = dapp_signature
        data['dapp_signature_method'] = dapp_signature_method
        return data

    def concat_signature(self, r, s):
        if r.startswith('0x'):
            r = r[2:]
        if len(r) < 64:
            r = '0' * (64 - len(r)) + r
        if s.startswith('0x'):
            s = s[2:]
        if len(s) < 64:
            s = '0' * (64 - len(s)) + s
        return '0x' + r + s

    def sign_secp256r1(self, data):
        sign_string = utils.generate_signature_base_string(data, '&')
        r, s = utils.sign_secp256r1(sign_string, self.key_path)
        signature = self.concat_signature(r, s)
        data['signature'] = signature
        data['sign_type'] = 'secp256r1'
        return data
