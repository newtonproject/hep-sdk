import datetime
import hep_rest
from hep_rest import utils

config = hep_rest.Configuration()
config.host = 'http://hep.newtonproject.dev.diynova.com/'

api_instance = hep_rest.RestApi(hep_rest.ApiClient(config))
api_version = '1'
dapp_id = '05e6e4bbd71f4ab8ac382f8c0ccb8d0b'
dapp_key = '0a3b1bb80adc4b0595ebc8aa8ff2fa5d'
dapp_secret = 'a5ef1dce6c644c83adf04b215e98d820'
protocol = 'HEP'
version = '1.0'
ts = datetime.datetime.now().timestamp()
nonce = 'nonce_example'
os = 'linux'
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
