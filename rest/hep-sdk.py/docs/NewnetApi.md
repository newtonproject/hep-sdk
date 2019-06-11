# swagger_client.NewnetApi

All URIs are relative to *http://127.0.0.1:8000/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**newnet_caches_auth_create**](NewnetApi.md#newnet_caches_auth_create) | **POST** /newnet/caches/auth/ | 
[**newnet_caches_auth_read**](NewnetApi.md#newnet_caches_auth_read) | **GET** /newnet/caches/auth/{auth_hash}/ | 
[**newnet_caches_pay_create**](NewnetApi.md#newnet_caches_pay_create) | **POST** /newnet/caches/pay/ | 
[**newnet_caches_pay_read**](NewnetApi.md#newnet_caches_pay_read) | **GET** /newnet/caches/pay/{pay_hash}/ | 

# **newnet_caches_auth_create**
> CreateAuthCacheResponse newnet_caches_auth_create(body)



Caches the authentication request

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
api_instance = swagger_client.NewnetApi(swagger_client.ApiClient(configuration))
body = swagger_client.AuthCacheRequest() # AuthCacheRequest | 

try:
    api_response = api_instance.newnet_caches_auth_create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NewnetApi->newnet_caches_auth_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AuthCacheRequest**](AuthCacheRequest.md)|  | 

### Return type

[**CreateAuthCacheResponse**](CreateAuthCacheResponse.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **newnet_caches_auth_read**
> AuthCacheResponse newnet_caches_auth_read(auth_hash, dapp_key, protocol, version, ts, nonce, os, language, md5)



Get the authentication information by given request hash.

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
api_instance = swagger_client.NewnetApi(swagger_client.ApiClient(configuration))
auth_hash = 'auth_hash_example' # str | 
dapp_key = 'dapp_key_example' # str | The decentralized application access key
protocol = 'protocol_example' # str | The protocol name. default is 'HEP'.
version = 'version_example' # str | The protocol version such as '1.0'
ts = 56 # int | The current timestamp
nonce = 'nonce_example' # str | The random string or auto-increment sequence
os = 'os_example' # str | The operating system of client such as ios, android, dweb,etc.
language = 'language_example' # str | The i18n language code such as zh, en, etc.
md5 = 'md5_example' # str | The HMAC authentication md5 checksum

try:
    api_response = api_instance.newnet_caches_auth_read(auth_hash, dapp_key, protocol, version, ts, nonce, os, language, md5)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NewnetApi->newnet_caches_auth_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_hash** | **str**|  | 
 **dapp_key** | **str**| The decentralized application access key | 
 **protocol** | **str**| The protocol name. default is &#x27;HEP&#x27;. | 
 **version** | **str**| The protocol version such as &#x27;1.0&#x27; | 
 **ts** | **int**| The current timestamp | 
 **nonce** | **str**| The random string or auto-increment sequence | 
 **os** | **str**| The operating system of client such as ios, android, dweb,etc. | 
 **language** | **str**| The i18n language code such as zh, en, etc. | 
 **md5** | **str**| The HMAC authentication md5 checksum | 

### Return type

[**AuthCacheResponse**](AuthCacheResponse.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **newnet_caches_pay_create**
> CreatePayCacheResponse newnet_caches_pay_create(body)



Cache the pay request

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
api_instance = swagger_client.NewnetApi(swagger_client.ApiClient(configuration))
body = swagger_client.PayCacheRequest() # PayCacheRequest | 

try:
    api_response = api_instance.newnet_caches_pay_create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NewnetApi->newnet_caches_pay_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PayCacheRequest**](PayCacheRequest.md)|  | 

### Return type

[**CreatePayCacheResponse**](CreatePayCacheResponse.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **newnet_caches_pay_read**
> PayCacheResponse newnet_caches_pay_read(pay_hash, dapp_key, protocol, version, ts, nonce, os, language, md5)



Retrieve the pay information by given pay hash.

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
api_instance = swagger_client.NewnetApi(swagger_client.ApiClient(configuration))
pay_hash = 'pay_hash_example' # str | 
dapp_key = 'dapp_key_example' # str | The decentralized application access key
protocol = 'protocol_example' # str | The protocol name. default is 'HEP'.
version = 'version_example' # str | The protocol version such as '1.0'
ts = 56 # int | The current timestamp
nonce = 'nonce_example' # str | The random string or auto-increment sequence
os = 'os_example' # str | The operating system of client such as ios, android, dweb,etc.
language = 'language_example' # str | The i18n language code such as zh, en, etc.
md5 = 'md5_example' # str | The HMAC authentication md5 checksum

try:
    api_response = api_instance.newnet_caches_pay_read(pay_hash, dapp_key, protocol, version, ts, nonce, os, language, md5)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NewnetApi->newnet_caches_pay_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pay_hash** | **str**|  | 
 **dapp_key** | **str**| The decentralized application access key | 
 **protocol** | **str**| The protocol name. default is &#x27;HEP&#x27;. | 
 **version** | **str**| The protocol version such as &#x27;1.0&#x27; | 
 **ts** | **int**| The current timestamp | 
 **nonce** | **str**| The random string or auto-increment sequence | 
 **os** | **str**| The operating system of client such as ios, android, dweb,etc. | 
 **language** | **str**| The i18n language code such as zh, en, etc. | 
 **md5** | **str**| The HMAC authentication md5 checksum | 

### Return type

[**PayCacheResponse**](PayCacheResponse.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

