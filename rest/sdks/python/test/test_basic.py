import sys
import uuid
import os
import datetime
# set the path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE_DIR, ""))
from sha3 import keccak_256
import hep_rest_api
from hep_rest_api import utils
from hep_rest_api.scenarios.auth import AuthHelper
from hep_rest_api.scenarios.pay import PayHelper
from hep_rest_api.scenarios.proof import ProofHelper
from hep_rest_api.scenarios.proof import OrderProof
from hep_rest_api.scenarios.proof import Order
print(BASE_DIR)
config_dev = {
    'app_id' : 'd32db928a0034598a69bdf375551f822',
    'app_key': '02c3119710714730b000db31d73052ce',
    'app_secret': 'eae92dbda0454049b8016a43c2d7025e',
    'private_path' : BASE_DIR + "/test/priv/priv",
    'hep_host': 'https://node.hep.testnet.newtonproject.org',
    'protocol': 'HEP',
    'protocol_version': '1.0',
    'chain_id': 1002
}
config_test = {
    'app_id' : 'ad153ffe8cff4677ae2edd5d5670d408',
    'app_key': 'e3e3b730955d4f7ca405645f17c6dd1d',
    'app_secret': '70dc942a981e469686c5b94108393eb9',
    'private_path': BASE_DIR + "/test/priv/priv",
    'hep_host': 'http://hep.newtonproject.dev.diynova.com',
    #'hep_host': 'http://127.0.0.1:8000',
    'protocol': 'HEP',
    'protocol_version': '1.0',
    'chain_id': 1007
}
config = config_dev

TEST_NEWID = "NEWID1acGJchbdZy74f3dTQxfZd6kkztfxzUgLtUyTvUtU21U4RaS72XY"

base_parameters = {
    'dapp_key': config['app_key'],
    'protocol': config['protocol'],
    'version': config['protocol_version'],
    'os': sys.platform,
    'language': 'en'
}
chain_id = config['chain_id']
key_path = config['private_path']
HEP_ID = config['app_id']
HEP_SECRET = config['app_secret']
payment_data = {"dapp_id": "75098291f88343b9836118546f375a9f", "nonce": "92ac0a98ba1742c48eb8e91100077817", "sign_type": "secp256r1", "signature": "0xee47bd99d1807b7a14bb36c9e9fe641753f13e3c5d77610121edd3e125ddf78d22a56c98de8012d185b6de0da27aaef4101d3fe4beb5cf3038bc134d73012f48", "ts": "1561121020", "txid": "0xd7ab1ddcad52efd96298610030c985083cb6639b3f0f07c86f51ea7845a61237", "uuid": "b8e89a114b104a8d83e0266bbc5a55a1"}
login_data = {"action": "hep.auth.login", "scope": 1, "expired": 1561129670, "memo": "default", "uuid": "682749f075b74702b8c41c9a75862b0a", "dapp_id": "75098291f88343b9836118546f375a9f", "dapp_key": "71ffeae1a9a2402c944d84c54f8ffddc", "protocol":"HEP", "version": "1.0", "os": "darwin", "language": "en", "ts": 1561129370, "nonce": "ae892ffdf7ee430a992f29b5760d4e69", "dapp_signature": "046fbe22f261c5e5b62b37679b8f5a99", "dapp_signature_method": "HMAC-MD5", "signature": "0xf33c0e088f1cb64a8d0845a62333500d73b227c242e36dcf902da4243e515472dd2de175443b2918c52fbd6abbcbbace98a8e75540a93e3d29628096437f09e7", "sign_type": "secp256r1"}
login_profile = {"address": "NEW17xYWcvn5cp7rgYubVeenHZLGDJ5JtJapUPm", "avatar": "", "cellphone": "18888888881", "country_code": "86", "invite_code": "XLFFKD", "name":"不上班", "newid": "NEWID1acGJchbdZy74f3dTQxfZd6kkztfxzUgLtUyTvUtU21U4RaS72XY", "sign_type": "secp256r1", "signature": "0x8132dc49de81e4a1b85aaaa142fce6502f1093d495004240c2fee7bbf39e7ddb5c4565537ebb9b50312b6c34d267724f6567aa473dc85c9b268efc8f46f2235d", "uuid": "c11494156640416393a8d7c9926ffa87"}

def _get_api_client():
    configuration = hep_rest_api.api_client.Configuration()
    configuration.host = config['hep_host']
    api_instance = hep_rest_api.RestApi(hep_rest_api.ApiClient(configuration))
    return api_instance

api_client = _get_api_client()
auth_helper = AuthHelper(api_client, base_parameters, HEP_ID, HEP_SECRET, key_path, chain_id=chain_id)
pay_helper = PayHelper(api_client, base_parameters, HEP_ID, HEP_SECRET, key_path, chain_id=chain_id)
proof_helper = ProofHelper(api_client, base_parameters, HEP_ID, HEP_SECRET, key_path, chain_id=chain_id)

def test_auth_login():
    auth_resposne = auth_helper.generate_auth_request(uuid=uuid.uuid4().hex)
    qr_str = auth_helper.generate_qrcode_string(auth_resposne.auth_hash)
    print(qr_str)
    is_valid = auth_helper.validate_auth_callback(login_profile)
    print(is_valid)
    
def test_auth_login_client():
    login_params = auth_helper.get_client_login_params(uuid.uuid4().hex, "haha", 2)
    print(login_params)


def test_auth_pay():
    pay_response = pay_helper.generate_pay_request(uuid.uuid4().hex, "NEW", "12", "description", "NEWID1acGJchbdZy74f3dTQxfZd6kkztfxzUgLtUyTvUtU21U4RaS72XY", "NEWID1acGJchbdZy74f3dTQxfZd6kkztfxzUgLtUyTvUtU21U4RaS72XY", "NEWID1acGJchbdZy74f3dTQxfZd6kkztfxzUgLtUyTvUtU21U4RaS72XY", uuid=uuid.uuid4().hex)
    print(pay_response.pay_hash)
    pay_qr_str = pay_helper.generate_qrcode_string(pay_response.pay_hash)
    print(pay_qr_str)
    is_valid = pay_helper.validate_pay_callback(payment_data)
    print(is_valid)
    pay_data = {'api_version': '1', 'dapp_key': '71ffeae1a9a2402c944d84c54f8ffddc', 'protocol': 'HEP', 'version': '1.0', 'os': 'darwin', 'language': 'en', 'ts': 1561189219, 'nonce': '7fd6675608ba49d48c4e5c2f7e87bd8f', 'dapp_signature': 'beccf75e3f0aad44e25e8a50c37f7476', 'dapp_signature_method': 'HMAC-MD5', 'txid': '0xd7ab1ddcad52efd96298610030c985083cb6639b3f0f07c86f51ea7845a61237'}
    response = pay_helper.get_confirmed_transaction(pay_data['txid'])
    print(response)

def test_auth_pay_client():
    res = pay_helper.get_client_pay_params(uuid.uuid4().hex, "NEW", 12, "description", "NEWID1acGJchbdZy74f3dTQxfZd6kkztfxzUgLtUyTvUtU21U4RaS72XY", "NEWID1acGJchbdZy74f3dTQxfZd6kkztfxzUgLtUyTvUtU21U4RaS72XY", "NEWID1acGJchbdZy74f3dTQxfZd6kkztfxzUgLtUyTvUtU21U4RaS72XY", uuid=uuid.uuid4().hex)
    print(res)

def test_auth_proof():
    order = Order( uuid.uuid4().hex, "deacription", "30", "CNY", TEST_NEWID, TEST_NEWID)
    order.add_order_item(uuid.uuid4().hex, "1", "10", "CNY", "pingguo", uuid.uuid4().hex)
    order.add_order_item(uuid.uuid4().hex, "2", "20", "CNY", "xiangjiao", uuid.uuid4().hex)
    order_content = OrderProof("30", "CNY", TEST_NEWID)
    order_content.add_order(order.to_dict())
    # proof_helper.validate_proof_callback({})
    print("start proof")
    proof_resposne = proof_helper.generate_proof_request(order_content.to_dict(), uuid=uuid.uuid4().hex)
    # proof_str = proof_helper.generate_qrcode_string(proof_resposne.proof_hash)
    print(proof_resposne)
    # proof_hashes = [
    #     proof_resposne.proof_hash
    # ]
    # response = proof_helper.get_status_of_proofs(proof_hashes)
    # print(response)

def test_auth_proof_client():
    res = proof_helper.get_client_proof_params(uuid.uuid4().hex, "proofhash")
    print(res)

def test_proof_callback():
    data = {"sign_type":"secp256r1","ts":"1562901022","signature":"0x796cb9876246bda055770d45d125e73350386fa20b81255d53ce44328a9dbc59e08a9e2605cc69281acfcda45b0586fb9db691acdb507af9f0b81b5a8f1ce714","uuid":"10096d6c-dffe-482c-91c1-8284dec83255","dapp_id":"565dcbe6d16d41b7ac4c7beebff44027","proof_hash":"2462d64549144208a73a1975c0d14391","nonce":"3557d6ae73524634b9ef70b4818f04b7"}
    api_client = _get_api_client()
    proof_helper = ProofHelper(api_client, base_parameters, config['app_id'], config['app_secret'], key_path, chain_id=chain_id)
    res = proof_helper.validate_proof_callback(data)
    print(res)


def test_dapp_daily_stats():
    dapp_id = ""
    time = ""
    api_client = _get_api_client()
    #    def rest_dapps_read_0(self, api_version, dapp_id, _date, dapp_key, protocol, version, ts, nonce, os, language, dapp_signature_method, dapp_signature, **kwargs):  # noqa: E501

    res = api_client.rest_dapps_read_0("1", "b8774f668c144aa78db2cd1b925284b2", "20190711", config['app_key'], 'HEP', '1.0', int(datetime.datetime.now().timestamp()), "nonce", 
                        "web", "en", "HMAC-MD5", "signature")
    print(res)


if __name__ == '__main__':
    message = "你好"
    r, s = utils.sign_secp256r1(message, key_path)
    print("r : %s   s: %s" %(r, s))
    pubs = ['0xc710c38f6042934940967f644943029229fb5180c42bda613c9f3edad120fc7f5dadf3d175733685f1c36de733c2ec2d01571d52a57e1eca121ec60f26e4dc8e']
    #r = "0xb5957b043805942e05fdbdb878cf10215408a318204f2e27a8671979602ae5ed"
    #s = "0x7e8ee6ca762ae1785f894ee5263304c934c2c889a2808cbd96636c4d4d2d3f6b"
    res = utils.validate_secp256r1_signature(r, s, message, pubs)
    print(res)
