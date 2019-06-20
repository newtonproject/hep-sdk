"""The abstract layer of HEP scenarios

"""

__copyright__ = """ Copyright (c) 2019 Newton Foundation. All rights reserved."""
__version__ = '1.0'
__author__ = 'xiawu@zeuux.org'

import logging

logger = logging.getLogger(__name__)

class BaseHelper(object):
    def __init__(self, api_client, base_parameters, key_path):
        """Initialize the basic parameters

        :param hep_rest_api.RestApi api_client: The api client instance
        :param dict base_parameters: The base parameters for HMAC authentication
        :param str key_path: The private key path for dapp owner's signature
        """
        self.api_client = api_client
        self.base_parameters = base_parameters
        self.key_path

    def get_default_trust_oracle(self):
        """Retrieve the public key of default trust oracle from hep node
        
        :rtype: str
        :return: The public key of default trust oracle
        """
        pass

