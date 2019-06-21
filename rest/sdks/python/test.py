import sys
import uuid
import hep_rest_api
from hep_rest_api.scenarios.auth import AuthHelper

PRIVATE_KEY_PATH = "/Users/erhu/pony/priv"
HEP_KEY = "71ffeae1a9a2402c944d84c54f8ffddc"
HEP_SECRET = "2d66e7f3dd4445dbb6791b56fadcd2dc"
HEP_PROTOCOL = "HEP"
HEP_PROTOCOL_VERSION = "1.0"
HEP_HOST = "http://hep.newtonproject.dev.diynova.com"
HEP_ID = "75098291f88343b9836118546f375a9f"
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
    qr_str = auth_helper.generate_qrcode_string(auth_resposne)
    print(qr_str)


if __name__ == '__main__':
    test_auth_login()
