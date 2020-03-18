"""The implementation of HEP Authentication protocol

"""

__copyright__ = """ Copyright (c) 2019 Newton Foundation. All rights reserved."""
__version__ = '1.0'
__author__ = 'xiawu@zeuux.org'

import logging
import datetime
from hep_rest_api.scenarios import BaseHelper
from hep_rest_api import models
from hep_rest_api import utils

logger = logging.getLogger(__name__)


class AuthHelper(BaseHelper):

    def generate_auth_request(self, scope=1, expired=300, memo='', uuid=None):
        """Generate the authentication request

        :param int scope: The request scope. 1: base profile including name,head,newid; 2: advance profile including cellphone.
        :param int expired: The expired time of request
        :param str memo: The memo of request to end user
        :param str uuid: The request uuid for desktop-browser. optional.
        :rtype: dict
        :return: The request information including signature
        """
        if not uuid:
            raise AttributeError(
                "uuid can not be None"
            )
        if not memo:
            memo = "default"
        data = {
            'action': self.action_auth_login,
            'scope': scope,
            'expired': int(datetime.datetime.now().timestamp()) + expired,
            'memo': memo,
            'uuid': uuid,
            'dapp_id': self.dapp_id
        }
        sign_data = self.generate_sign_data(data)
        hmac_data = self.sign_hmac(sign_data)
        final_data = self.sign_secp256r1(hmac_data)
        # start request
        auth_cache = models.AuthCacheRequest(**final_data)
        auth_response = self.api_client.rest_newnet_caches_auth_create(self.api_version, auth_cache)
        return auth_response

    def generate_qrcode_string(self, auth_hash):
        """Generate the hep-based scheme string string for QRCode 
        
        :param str auth_hash: The auth request hash
        :rtype: str
        :return: The QRcode string
        """
        protocol = self.base_parameters.get('protocol')
        action = self.action_auth_login
        qrcode_str = "%s://%s/?action=%s&auth_hash=%s" % (protocol.lower(), self.dapp_id, action, auth_hash)
        return qrcode_str

    def validate_auth_callback(self, data):
        """Validate the response of auth callback sent by end users such as NewPay users 
        
        :param dict data: The callback data
        :rtype: bool
        :return: True if valid data, otherwise False
        """
        newid = data.get('newid')
        signature = data.get('signature')
        signed_string = utils.generate_signature_base_string(data, "&")
        r, s = utils.split_signature(signature)
        return utils.validate_newid(r, s, signed_string, newid, self.chain_id)
    
    def get_client_login_params(self, uuid, memo=None, scope=2):
        """Get the client params for login
        params uuid: session id,random string
        params memo: request information,optional
        params scope: profile scope, 1 is for summary, 2 for detail.
        :rtype: dict
        :return: The data for client to login.
        """
        if not uuid:
            raise AttributeError(
                "uuid can not be None"
            )
        if not memo:
            memo = "default"
        login_params = {
            'action': self.action_auth_login,
            'scope': 2,
            'memo': memo,
            'uuid': uuid,
        }
        return self._get_client_base_params(login_params)

    def get_reward_tokens(self, newid):
        if not newid:
            raise AttributeError(
                "newid can not be None"
            )
        data = {
        }
        sign_data = self.generate_sign_data(data)
        hmac_data = self.sign_hmac(sign_data)
        hmac_data['api_version'] = self.api_version
        hmac_data['newid'] = newid
        return self.api_client.rest_newids_newforce_reward_list(**hmac_data)

    def get_newforce_of_partner_and_voter(self, node_wallet_address, page_id=1, page_size=50, direction=0):
        if not node_wallet_address:
            raise AttributeError(
                "node wallet address can not be None"
            )
        data = {
            'page_id': page_id,
            'page_size': page_size,
            'direction': direction,
        }
        sign_data = self.generate_sign_data(data)
        hmac_data = self.sign_hmac(sign_data)
        hmac_data["node_wallet_address"] = node_wallet_address
        hmac_data['api_version'] = self.api_version
        return self.api_client.rest_newforce_node_round_read(**hmac_data)
