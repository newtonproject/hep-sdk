"""The implementation of HEP Authentication protocol

"""

__copyright__ = """ Copyright (c) 2019 Newton Foundation. All rights reserved."""
__version__ = '1.0'
__author__ = 'xiawu@zeuux.org'

import logging
from hep_rest_api.scenarios import BaseHelper

logger = logging.getLogger(__name__)

class AuthHelper(BaseHelper):
    def generateAuthRequest(self, dapp_id, action='hep.auth.login', scope=1, expired=300, memo=''):
        """Generate the authentication request
        
        :param str dapp_id: The DApp ID
        :param str action: The request action name
        :param int scope: The request scope. 1: base profile including name,head,newid; 2: advance profile including cellphone.
        :param int expired: The expired time of request
        :param str memo: The memo of request to end user
        :rtype: dict
        :return: The request information including signature
        """
        pass

