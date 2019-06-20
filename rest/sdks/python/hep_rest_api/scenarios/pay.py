"""The implementation of HEP Payment protocol

"""

__copyright__ = """ Copyright (c) 2019 Newton Foundation. All rights reserved."""
__version__ = '1.0'
__author__ = 'xiawu@zeuux.org'

import logging
from hep_rest_api.scenarios import BaseHelper

logger = logging.getLogger(__name__)

class PayHelper(BaseHelper):
    def generate_pay_request(self,
                             dapp_id,
                             order_number,
                             price_currency,
                             total_price,
                             description,
                             seller,
                             customer,
                             broker='',
                             action='hep.pay.order',
                             expired=300,
                             uuid=None):
        """Generate the payment request
        
        :param str dapp_id: The DApp ID
        :param str order_number: The order number
        :param str price_currency: The symbol of fiat or digital token, such as USD, CNY, NEW,BTC,ETH.
        :param str total_price: The amount of fiat or digital token, unit is the minimum unit of given fiat or digital token.
        :param str description: The order description
        :param str seller: The seller's NewID
        :param str customer: The customer's NewID
        :param str broker: The broker's NewID. optional.
        :param str action: The request action name
        :param int expired: The expired time of request
        :param str uuid: The request uuid for desktop-browser. optional.
        :rtype: dict
        :return: The request information including signature
        """
        pass

    def generate_qrcode_string(self, pay_request):
        """Generate the hep-based scheme string string for QRCode 
        
        :param dict pay_request: The pay request
        :rtype: str
        :return: The QRcode string
        """
        pass

    def validate_pay_callback(self, data):
        """Validate the response of pay callback sent by end users such as NewPay users 
        
        :param dict data: The callback data
        :rtype: bool
        :return: True if valid data, otherwise False
        """
        pass


