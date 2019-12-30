# -*- coding: utf-8 -*-

__copyright__ = """ Copyright (c) 2019 Newton Foundation. All rights reserved."""
__version__ = '$'
__author__ = 'liuchao@diynova.com'

import logging
import datetime
import uuid
from hep_rest_api.scenarios import BaseHelper
from hep_rest_api import models
from hep_rest_api import utils

logger = logging.getLogger(__name__)


class NewChainHelper(BaseHelper):

    def __init__(self, api_client, base_parameters, dapp_id, dapp_secret, key_path, api_version='1', chain_id=1012):
        super(NewChainHelper, self).__init__(api_client, base_parameters, dapp_id, dapp_secret, key_path, api_version='1', chain_id=1012)
        self.action_gravity_mint = "hep.gravity.mint.submit"
        self.action_gravity_collect = "hep.gravity.mint.collect"
        self.action_gravity_subscribe = "hep.gravity.subscribe"

    def get_gravity_account(self, newid):
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
        return self.api_client.rest_newchain_coin_gravity_account_read(**hmac_data)

    def get_gravity_mint_condition(self, newid):
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
        return self.api_client.rest_newchain_coin_gravity_mint_condition_read(**hmac_data)

    def get_current_mint_data(self, newid):
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
        return self.api_client.rest_newchain_coin_gravity_mint_data_current_read(**hmac_data)

    def get_history_mint_data(self, newid, page_id=0, page_size=20):
        if not newid:
            raise AttributeError(
                "newid can not be None"
            )
        data = {
            "newid": newid,
            "page_id": page_id,
            "page_size": page_size
        }
        sign_data = self.generate_sign_data(data)
        hmac_data = self.sign_hmac(sign_data)
        history_data_request = models.HistoryDataRequest(**hmac_data)
        return self.api_client.rest_newchain_coin_gravity_mint_data_history_create(
            data=history_data_request,
            api_version=self.api_version
        )

    def mint_submit(self, newid, tx_tokens, tx_gravity):
        if not newid:
            raise AttributeError(
                "newid can not be None"
            )
        if not tx_tokens:
            raise AttributeError(
                "tx_tokens can not be None"
            )
        if not tx_gravity:
            raise AttributeError(
                "tx_gravity can not be None"
            )
        data = {
            "newid": newid,
            "tx_tokens": tx_tokens,
            "tx_gravity": tx_gravity,
            "action": self.action_gravity_mint,
            "uuid": uuid.uuid4().hex,
            "dapp_id": self.dapp_id
        }
        sign_data = self.generate_sign_data(data)
        hmac_data = self.sign_hmac(sign_data)
        final_data = self.sign_secp256r1(hmac_data)
        submit_mint_request = models.SubmitMintRequest(**final_data)
        return self.api_client.rest_newchain_coin_gravity_mint_submit_create(
            data=submit_mint_request,
            api_version=self.api_version
        )

    def mint_collect(self, newid):
        if not newid:
            raise AttributeError(
                "newid can not be None"
            )
        data = {
            "newid": newid,
            "action": self.action_gravity_collect,
            "uuid": uuid.uuid4().hex,
            "dapp_id": self.dapp_id
        }
        sign_data = self.generate_sign_data(data)
        hmac_data = self.sign_hmac(sign_data)
        final_data = self.sign_secp256r1(hmac_data)
        collect_mint_request = models.CollectMintRequest(**final_data)
        return self.api_client.rest_newchain_coin_gravity_mint_collect_create(
            data=collect_mint_request,
            api_version=self.api_version
        )

    def get_gravity_subscribe_condition(self, newid):
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
        return self.api_client.rest_newchain_coin_gravity_subscription_condition_read(**hmac_data)

    def subscribe_submit(self, newid, tx):
        if not newid:
            raise AttributeError(
                "newid can not be None"
            )
        if not tx:
            raise AttributeError(
                "tx can not be None"
            )
        data = {
            "newid": newid,
            "tx": tx,
            "action": self.action_gravity_subscribe,
            "uuid": uuid.uuid4().hex,
            "dapp_id": self.dapp_id
        }
        sign_data = self.generate_sign_data(data)
        hmac_data = self.sign_hmac(sign_data)
        final_data = self.sign_secp256r1(hmac_data)
        subscribe_request = models.SubmitSubscribeRequest(**final_data)
        return self.api_client.rest_newchain_coin_gravity_subscription_submit_create(
            data=subscribe_request,
            api_version=self.api_version
        )
