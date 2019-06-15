import datetime
import uuid
import sys
import hep_rest_api
from hep_rest_api import utils

config = hep_rest_api.Configuration()
config.host = 'xx'

api_instance = hep_rest_api.RestApi(hep_rest.ApiClient(config))
api_version = '1'
dapp_id = 'xxx'
dapp_key = 'xxx'
dapp_secret = 'xx'
protocol = 'HEP'
version = '1.0'
ts = datetime.datetime.now().timestamp()
nonce = uuid.uuid4().hex
os = sys.platform
language = 'en'
dapp_signature_method = 'HMAC-MD5'
dapp_signature = ''

data = {
    'api_version': api_version,
    'dapp_id': dapp_id,
    'dapp_key': dapp_key,
    'protocol': protocol,
    'version': version,
    'ts': ts,
    'nonce': nonce,
    'os': os,
    'language': language,
    'dapp_signature_method': dapp_signature_method
}
dapp_signature = utils.sign_hmac(data, dapp_secret)
data['dapp_signature'] = dapp_signature

api_response = api_instance.rest_dapps_read(**data)
print(api_response)
