# hep_rest.RestApi

All URIs are relative to *http://127.0.0.1:8000/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_dapps_read**](RestApi.md#rest_dapps_read) | **GET** /rest/v{version}/dapps/{dapp_id}/ | 
[**rest_newids_read**](RestApi.md#rest_newids_read) | **GET** /rest/v{version}/newids/{newid}/ | 
[**rest_newnet_caches_auth_create**](RestApi.md#rest_newnet_caches_auth_create) | **POST** /rest/v{version}/newnet/caches/auth/ | 
[**rest_newnet_caches_auth_read**](RestApi.md#rest_newnet_caches_auth_read) | **GET** /rest/v{version}/newnet/caches/auth/{auth_hash}/ | 
[**rest_newnet_caches_pay_create**](RestApi.md#rest_newnet_caches_pay_create) | **POST** /rest/v{version}/newnet/caches/pay/ | 
[**rest_newnet_caches_pay_read**](RestApi.md#rest_newnet_caches_pay_read) | **GET** /rest/v{version}/newnet/caches/pay/{pay_hash}/ | 
[**rest_proofs_create**](RestApi.md#rest_proofs_create) | **POST** /rest/v{version}/proofs/ | 
[**rest_proofs_delete**](RestApi.md#rest_proofs_delete) | **DELETE** /rest/v{version}/proofs/{proof_hash}/ | 
[**rest_proofs_update**](RestApi.md#rest_proofs_update) | **PUT** /rest/v{version}/proofs/{proof_hash}/ | 

# **rest_dapps_read**
> Dapp rest_dapps_read(dapp_id, version, dapp_key, protocol, version2, ts, nonce, os, language, md5)



### Example
```python
from __future__ import print_function
import time
import hep_rest
from hep_rest.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: Basic
configuration = hep_rest.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = hep_rest.RestApi(hep_rest.ApiClient(configuration))
dapp_id = 'dapp_id_example' # str | 
version = 'version_example' # str | 
dapp_key = 'dapp_key_example' # str | The decentralized application access key
protocol = 'protocol_example' # str | The protocol name. default is 'HEP'.
version2 = 'version_example' # str | The protocol version such as '1.0'
ts = 56 # int | The current timestamp
nonce = 'nonce_example' # str | The random string or auto-increment sequence
os = 'os_example' # str | The operating system of client such as ios, android, dweb,etc.
language = 'language_example' # str | The i18n language code such as zh, en, etc.
md5 = 'md5_example' # str | The HMAC authentication md5 checksum

try:
    api_response = api_instance.rest_dapps_read(dapp_id, version, dapp_key, protocol, version2, ts, nonce, os, language, md5)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RestApi->rest_dapps_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dapp_id** | **str**|  | 
 **version** | **str**|  | 
 **dapp_key** | **str**| The decentralized application access key | 
 **protocol** | **str**| The protocol name. default is &#x27;HEP&#x27;. | 
 **version2** | **str**| The protocol version such as &#x27;1.0&#x27; | 
 **ts** | **int**| The current timestamp | 
 **nonce** | **str**| The random string or auto-increment sequence | 
 **os** | **str**| The operating system of client such as ios, android, dweb,etc. | 
 **language** | **str**| The i18n language code such as zh, en, etc. | 
 **md5** | **str**| The HMAC authentication md5 checksum | 

### Return type

[**Dapp**](Dapp.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_newids_read**
> NewidResponse rest_newids_read(newid, version, dapp_key, protocol, version2, ts, nonce, os, language, md5)



Retrieve the information by given NewID

### Example
```python
from __future__ import print_function
import time
import hep_rest
from hep_rest.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: Basic
configuration = hep_rest.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = hep_rest.RestApi(hep_rest.ApiClient(configuration))
newid = 'newid_example' # str | 
version = 'version_example' # str | 
dapp_key = 'dapp_key_example' # str | The decentralized application access key
protocol = 'protocol_example' # str | The protocol name. default is 'HEP'.
version2 = 'version_example' # str | The protocol version such as '1.0'
ts = 56 # int | The current timestamp
nonce = 'nonce_example' # str | The random string or auto-increment sequence
os = 'os_example' # str | The operating system of client such as ios, android, dweb,etc.
language = 'language_example' # str | The i18n language code such as zh, en, etc.
md5 = 'md5_example' # str | The HMAC authentication md5 checksum

try:
    api_response = api_instance.rest_newids_read(newid, version, dapp_key, protocol, version2, ts, nonce, os, language, md5)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RestApi->rest_newids_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **newid** | **str**|  | 
 **version** | **str**|  | 
 **dapp_key** | **str**| The decentralized application access key | 
 **protocol** | **str**| The protocol name. default is &#x27;HEP&#x27;. | 
 **version2** | **str**| The protocol version such as &#x27;1.0&#x27; | 
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

# **rest_newnet_caches_auth_create**
> CreateAuthCacheResponse rest_newnet_caches_auth_create(body, version)



Caches the authentication request

### Example
```python
from __future__ import print_function
import time
import hep_rest
from hep_rest.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: Basic
configuration = hep_rest.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = hep_rest.RestApi(hep_rest.ApiClient(configuration))
body = hep_rest.AuthCacheRequest() # AuthCacheRequest | 
version = 'version_example' # str | 

try:
    api_response = api_instance.rest_newnet_caches_auth_create(body, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RestApi->rest_newnet_caches_auth_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AuthCacheRequest**](AuthCacheRequest.md)|  | 
 **version** | **str**|  | 

### Return type

[**CreateAuthCacheResponse**](CreateAuthCacheResponse.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_newnet_caches_auth_read**
> AuthCacheResponse rest_newnet_caches_auth_read(auth_hash, version, dapp_key, protocol, version2, ts, nonce, os, language, md5)



Get the authentication information by given request hash.

### Example
```python
from __future__ import print_function
import time
import hep_rest
from hep_rest.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: Basic
configuration = hep_rest.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = hep_rest.RestApi(hep_rest.ApiClient(configuration))
auth_hash = 'auth_hash_example' # str | 
version = 'version_example' # str | 
dapp_key = 'dapp_key_example' # str | The decentralized application access key
protocol = 'protocol_example' # str | The protocol name. default is 'HEP'.
version2 = 'version_example' # str | The protocol version such as '1.0'
ts = 56 # int | The current timestamp
nonce = 'nonce_example' # str | The random string or auto-increment sequence
os = 'os_example' # str | The operating system of client such as ios, android, dweb,etc.
language = 'language_example' # str | The i18n language code such as zh, en, etc.
md5 = 'md5_example' # str | The HMAC authentication md5 checksum

try:
    api_response = api_instance.rest_newnet_caches_auth_read(auth_hash, version, dapp_key, protocol, version2, ts, nonce, os, language, md5)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RestApi->rest_newnet_caches_auth_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_hash** | **str**|  | 
 **version** | **str**|  | 
 **dapp_key** | **str**| The decentralized application access key | 
 **protocol** | **str**| The protocol name. default is &#x27;HEP&#x27;. | 
 **version2** | **str**| The protocol version such as &#x27;1.0&#x27; | 
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

# **rest_newnet_caches_pay_create**
> CreatePayCacheResponse rest_newnet_caches_pay_create(body, version)



Cache the pay request

### Example
```python
from __future__ import print_function
import time
import hep_rest
from hep_rest.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: Basic
configuration = hep_rest.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = hep_rest.RestApi(hep_rest.ApiClient(configuration))
body = hep_rest.PayCacheRequest() # PayCacheRequest | 
version = 'version_example' # str | 

try:
    api_response = api_instance.rest_newnet_caches_pay_create(body, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RestApi->rest_newnet_caches_pay_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PayCacheRequest**](PayCacheRequest.md)|  | 
 **version** | **str**|  | 

### Return type

[**CreatePayCacheResponse**](CreatePayCacheResponse.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_newnet_caches_pay_read**
> PayCacheResponse rest_newnet_caches_pay_read(pay_hash, version, dapp_key, protocol, version2, ts, nonce, os, language, md5)



Retrieve the pay information by given pay hash.

### Example
```python
from __future__ import print_function
import time
import hep_rest
from hep_rest.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: Basic
configuration = hep_rest.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = hep_rest.RestApi(hep_rest.ApiClient(configuration))
pay_hash = 'pay_hash_example' # str | 
version = 'version_example' # str | 
dapp_key = 'dapp_key_example' # str | The decentralized application access key
protocol = 'protocol_example' # str | The protocol name. default is 'HEP'.
version2 = 'version_example' # str | The protocol version such as '1.0'
ts = 56 # int | The current timestamp
nonce = 'nonce_example' # str | The random string or auto-increment sequence
os = 'os_example' # str | The operating system of client such as ios, android, dweb,etc.
language = 'language_example' # str | The i18n language code such as zh, en, etc.
md5 = 'md5_example' # str | The HMAC authentication md5 checksum

try:
    api_response = api_instance.rest_newnet_caches_pay_read(pay_hash, version, dapp_key, protocol, version2, ts, nonce, os, language, md5)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RestApi->rest_newnet_caches_pay_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pay_hash** | **str**|  | 
 **version** | **str**|  | 
 **dapp_key** | **str**| The decentralized application access key | 
 **protocol** | **str**| The protocol name. default is &#x27;HEP&#x27;. | 
 **version2** | **str**| The protocol version such as &#x27;1.0&#x27; | 
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

# **rest_proofs_create**
> CreateProofResponse rest_proofs_create(body, version)



### Example
```python
from __future__ import print_function
import time
import hep_rest
from hep_rest.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: Basic
configuration = hep_rest.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = hep_rest.RestApi(hep_rest.ApiClient(configuration))
body = hep_rest.CreateProofRequest() # CreateProofRequest | 
version = 'version_example' # str | 

try:
    api_response = api_instance.rest_proofs_create(body, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RestApi->rest_proofs_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateProofRequest**](CreateProofRequest.md)|  | 
 **version** | **str**|  | 

### Return type

[**CreateProofResponse**](CreateProofResponse.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_proofs_delete**
> CancelProofResponse rest_proofs_delete(body, proof_hash, version)



### Example
```python
from __future__ import print_function
import time
import hep_rest
from hep_rest.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: Basic
configuration = hep_rest.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = hep_rest.RestApi(hep_rest.ApiClient(configuration))
body = hep_rest.CancelProofRequest() # CancelProofRequest | 
proof_hash = 'proof_hash_example' # str | 
version = 'version_example' # str | 

try:
    api_response = api_instance.rest_proofs_delete(body, proof_hash, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RestApi->rest_proofs_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CancelProofRequest**](CancelProofRequest.md)|  | 
 **proof_hash** | **str**|  | 
 **version** | **str**|  | 

### Return type

[**CancelProofResponse**](CancelProofResponse.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_proofs_update**
> UpdateProofResponse rest_proofs_update(body, proof_hash, version)



### Example
```python
from __future__ import print_function
import time
import hep_rest
from hep_rest.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: Basic
configuration = hep_rest.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = hep_rest.RestApi(hep_rest.ApiClient(configuration))
body = hep_rest.UpdateProofRequest() # UpdateProofRequest | 
proof_hash = 'proof_hash_example' # str | 
version = 'version_example' # str | 

try:
    api_response = api_instance.rest_proofs_update(body, proof_hash, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RestApi->rest_proofs_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateProofRequest**](UpdateProofRequest.md)|  | 
 **proof_hash** | **str**|  | 
 **version** | **str**|  | 

### Return type

[**UpdateProofResponse**](UpdateProofResponse.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

