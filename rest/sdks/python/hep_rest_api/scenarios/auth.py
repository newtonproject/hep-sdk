"""The implementation of HEP Authentication protocol

"""

__copyright__ = """ Copyright (c) 2019 Newton Foundation. All rights reserved."""
__version__ = '1.0'
__author__ = 'xiawu@zeuux.org'

import logging
import datetime
from hep_rest_api.scenarios import BaseHelper

logger = logging.getLogger(__name__)

class AuthHelper(BaseHelper):
    def generate_auth_request(self, dapp_id, action='hep.auth.login', scope=1, expired=300, memo='', uuid=None):
        """Generate the authentication request
        
        :param str dapp_id: The DApp ID
        :param str action: The request action name
        :param int scope: The request scope. 1: base profile including name,head,newid; 2: advance profile including cellphone.
        :param int expired: The expired time of request
        :param str memo: The memo of request to end user
        :param str uuid: The request uuid for desktop-browser. optional.
        :rtype: dict
        :return: The request information including signature
        """
        data = {
            'dapp_id': dapp_id,
            'action': action,
            'scope': scope,
            'expired': int(datetime.datetime.now().timestamp()) + expired,
            'memo': memo
        }
        if uuid:
            data['uuid'] = uuid
        sign_data = self.generate_sign_data(data)
        final_data = self.sign_hmac(sign_data)
        r1_data = self.sign_secp256r1(sign_data)
        final_data.update(r1_data) # merge two data set
        # start request

    def generate_qrcode_string(self, auth_request):
        """Generate the hep-based scheme string string for QRCode 
        
        :param dict auth_request: The auth request
        :rtype: str
        :return: The QRcode string
        """
        pass

    def validate_auth_callback(self, data):
        """Validate the response of auth callback sent by end users such as NewPay users 
        
        :param dict data: The callback data
        :rtype: bool
        :return: True if valid data, otherwise False
        """
        pass
