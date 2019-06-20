"""The implementation of HEP Proof protocol

"""

__copyright__ = """ Copyright (c) 2019 Newton Foundation. All rights reserved."""
__version__ = '1.0'
__author__ = 'xiawu@zeuux.org'

import logging
from hep_rest_api.scenarios import BaseHelper

logger = logging.getLogger(__name__)

class OrderProof(object):
    def __init__(self,
                 order_number, # The order number
                 price_currency, # The symbol of fiat or digital token, such as USD, RMB, NEW,BTC,ETH.
                 total_price, # The amount of fiat or digital token, unit is the minimum unit of given fiat or digital token.
                 seller, # The seller's NewID
                 customer, # The customer's NewID
                 broker='', # The broker's NewID. optional.
                 proof_type='order', # The proof type which value is "order".
                 description='', # The order description
                 chain_txid='' # The txid of blockchain. optional.
    ):
        self.order_number = order_number
        self.price_currency = price_currency
        self.total_price = total_price
        self.seller = seller
        self.customer = customer
        self.broker = broker
        self.proof_type = proof_type
        self.description = description
        self.chain_txid = chain_txid
        self.order_items = []

    def add_order_item(self,
                       order_item_number, # The identifier of the order item.
                       order_item_quantity, # The number of the item ordered. If the property is not set, assume the quantity is one.
                       price, # The order item's price
                       price_currency, # The symbol of fiat or digital token, such as USD, CNY, NEW,BTC,ETH.
                       thing_name, # The thing name such as product or service name.
                       thing_id, # The thing id such as sku, ISBN.
                       thing_type='product' # The thing type such as product or service.
    ):
        self.order_items.append({
            'order_item_number': order_item_number,
            'order_item_quantity': order_item_quantity,
            'price': price,
            'price_currency': price_currency,
            'ordered_item': {
                'thing_name': thing_name,
                'thing_id': thing_id,
                'thing_type': thing_type,
            }
        })

    def to_dict(self):
        return {
            'order_number': self.order_number,
            'price_currency': self.price_currency,
            'total_price': self.total_price,
            'seller': self.seller,
            'customer': self.customer,
            'broker': self.broker,
            'proof_type': self.proof_type,
            'description': self.description,
            'chain_txid': self.chain_txid,
            'order_items': self.order_items
        }

    
class ProofHelper(BaseHelper):
    def generate_proof_request(self,
                               dapp_id,
                               content,
                               action='hep.proof.submit',
                               expired=300,
                               uuid=None):
        """Generate the payment request
        
        :param str dapp_id: The DApp ID
        :param dict content: The content. it can be generated by OrderProof utility.
        :param str action: The request action name
        :param int expired: The expired time of request
        :param str uuid: The request uuid for desktop-browser. optional.
        :rtype: dict
        :return: The request information including signature
        """
        pass

    def generate_qrcode_string(self, proof_request):
        """Generate the hep-based scheme string string for QRCode 
        
        :param dict proof_request: The proof request
        :rtype: str
        :return: The QRcode string
        """
        pass

    def validate_proof_callback(self, data):
        """Validate the response of proof callback sent by end users such as NewPay users 
        
        :param dict data: The callback data
        :rtype: bool
        :return: True if valid data, otherwise False
        """
        pass
