import sys
import uuid
import hep_rest_api
from hep_rest_api.scenarios.auth import AuthHelper
from hep_rest_api.scenarios.pay import PayHelper
from hep_rest_api.scenarios.proof import ProofHelper
from hep_rest_api.scenarios.proof import OrderProof


PRIVATE_KEY_PATH = "/Users/erhu/pony/priv"
HEP_KEY = "71ffeae1a9a2402c944d84c54f8ffddc"
HEP_SECRET = "2d66e7f3dd4445dbb6791b56fadcd2dc"
HEP_PROTOCOL = "HEP"
HEP_PROTOCOL_VERSION = "1.0"
HEP_HOST = "http://hep.newtonproject.dev.diynova.com"
HEP_ID = "75098291f88343b9836118546f375a9f"
TEST_NEWID = "NEWID1acGJchbdZy74f3dTQxfZd6kkztfxzUgLtUyTvUtU21U4RaS72XY"
base_parameters = {
    'dapp_id': HEP_ID,
    'dapp_key': HEP_KEY,
    'protocol': HEP_PROTOCOL,
    'version': HEP_PROTOCOL_VERSION,
    'os': sys.platform,
    'language': 'en'
}
key_path = PRIVATE_KEY_PATH
configuration = hep_rest_api.api_client.Configuration()
configuration.host = HEP_HOST
api_client = hep_rest_api.RestApi(hep_rest_api.ApiClient(configuration))


def _get_api_client():
    configuration = hep_rest_api.api_client.Configuration()
    configuration.host = HEP_HOST
    api_instance = hep_rest_api.RestApi(hep_rest_api.ApiClient(configuration))
    return api_instance


def test_auth_login():
    api_client = _get_api_client()
    auth_helper = AuthHelper(api_client, base_parameters, HEP_SECRET, key_path)
    auth_resposne = auth_helper.generate_auth_request(uuid=uuid.uuid4().hex)
    qr_str = auth_helper.generate_qrcode_string(auth_resposne.auth_hash)
    print(qr_str)


def test_auth_pay():
    api_client = _get_api_client()
    pay_helper = PayHelper(api_client, base_parameters, HEP_SECRET, key_path)
    pay_response = pay_helper.generate_pay_request(uuid.uuid4().hex, "NEW", 12, "description", "NEWID1acGJchbdZy74f3dTQxfZd6kkztfxzUgLtUyTvUtU21U4RaS72XY", "NEWID1acGJchbdZy74f3dTQxfZd6kkztfxzUgLtUyTvUtU21U4RaS72XY", "NEWID1acGJchbdZy74f3dTQxfZd6kkztfxzUgLtUyTvUtU21U4RaS72XY", uuid=uuid.uuid4().hex)
    print(pay_response.pay_hash)
    pay_qr_str = pay_helper.generate_qrcode_string(pay_response.pay_hash)
    print(pay_qr_str)


def test_auth_proof():
    api_client = _get_api_client()
    order_content = OrderProof(uuid.uuid4().hex, "NEW", "20", TEST_NEWID, TEST_NEWID,TEST_NEWID, description="haha", chain_txid="0x91a662d227a62d30746e67fdc2ce7903ff63b29b5f3861b8bb2b50f64561cfaa")
    order_content.add_order_item(2, 1, 10, "NEW", "testnet", uuid.uuid4().hex, "product")
    proof_helper = ProofHelper(api_client, base_parameters, HEP_SECRET, key_path)
    proof_resposne = proof_helper.generate_proof_request(order_content.to_dict(), uuid=uuid.uuid4().hex)
    proof_str = proof_helper.generate_qrcode_string(proof_resposne.proof_hash)
    print(proof_str)


if __name__ == '__main__':
    test_auth_proof()
