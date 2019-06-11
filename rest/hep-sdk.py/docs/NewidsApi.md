# swagger_client.NewidsApi

All URIs are relative to *http://127.0.0.1:8000/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**newids_read**](NewidsApi.md#newids_read) | **GET** /newids/{newid}/ | 

# **newids_read**
> NewidResponse newids_read(newid, dapp_key, protocol, version, ts, nonce, os, language, md5)



Retrieve the information by given NewID

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: Basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.NewidsApi(swagger_client.ApiClient(configuration))
newid = 'newid_example' # str | 
dapp_key = 'dapp_key_example' # str | The decentralized application access key
protocol = 'protocol_example' # str | The protocol name. default is 'HEP'.
version = 'version_example' # str | The protocol version such as '1.0'
ts = 56 # int | The current timestamp
nonce = 'nonce_example' # str | The random string or auto-increment sequence
os = 'os_example' # str | The operating system of client such as ios, android, dweb,etc.
language = 'language_example' # str | The i18n language code such as zh, en, etc.
md5 = 'md5_example' # str | The HMAC authentication md5 checksum

try:
    api_response = api_instance.newids_read(newid, dapp_key, protocol, version, ts, nonce, os, language, md5)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NewidsApi->newids_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **newid** | **str**|  | 
 **dapp_key** | **str**| The decentralized application access key | 
 **protocol** | **str**| The protocol name. default is &#x27;HEP&#x27;. | 
 **version** | **str**| The protocol version such as &#x27;1.0&#x27; | 
 **ts** | **int**| The current timestamp | 
 **nonce** | **str**| The random string or auto-increment sequence | 
 **os** | **str**| The operating system of client such as ios, android, dweb,etc. | 
 **language** | **str**| The i18n language code such as zh, en, etc. | 
 **md5** | **str**| The HMAC authentication md5 checksum | 

### Return type

[**NewidResponse**](NewidResponse.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

