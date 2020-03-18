# hep_rest_api.RestApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_dapps_read**](RestApi.md#rest_dapps_read) | **GET** /rest/v{api_version}/dapps/{dapp_id}/ | 
[**rest_dapps_read_0**](RestApi.md#rest_dapps_read_0) | **GET** /rest/v{api_version}/dapps/{dapp_id}/{date}/ | 
[**rest_health_list**](RestApi.md#rest_health_list) | **GET** /rest/v{api_version}/health/ | 
[**rest_newchain_coin_gravity_account_read**](RestApi.md#rest_newchain_coin_gravity_account_read) | **GET** /rest/v{api_version}/newchain/coin/gravity/account/{newid}/ | 
[**rest_newchain_coin_gravity_mint_collect_create**](RestApi.md#rest_newchain_coin_gravity_mint_collect_create) | **POST** /rest/v{api_version}/newchain/coin/gravity/mint/collect/ | 
[**rest_newchain_coin_gravity_mint_condition_read**](RestApi.md#rest_newchain_coin_gravity_mint_condition_read) | **GET** /rest/v{api_version}/newchain/coin/gravity/mint/condition/{newid}/ | 
[**rest_newchain_coin_gravity_mint_data_current_read**](RestApi.md#rest_newchain_coin_gravity_mint_data_current_read) | **GET** /rest/v{api_version}/newchain/coin/gravity/mint/data/current/{newid}/ | 
[**rest_newchain_coin_gravity_mint_data_history_create**](RestApi.md#rest_newchain_coin_gravity_mint_data_history_create) | **POST** /rest/v{api_version}/newchain/coin/gravity/mint/data/history/ | 
[**rest_newchain_coin_gravity_mint_submit_create**](RestApi.md#rest_newchain_coin_gravity_mint_submit_create) | **POST** /rest/v{api_version}/newchain/coin/gravity/mint/submit/ | 
[**rest_newchain_coin_gravity_subscription_condition_read**](RestApi.md#rest_newchain_coin_gravity_subscription_condition_read) | **GET** /rest/v{api_version}/newchain/coin/gravity/subscription/condition/{newid}/ | 
[**rest_newchain_coin_gravity_subscription_submit_create**](RestApi.md#rest_newchain_coin_gravity_subscription_submit_create) | **POST** /rest/v{api_version}/newchain/coin/gravity/subscription/submit/ | 
[**rest_newchain_tx_read**](RestApi.md#rest_newchain_tx_read) | **GET** /rest/v{api_version}/newchain/tx/{txid}/ | 
[**rest_newforce_node_round_read**](RestApi.md#rest_newforce_node_round_read) | **GET** /rest/v{api_version}/newforce/node/round/{node_wallet_address}/ | 
[**rest_newforce_read**](RestApi.md#rest_newforce_read) | **GET** /rest/v{api_version}/newforce/{date}/ | 
[**rest_newids_newforce_reward_list**](RestApi.md#rest_newids_newforce_reward_list) | **GET** /rest/v{api_version}/newids/{newid}/newforce/reward/ | 
[**rest_newids_read**](RestApi.md#rest_newids_read) | **GET** /rest/v{api_version}/newids/{newid}/ | 
[**rest_newnet_caches_auth_create**](RestApi.md#rest_newnet_caches_auth_create) | **POST** /rest/v{api_version}/newnet/caches/auth/ | 
[**rest_newnet_caches_auth_read**](RestApi.md#rest_newnet_caches_auth_read) | **GET** /rest/v{api_version}/newnet/caches/auth/{auth_hash}/ | 
[**rest_newnet_caches_pay_create**](RestApi.md#rest_newnet_caches_pay_create) | **POST** /rest/v{api_version}/newnet/caches/pay/ | 
[**rest_newnet_caches_pay_read**](RestApi.md#rest_newnet_caches_pay_read) | **GET** /rest/v{api_version}/newnet/caches/pay/{pay_hash}/ | 
[**rest_oracles_read**](RestApi.md#rest_oracles_read) | **GET** /rest/v{api_version}/oracles/{oracle_id}/ | 
[**rest_proofs_create**](RestApi.md#rest_proofs_create) | **POST** /rest/v{api_version}/proofs/ | 
[**rest_proofs_delete**](RestApi.md#rest_proofs_delete) | **DELETE** /rest/v{api_version}/proofs/{proof_hash}/ | 
[**rest_proofs_read**](RestApi.md#rest_proofs_read) | **GET** /rest/v{api_version}/proofs/{proof_hash}/ | 
[**rest_proofs_receipts_create**](RestApi.md#rest_proofs_receipts_create) | **POST** /rest/v{api_version}/proofs/receipts/ | 
[**rest_proofs_rewards_create**](RestApi.md#rest_proofs_rewards_create) | **POST** /rest/v{api_version}/proofs/rewards/ | 

# **rest_dapps_read**
> Dapp rest_dapps_read(api_version, dapp_id, dapp_key, protocol, version, ts, nonce, os, language, dapp_signature_method, dapp_signature)



### Example
```python
from __future__ import print_function
import time
import hep_rest_api
from hep_rest_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hep_rest_api.RestApi()
api_version = 'api_version_example' # str | 
dapp_id = 'dapp_id_example' # str | 
dapp_key = 'dapp_key_example' # str | The decentralized application access key
protocol = 'protocol_example' # str | The protocol name. default is 'HEP'.
version = 'version_example' # str | The protocol version such as '1.0'
ts = 56 # int | The current timestamp
nonce = 'nonce_example' # str | The random string or auto-increment sequence
os = 'os_example' # str | The operating system of client such as ios, android, dweb,etc.
language = 'language_example' # str | The i18n language code such as zh, en, etc.
dapp_signature_method = 'dapp_signature_method_example' # str | The signature method used by dapp.
dapp_signature = 'dapp_signature_example' # str | The signature generated by dapp.

try:
    api_response = api_instance.rest_dapps_read(api_version, dapp_id, dapp_key, protocol, version, ts, nonce, os, language, dapp_signature_method, dapp_signature)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RestApi->rest_dapps_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**|  | 
 **dapp_id** | **str**|  | 
 **dapp_key** | **str**| The decentralized application access key | 
 **protocol** | **str**| The protocol name. default is &#x27;HEP&#x27;. | 
 **version** | **str**| The protocol version such as &#x27;1.0&#x27; | 
 **ts** | **int**| The current timestamp | 
 **nonce** | **str**| The random string or auto-increment sequence | 
 **os** | **str**| The operating system of client such as ios, android, dweb,etc. | 
 **language** | **str**| The i18n language code such as zh, en, etc. | 
 **dapp_signature_method** | **str**| The signature method used by dapp. | 
 **dapp_signature** | **str**| The signature generated by dapp. | 

### Return type

[**Dapp**](Dapp.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_dapps_read_0**
> RetrieveDappDailyStatsResponse rest_dapps_read_0(api_version, dapp_id, _date, dapp_key, protocol, version, ts, nonce, os, language, dapp_signature_method, dapp_signature)



### Example
```python
from __future__ import print_function
import time
import hep_rest_api
from hep_rest_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hep_rest_api.RestApi()
api_version = 'api_version_example' # str | 
dapp_id = 'dapp_id_example' # str | 
_date = '_date_example' # str | 
dapp_key = 'dapp_key_example' # str | The decentralized application access key
protocol = 'protocol_example' # str | The protocol name. default is 'HEP'.
version = 'version_example' # str | The protocol version such as '1.0'
ts = 56 # int | The current timestamp
nonce = 'nonce_example' # str | The random string or auto-increment sequence
os = 'os_example' # str | The operating system of client such as ios, android, dweb,etc.
language = 'language_example' # str | The i18n language code such as zh, en, etc.
dapp_signature_method = 'dapp_signature_method_example' # str | The signature method used by dapp.
dapp_signature = 'dapp_signature_example' # str | The signature generated by dapp.

try:
    api_response = api_instance.rest_dapps_read_0(api_version, dapp_id, _date, dapp_key, protocol, version, ts, nonce, os, language, dapp_signature_method, dapp_signature)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RestApi->rest_dapps_read_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**|  | 
 **dapp_id** | **str**|  | 
 **_date** | **str**|  | 
 **dapp_key** | **str**| The decentralized application access key | 
 **protocol** | **str**| The protocol name. default is &#x27;HEP&#x27;. | 
 **version** | **str**| The protocol version such as &#x27;1.0&#x27; | 
 **ts** | **int**| The current timestamp | 
 **nonce** | **str**| The random string or auto-increment sequence | 
 **os** | **str**| The operating system of client such as ios, android, dweb,etc. | 
 **language** | **str**| The i18n language code such as zh, en, etc. | 
 **dapp_signature_method** | **str**| The signature method used by dapp. | 
 **dapp_signature** | **str**| The signature generated by dapp. | 

### Return type

[**RetrieveDappDailyStatsResponse**](RetrieveDappDailyStatsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_health_list**
> rest_health_list(api_version)



### Example
```python
from __future__ import print_function
import time
import hep_rest_api
from hep_rest_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hep_rest_api.RestApi()
api_version = 'api_version_example' # str | 

try:
    api_instance.rest_health_list(api_version)
except ApiException as e:
    print("Exception when calling RestApi->rest_health_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_newchain_coin_gravity_account_read**
> AccountResponse rest_newchain_coin_gravity_account_read(api_version, newid, dapp_key, protocol, version, ts, nonce, os, language, dapp_signature_method, dapp_signature)



### Example
```python
from __future__ import print_function
import time
import hep_rest_api
from hep_rest_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hep_rest_api.RestApi()
api_version = 'api_version_example' # str | 
newid = 'newid_example' # str | 
dapp_key = 'dapp_key_example' # str | The decentralized application access key
protocol = 'protocol_example' # str | The protocol name. default is 'HEP'.
version = 'version_example' # str | The protocol version such as '1.0'
ts = 56 # int | The current timestamp
nonce = 'nonce_example' # str | The random string or auto-increment sequence
os = 'os_example' # str | The operating system of client such as ios, android, dweb,etc.
language = 'language_example' # str | The i18n language code such as zh, en, etc.
dapp_signature_method = 'dapp_signature_method_example' # str | The signature method used by dapp.
dapp_signature = 'dapp_signature_example' # str | The signature generated by dapp.

try:
    api_response = api_instance.rest_newchain_coin_gravity_account_read(api_version, newid, dapp_key, protocol, version, ts, nonce, os, language, dapp_signature_method, dapp_signature)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RestApi->rest_newchain_coin_gravity_account_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**|  | 
 **newid** | **str**|  | 
 **dapp_key** | **str**| The decentralized application access key | 
 **protocol** | **str**| The protocol name. default is &#x27;HEP&#x27;. | 
 **version** | **str**| The protocol version such as &#x27;1.0&#x27; | 
 **ts** | **int**| The current timestamp | 
 **nonce** | **str**| The random string or auto-increment sequence | 
 **os** | **str**| The operating system of client such as ios, android, dweb,etc. | 
 **language** | **str**| The i18n language code such as zh, en, etc. | 
 **dapp_signature_method** | **str**| The signature method used by dapp. | 
 **dapp_signature** | **str**| The signature generated by dapp. | 

### Return type

[**AccountResponse**](AccountResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_newchain_coin_gravity_mint_collect_create**
> CollectMintResponse rest_newchain_coin_gravity_mint_collect_create(body, api_version)



### Example
```python
from __future__ import print_function
import time
import hep_rest_api
from hep_rest_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hep_rest_api.RestApi()
body = hep_rest_api.CollectMintRequest() # CollectMintRequest | 
api_version = 'api_version_example' # str | 

try:
    api_response = api_instance.rest_newchain_coin_gravity_mint_collect_create(body, api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RestApi->rest_newchain_coin_gravity_mint_collect_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CollectMintRequest**](CollectMintRequest.md)|  | 
 **api_version** | **str**|  | 

### Return type

[**CollectMintResponse**](CollectMintResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_newchain_coin_gravity_mint_condition_read**
> MintConditionResponse rest_newchain_coin_gravity_mint_condition_read(api_version, newid, dapp_key, protocol, version, ts, nonce, os, language, dapp_signature_method, dapp_signature)



### Example
```python
from __future__ import print_function
import time
import hep_rest_api
from hep_rest_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hep_rest_api.RestApi()
api_version = 'api_version_example' # str | 
newid = 'newid_example' # str | 
dapp_key = 'dapp_key_example' # str | The decentralized application access key
protocol = 'protocol_example' # str | The protocol name. default is 'HEP'.
version = 'version_example' # str | The protocol version such as '1.0'
ts = 56 # int | The current timestamp
nonce = 'nonce_example' # str | The random string or auto-increment sequence
os = 'os_example' # str | The operating system of client such as ios, android, dweb,etc.
language = 'language_example' # str | The i18n language code such as zh, en, etc.
dapp_signature_method = 'dapp_signature_method_example' # str | The signature method used by dapp.
dapp_signature = 'dapp_signature_example' # str | The signature generated by dapp.

try:
    api_response = api_instance.rest_newchain_coin_gravity_mint_condition_read(api_version, newid, dapp_key, protocol, version, ts, nonce, os, language, dapp_signature_method, dapp_signature)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RestApi->rest_newchain_coin_gravity_mint_condition_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**|  | 
 **newid** | **str**|  | 
 **dapp_key** | **str**| The decentralized application access key | 
 **protocol** | **str**| The protocol name. default is &#x27;HEP&#x27;. | 
 **version** | **str**| The protocol version such as &#x27;1.0&#x27; | 
 **ts** | **int**| The current timestamp | 
 **nonce** | **str**| The random string or auto-increment sequence | 
 **os** | **str**| The operating system of client such as ios, android, dweb,etc. | 
 **language** | **str**| The i18n language code such as zh, en, etc. | 
 **dapp_signature_method** | **str**| The signature method used by dapp. | 
 **dapp_signature** | **str**| The signature generated by dapp. | 

### Return type

[**MintConditionResponse**](MintConditionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_newchain_coin_gravity_mint_data_current_read**
> CurrentDataResponse rest_newchain_coin_gravity_mint_data_current_read(api_version, newid, dapp_key, protocol, version, ts, nonce, os, language, dapp_signature_method, dapp_signature)



### Example
```python
from __future__ import print_function
import time
import hep_rest_api
from hep_rest_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hep_rest_api.RestApi()
api_version = 'api_version_example' # str | 
newid = 'newid_example' # str | 
dapp_key = 'dapp_key_example' # str | The decentralized application access key
protocol = 'protocol_example' # str | The protocol name. default is 'HEP'.
version = 'version_example' # str | The protocol version such as '1.0'
ts = 56 # int | The current timestamp
nonce = 'nonce_example' # str | The random string or auto-increment sequence
os = 'os_example' # str | The operating system of client such as ios, android, dweb,etc.
language = 'language_example' # str | The i18n language code such as zh, en, etc.
dapp_signature_method = 'dapp_signature_method_example' # str | The signature method used by dapp.
dapp_signature = 'dapp_signature_example' # str | The signature generated by dapp.

try:
    api_response = api_instance.rest_newchain_coin_gravity_mint_data_current_read(api_version, newid, dapp_key, protocol, version, ts, nonce, os, language, dapp_signature_method, dapp_signature)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RestApi->rest_newchain_coin_gravity_mint_data_current_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**|  | 
 **newid** | **str**|  | 
 **dapp_key** | **str**| The decentralized application access key | 
 **protocol** | **str**| The protocol name. default is &#x27;HEP&#x27;. | 
 **version** | **str**| The protocol version such as &#x27;1.0&#x27; | 
 **ts** | **int**| The current timestamp | 
 **nonce** | **str**| The random string or auto-increment sequence | 
 **os** | **str**| The operating system of client such as ios, android, dweb,etc. | 
 **language** | **str**| The i18n language code such as zh, en, etc. | 
 **dapp_signature_method** | **str**| The signature method used by dapp. | 
 **dapp_signature** | **str**| The signature generated by dapp. | 

### Return type

[**CurrentDataResponse**](CurrentDataResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_newchain_coin_gravity_mint_data_history_create**
> HistoryDataResponse rest_newchain_coin_gravity_mint_data_history_create(body, api_version)



### Example
```python
from __future__ import print_function
import time
import hep_rest_api
from hep_rest_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hep_rest_api.RestApi()
body = hep_rest_api.HistoryDataRequest() # HistoryDataRequest | 
api_version = 'api_version_example' # str | 

try:
    api_response = api_instance.rest_newchain_coin_gravity_mint_data_history_create(body, api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RestApi->rest_newchain_coin_gravity_mint_data_history_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**HistoryDataRequest**](HistoryDataRequest.md)|  | 
 **api_version** | **str**|  | 

### Return type

[**HistoryDataResponse**](HistoryDataResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_newchain_coin_gravity_mint_submit_create**
> SubmitMintResponse rest_newchain_coin_gravity_mint_submit_create(body, api_version)



### Example
```python
from __future__ import print_function
import time
import hep_rest_api
from hep_rest_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hep_rest_api.RestApi()
body = hep_rest_api.SubmitMintRequest() # SubmitMintRequest | 
api_version = 'api_version_example' # str | 

try:
    api_response = api_instance.rest_newchain_coin_gravity_mint_submit_create(body, api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RestApi->rest_newchain_coin_gravity_mint_submit_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SubmitMintRequest**](SubmitMintRequest.md)|  | 
 **api_version** | **str**|  | 

### Return type

[**SubmitMintResponse**](SubmitMintResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_newchain_coin_gravity_subscription_condition_read**
> SubscribeConditionResponse rest_newchain_coin_gravity_subscription_condition_read(api_version, newid, dapp_key, protocol, version, ts, nonce, os, language, dapp_signature_method, dapp_signature)



### Example
```python
from __future__ import print_function
import time
import hep_rest_api
from hep_rest_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hep_rest_api.RestApi()
api_version = 'api_version_example' # str | 
newid = 'newid_example' # str | 
dapp_key = 'dapp_key_example' # str | The decentralized application access key
protocol = 'protocol_example' # str | The protocol name. default is 'HEP'.
version = 'version_example' # str | The protocol version such as '1.0'
ts = 56 # int | The current timestamp
nonce = 'nonce_example' # str | The random string or auto-increment sequence
os = 'os_example' # str | The operating system of client such as ios, android, dweb,etc.
language = 'language_example' # str | The i18n language code such as zh, en, etc.
dapp_signature_method = 'dapp_signature_method_example' # str | The signature method used by dapp.
dapp_signature = 'dapp_signature_example' # str | The signature generated by dapp.

try:
    api_response = api_instance.rest_newchain_coin_gravity_subscription_condition_read(api_version, newid, dapp_key, protocol, version, ts, nonce, os, language, dapp_signature_method, dapp_signature)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RestApi->rest_newchain_coin_gravity_subscription_condition_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**|  | 
 **newid** | **str**|  | 
 **dapp_key** | **str**| The decentralized application access key | 
 **protocol** | **str**| The protocol name. default is &#x27;HEP&#x27;. | 
 **version** | **str**| The protocol version such as &#x27;1.0&#x27; | 
 **ts** | **int**| The current timestamp | 
 **nonce** | **str**| The random string or auto-increment sequence | 
 **os** | **str**| The operating system of client such as ios, android, dweb,etc. | 
 **language** | **str**| The i18n language code such as zh, en, etc. | 
 **dapp_signature_method** | **str**| The signature method used by dapp. | 
 **dapp_signature** | **str**| The signature generated by dapp. | 

### Return type

[**SubscribeConditionResponse**](SubscribeConditionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_newchain_coin_gravity_subscription_submit_create**
> SubmitSubscribeResponse rest_newchain_coin_gravity_subscription_submit_create(body, api_version)



### Example
```python
from __future__ import print_function
import time
import hep_rest_api
from hep_rest_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hep_rest_api.RestApi()
body = hep_rest_api.SubmitSubscribeRequest() # SubmitSubscribeRequest | 
api_version = 'api_version_example' # str | 

try:
    api_response = api_instance.rest_newchain_coin_gravity_subscription_submit_create(body, api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RestApi->rest_newchain_coin_gravity_subscription_submit_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SubmitSubscribeRequest**](SubmitSubscribeRequest.md)|  | 
 **api_version** | **str**|  | 

### Return type

[**SubmitSubscribeResponse**](SubmitSubscribeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_newchain_tx_read**
> NewchainTransactionResponse rest_newchain_tx_read(api_version, txid, dapp_key, protocol, version, ts, nonce, os, language, dapp_signature_method, dapp_signature)



Retrieve the transaction information by given txid

### Example
```python
from __future__ import print_function
import time
import hep_rest_api
from hep_rest_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hep_rest_api.RestApi()
api_version = 'api_version_example' # str | 
txid = 'txid_example' # str | 
dapp_key = 'dapp_key_example' # str | The decentralized application access key
protocol = 'protocol_example' # str | The protocol name. default is 'HEP'.
version = 'version_example' # str | The protocol version such as '1.0'
ts = 56 # int | The current timestamp
nonce = 'nonce_example' # str | The random string or auto-increment sequence
os = 'os_example' # str | The operating system of client such as ios, android, dweb,etc.
language = 'language_example' # str | The i18n language code such as zh, en, etc.
dapp_signature_method = 'dapp_signature_method_example' # str | The signature method used by dapp.
dapp_signature = 'dapp_signature_example' # str | The signature generated by dapp.

try:
    api_response = api_instance.rest_newchain_tx_read(api_version, txid, dapp_key, protocol, version, ts, nonce, os, language, dapp_signature_method, dapp_signature)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RestApi->rest_newchain_tx_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**|  | 
 **txid** | **str**|  | 
 **dapp_key** | **str**| The decentralized application access key | 
 **protocol** | **str**| The protocol name. default is &#x27;HEP&#x27;. | 
 **version** | **str**| The protocol version such as &#x27;1.0&#x27; | 
 **ts** | **int**| The current timestamp | 
 **nonce** | **str**| The random string or auto-increment sequence | 
 **os** | **str**| The operating system of client such as ios, android, dweb,etc. | 
 **language** | **str**| The i18n language code such as zh, en, etc. | 
 **dapp_signature_method** | **str**| The signature method used by dapp. | 
 **dapp_signature** | **str**| The signature generated by dapp. | 

### Return type

[**NewchainTransactionResponse**](NewchainTransactionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_newforce_node_round_read**
> NewforceOfPartnerAndVoterResponse rest_newforce_node_round_read(api_version, node_wallet_address, dapp_key, protocol, version, ts, nonce, os, language, dapp_signature_method, dapp_signature, page_id=page_id, page_size=page_size, direction=direction)



Retrieve the daily newforce statistics

### Example
```python
from __future__ import print_function
import time
import hep_rest_api
from hep_rest_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hep_rest_api.RestApi()
api_version = 'api_version_example' # str | 
node_wallet_address = 'node_wallet_address_example' # str | 
dapp_key = 'dapp_key_example' # str | The decentralized application access key
protocol = 'protocol_example' # str | The protocol name. default is 'HEP'.
version = 'version_example' # str | The protocol version such as '1.0'
ts = 56 # int | The current timestamp
nonce = 'nonce_example' # str | The random string or auto-increment sequence
os = 'os_example' # str | The operating system of client such as ios, android, dweb,etc.
language = 'language_example' # str | The i18n language code such as zh, en, etc.
dapp_signature_method = 'dapp_signature_method_example' # str | The signature method used by dapp.
dapp_signature = 'dapp_signature_example' # str | The signature generated by dapp.
page_id = 56 # int |  (optional)
page_size = 56 # int |  (optional)
direction = 56 # int |  (optional)

try:
    api_response = api_instance.rest_newforce_node_round_read(api_version, node_wallet_address, dapp_key, protocol, version, ts, nonce, os, language, dapp_signature_method, dapp_signature, page_id=page_id, page_size=page_size, direction=direction)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RestApi->rest_newforce_node_round_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**|  | 
 **node_wallet_address** | **str**|  | 
 **dapp_key** | **str**| The decentralized application access key | 
 **protocol** | **str**| The protocol name. default is &#x27;HEP&#x27;. | 
 **version** | **str**| The protocol version such as &#x27;1.0&#x27; | 
 **ts** | **int**| The current timestamp | 
 **nonce** | **str**| The random string or auto-increment sequence | 
 **os** | **str**| The operating system of client such as ios, android, dweb,etc. | 
 **language** | **str**| The i18n language code such as zh, en, etc. | 
 **dapp_signature_method** | **str**| The signature method used by dapp. | 
 **dapp_signature** | **str**| The signature generated by dapp. | 
 **page_id** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 
 **direction** | **int**|  | [optional] 

### Return type

[**NewforceOfPartnerAndVoterResponse**](NewforceOfPartnerAndVoterResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_newforce_read**
> NewforceDailyStatsResponse rest_newforce_read(api_version, _date, dapp_key, protocol, version, ts, nonce, os, language, dapp_signature_method, dapp_signature)



Retrieve the daily newforce statistics

### Example
```python
from __future__ import print_function
import time
import hep_rest_api
from hep_rest_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hep_rest_api.RestApi()
api_version = 'api_version_example' # str | 
_date = '_date_example' # str | 
dapp_key = 'dapp_key_example' # str | The decentralized application access key
protocol = 'protocol_example' # str | The protocol name. default is 'HEP'.
version = 'version_example' # str | The protocol version such as '1.0'
ts = 56 # int | The current timestamp
nonce = 'nonce_example' # str | The random string or auto-increment sequence
os = 'os_example' # str | The operating system of client such as ios, android, dweb,etc.
language = 'language_example' # str | The i18n language code such as zh, en, etc.
dapp_signature_method = 'dapp_signature_method_example' # str | The signature method used by dapp.
dapp_signature = 'dapp_signature_example' # str | The signature generated by dapp.

try:
    api_response = api_instance.rest_newforce_read(api_version, _date, dapp_key, protocol, version, ts, nonce, os, language, dapp_signature_method, dapp_signature)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RestApi->rest_newforce_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**|  | 
 **_date** | **str**|  | 
 **dapp_key** | **str**| The decentralized application access key | 
 **protocol** | **str**| The protocol name. default is &#x27;HEP&#x27;. | 
 **version** | **str**| The protocol version such as &#x27;1.0&#x27; | 
 **ts** | **int**| The current timestamp | 
 **nonce** | **str**| The random string or auto-increment sequence | 
 **os** | **str**| The operating system of client such as ios, android, dweb,etc. | 
 **language** | **str**| The i18n language code such as zh, en, etc. | 
 **dapp_signature_method** | **str**| The signature method used by dapp. | 
 **dapp_signature** | **str**| The signature generated by dapp. | 

### Return type

[**NewforceDailyStatsResponse**](NewforceDailyStatsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_newids_newforce_reward_list**
> NewforceRewardAmountResponse rest_newids_newforce_reward_list(api_version, newid, dapp_key, protocol, version, ts, nonce, os, language, dapp_signature_method, dapp_signature)



Get the reward tokens amount by newid

### Example
```python
from __future__ import print_function
import time
import hep_rest_api
from hep_rest_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hep_rest_api.RestApi()
api_version = 'api_version_example' # str | 
newid = 'newid_example' # str | 
dapp_key = 'dapp_key_example' # str | The decentralized application access key
protocol = 'protocol_example' # str | The protocol name. default is 'HEP'.
version = 'version_example' # str | The protocol version such as '1.0'
ts = 56 # int | The current timestamp
nonce = 'nonce_example' # str | The random string or auto-increment sequence
os = 'os_example' # str | The operating system of client such as ios, android, dweb,etc.
language = 'language_example' # str | The i18n language code such as zh, en, etc.
dapp_signature_method = 'dapp_signature_method_example' # str | The signature method used by dapp.
dapp_signature = 'dapp_signature_example' # str | The signature generated by dapp.

try:
    api_response = api_instance.rest_newids_newforce_reward_list(api_version, newid, dapp_key, protocol, version, ts, nonce, os, language, dapp_signature_method, dapp_signature)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RestApi->rest_newids_newforce_reward_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**|  | 
 **newid** | **str**|  | 
 **dapp_key** | **str**| The decentralized application access key | 
 **protocol** | **str**| The protocol name. default is &#x27;HEP&#x27;. | 
 **version** | **str**| The protocol version such as &#x27;1.0&#x27; | 
 **ts** | **int**| The current timestamp | 
 **nonce** | **str**| The random string or auto-increment sequence | 
 **os** | **str**| The operating system of client such as ios, android, dweb,etc. | 
 **language** | **str**| The i18n language code such as zh, en, etc. | 
 **dapp_signature_method** | **str**| The signature method used by dapp. | 
 **dapp_signature** | **str**| The signature generated by dapp. | 

### Return type

[**NewforceRewardAmountResponse**](NewforceRewardAmountResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_newids_read**
> NewidResponse rest_newids_read(api_version, newid, dapp_key, protocol, version, ts, nonce, os, language, dapp_signature_method, dapp_signature)



Retrieve the information by given NewID

### Example
```python
from __future__ import print_function
import time
import hep_rest_api
from hep_rest_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hep_rest_api.RestApi()
api_version = 'api_version_example' # str | 
newid = 'newid_example' # str | 
dapp_key = 'dapp_key_example' # str | The decentralized application access key
protocol = 'protocol_example' # str | The protocol name. default is 'HEP'.
version = 'version_example' # str | The protocol version such as '1.0'
ts = 56 # int | The current timestamp
nonce = 'nonce_example' # str | The random string or auto-increment sequence
os = 'os_example' # str | The operating system of client such as ios, android, dweb,etc.
language = 'language_example' # str | The i18n language code such as zh, en, etc.
dapp_signature_method = 'dapp_signature_method_example' # str | The signature method used by dapp.
dapp_signature = 'dapp_signature_example' # str | The signature generated by dapp.

try:
    api_response = api_instance.rest_newids_read(api_version, newid, dapp_key, protocol, version, ts, nonce, os, language, dapp_signature_method, dapp_signature)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RestApi->rest_newids_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**|  | 
 **newid** | **str**|  | 
 **dapp_key** | **str**| The decentralized application access key | 
 **protocol** | **str**| The protocol name. default is &#x27;HEP&#x27;. | 
 **version** | **str**| The protocol version such as &#x27;1.0&#x27; | 
 **ts** | **int**| The current timestamp | 
 **nonce** | **str**| The random string or auto-increment sequence | 
 **os** | **str**| The operating system of client such as ios, android, dweb,etc. | 
 **language** | **str**| The i18n language code such as zh, en, etc. | 
 **dapp_signature_method** | **str**| The signature method used by dapp. | 
 **dapp_signature** | **str**| The signature generated by dapp. | 

### Return type

[**NewidResponse**](NewidResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_newnet_caches_auth_create**
> CreateAuthCacheResponse rest_newnet_caches_auth_create(body, api_version)



Caches the authentication request

### Example
```python
from __future__ import print_function
import time
import hep_rest_api
from hep_rest_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hep_rest_api.RestApi()
body = hep_rest_api.AuthCacheRequest() # AuthCacheRequest | 
api_version = 'api_version_example' # str | 

try:
    api_response = api_instance.rest_newnet_caches_auth_create(body, api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RestApi->rest_newnet_caches_auth_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AuthCacheRequest**](AuthCacheRequest.md)|  | 
 **api_version** | **str**|  | 

### Return type

[**CreateAuthCacheResponse**](CreateAuthCacheResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_newnet_caches_auth_read**
> AuthCacheResponse rest_newnet_caches_auth_read(api_version, auth_hash, dapp_key, protocol, version, ts, nonce, os, language, dapp_signature_method, dapp_signature)



Get the authentication information by given request hash.

### Example
```python
from __future__ import print_function
import time
import hep_rest_api
from hep_rest_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hep_rest_api.RestApi()
api_version = 'api_version_example' # str | 
auth_hash = 'auth_hash_example' # str | 
dapp_key = 'dapp_key_example' # str | The decentralized application access key
protocol = 'protocol_example' # str | The protocol name. default is 'HEP'.
version = 'version_example' # str | The protocol version such as '1.0'
ts = 56 # int | The current timestamp
nonce = 'nonce_example' # str | The random string or auto-increment sequence
os = 'os_example' # str | The operating system of client such as ios, android, dweb,etc.
language = 'language_example' # str | The i18n language code such as zh, en, etc.
dapp_signature_method = 'dapp_signature_method_example' # str | The signature method used by dapp.
dapp_signature = 'dapp_signature_example' # str | The signature generated by dapp.

try:
    api_response = api_instance.rest_newnet_caches_auth_read(api_version, auth_hash, dapp_key, protocol, version, ts, nonce, os, language, dapp_signature_method, dapp_signature)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RestApi->rest_newnet_caches_auth_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**|  | 
 **auth_hash** | **str**|  | 
 **dapp_key** | **str**| The decentralized application access key | 
 **protocol** | **str**| The protocol name. default is &#x27;HEP&#x27;. | 
 **version** | **str**| The protocol version such as &#x27;1.0&#x27; | 
 **ts** | **int**| The current timestamp | 
 **nonce** | **str**| The random string or auto-increment sequence | 
 **os** | **str**| The operating system of client such as ios, android, dweb,etc. | 
 **language** | **str**| The i18n language code such as zh, en, etc. | 
 **dapp_signature_method** | **str**| The signature method used by dapp. | 
 **dapp_signature** | **str**| The signature generated by dapp. | 

### Return type

[**AuthCacheResponse**](AuthCacheResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_newnet_caches_pay_create**
> CreatePayCacheResponse rest_newnet_caches_pay_create(body, api_version)



Cache the pay request

### Example
```python
from __future__ import print_function
import time
import hep_rest_api
from hep_rest_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hep_rest_api.RestApi()
body = hep_rest_api.PayCacheRequest() # PayCacheRequest | 
api_version = 'api_version_example' # str | 

try:
    api_response = api_instance.rest_newnet_caches_pay_create(body, api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RestApi->rest_newnet_caches_pay_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PayCacheRequest**](PayCacheRequest.md)|  | 
 **api_version** | **str**|  | 

### Return type

[**CreatePayCacheResponse**](CreatePayCacheResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_newnet_caches_pay_read**
> PayCacheResponse rest_newnet_caches_pay_read(api_version, pay_hash, dapp_key, protocol, version, ts, nonce, os, language, dapp_signature_method, dapp_signature)



Retrieve the pay information by given pay hash.

### Example
```python
from __future__ import print_function
import time
import hep_rest_api
from hep_rest_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hep_rest_api.RestApi()
api_version = 'api_version_example' # str | 
pay_hash = 'pay_hash_example' # str | 
dapp_key = 'dapp_key_example' # str | The decentralized application access key
protocol = 'protocol_example' # str | The protocol name. default is 'HEP'.
version = 'version_example' # str | The protocol version such as '1.0'
ts = 56 # int | The current timestamp
nonce = 'nonce_example' # str | The random string or auto-increment sequence
os = 'os_example' # str | The operating system of client such as ios, android, dweb,etc.
language = 'language_example' # str | The i18n language code such as zh, en, etc.
dapp_signature_method = 'dapp_signature_method_example' # str | The signature method used by dapp.
dapp_signature = 'dapp_signature_example' # str | The signature generated by dapp.

try:
    api_response = api_instance.rest_newnet_caches_pay_read(api_version, pay_hash, dapp_key, protocol, version, ts, nonce, os, language, dapp_signature_method, dapp_signature)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RestApi->rest_newnet_caches_pay_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**|  | 
 **pay_hash** | **str**|  | 
 **dapp_key** | **str**| The decentralized application access key | 
 **protocol** | **str**| The protocol name. default is &#x27;HEP&#x27;. | 
 **version** | **str**| The protocol version such as &#x27;1.0&#x27; | 
 **ts** | **int**| The current timestamp | 
 **nonce** | **str**| The random string or auto-increment sequence | 
 **os** | **str**| The operating system of client such as ios, android, dweb,etc. | 
 **language** | **str**| The i18n language code such as zh, en, etc. | 
 **dapp_signature_method** | **str**| The signature method used by dapp. | 
 **dapp_signature** | **str**| The signature generated by dapp. | 

### Return type

[**PayCacheResponse**](PayCacheResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_oracles_read**
> RetrieveOracleResponse rest_oracles_read(api_version, oracle_id, dapp_key, protocol, version, ts, nonce, os, language, dapp_signature_method, dapp_signature)



Get the oracle information by given id.

### Example
```python
from __future__ import print_function
import time
import hep_rest_api
from hep_rest_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hep_rest_api.RestApi()
api_version = 'api_version_example' # str | 
oracle_id = 'oracle_id_example' # str | 
dapp_key = 'dapp_key_example' # str | The decentralized application access key
protocol = 'protocol_example' # str | The protocol name. default is 'HEP'.
version = 'version_example' # str | The protocol version such as '1.0'
ts = 56 # int | The current timestamp
nonce = 'nonce_example' # str | The random string or auto-increment sequence
os = 'os_example' # str | The operating system of client such as ios, android, dweb,etc.
language = 'language_example' # str | The i18n language code such as zh, en, etc.
dapp_signature_method = 'dapp_signature_method_example' # str | The signature method used by dapp.
dapp_signature = 'dapp_signature_example' # str | The signature generated by dapp.

try:
    api_response = api_instance.rest_oracles_read(api_version, oracle_id, dapp_key, protocol, version, ts, nonce, os, language, dapp_signature_method, dapp_signature)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RestApi->rest_oracles_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**|  | 
 **oracle_id** | **str**|  | 
 **dapp_key** | **str**| The decentralized application access key | 
 **protocol** | **str**| The protocol name. default is &#x27;HEP&#x27;. | 
 **version** | **str**| The protocol version such as &#x27;1.0&#x27; | 
 **ts** | **int**| The current timestamp | 
 **nonce** | **str**| The random string or auto-increment sequence | 
 **os** | **str**| The operating system of client such as ios, android, dweb,etc. | 
 **language** | **str**| The i18n language code such as zh, en, etc. | 
 **dapp_signature_method** | **str**| The signature method used by dapp. | 
 **dapp_signature** | **str**| The signature generated by dapp. | 

### Return type

[**RetrieveOracleResponse**](RetrieveOracleResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_proofs_create**
> CreateProofResponse rest_proofs_create(body, api_version)



### Example
```python
from __future__ import print_function
import time
import hep_rest_api
from hep_rest_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hep_rest_api.RestApi()
body = hep_rest_api.CreateProofRequest() # CreateProofRequest | 
api_version = 'api_version_example' # str | 

try:
    api_response = api_instance.rest_proofs_create(body, api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RestApi->rest_proofs_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateProofRequest**](CreateProofRequest.md)|  | 
 **api_version** | **str**|  | 

### Return type

[**CreateProofResponse**](CreateProofResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_proofs_delete**
> CancelProofResponse rest_proofs_delete(body, api_version, proof_hash)



### Example
```python
from __future__ import print_function
import time
import hep_rest_api
from hep_rest_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hep_rest_api.RestApi()
body = hep_rest_api.CancelProofRequest() # CancelProofRequest | 
api_version = 'api_version_example' # str | 
proof_hash = 'proof_hash_example' # str | 

try:
    api_response = api_instance.rest_proofs_delete(body, api_version, proof_hash)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RestApi->rest_proofs_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CancelProofRequest**](CancelProofRequest.md)|  | 
 **api_version** | **str**|  | 
 **proof_hash** | **str**|  | 

### Return type

[**CancelProofResponse**](CancelProofResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_proofs_read**
> ProofResponse rest_proofs_read(api_version, proof_hash, dapp_key, protocol, version, ts, nonce, os, language, dapp_signature_method, dapp_signature)



Get the proof by given proof hash.

### Example
```python
from __future__ import print_function
import time
import hep_rest_api
from hep_rest_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hep_rest_api.RestApi()
api_version = 'api_version_example' # str | 
proof_hash = 'proof_hash_example' # str | 
dapp_key = 'dapp_key_example' # str | The decentralized application access key
protocol = 'protocol_example' # str | The protocol name. default is 'HEP'.
version = 'version_example' # str | The protocol version such as '1.0'
ts = 56 # int | The current timestamp
nonce = 'nonce_example' # str | The random string or auto-increment sequence
os = 'os_example' # str | The operating system of client such as ios, android, dweb,etc.
language = 'language_example' # str | The i18n language code such as zh, en, etc.
dapp_signature_method = 'dapp_signature_method_example' # str | The signature method used by dapp.
dapp_signature = 'dapp_signature_example' # str | The signature generated by dapp.

try:
    api_response = api_instance.rest_proofs_read(api_version, proof_hash, dapp_key, protocol, version, ts, nonce, os, language, dapp_signature_method, dapp_signature)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RestApi->rest_proofs_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**|  | 
 **proof_hash** | **str**|  | 
 **dapp_key** | **str**| The decentralized application access key | 
 **protocol** | **str**| The protocol name. default is &#x27;HEP&#x27;. | 
 **version** | **str**| The protocol version such as &#x27;1.0&#x27; | 
 **ts** | **int**| The current timestamp | 
 **nonce** | **str**| The random string or auto-increment sequence | 
 **os** | **str**| The operating system of client such as ios, android, dweb,etc. | 
 **language** | **str**| The i18n language code such as zh, en, etc. | 
 **dapp_signature_method** | **str**| The signature method used by dapp. | 
 **dapp_signature** | **str**| The signature generated by dapp. | 

### Return type

[**ProofResponse**](ProofResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_proofs_receipts_create**
> RetrieveProofReceiptsResponse rest_proofs_receipts_create(body, api_version)



### Example
```python
from __future__ import print_function
import time
import hep_rest_api
from hep_rest_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hep_rest_api.RestApi()
body = hep_rest_api.RetrieveProofReceiptsRequest() # RetrieveProofReceiptsRequest | 
api_version = 'api_version_example' # str | 

try:
    api_response = api_instance.rest_proofs_receipts_create(body, api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RestApi->rest_proofs_receipts_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RetrieveProofReceiptsRequest**](RetrieveProofReceiptsRequest.md)|  | 
 **api_version** | **str**|  | 

### Return type

[**RetrieveProofReceiptsResponse**](RetrieveProofReceiptsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_proofs_rewards_create**
> RetrieveProofRewardsResponse rest_proofs_rewards_create(body, api_version)



### Example
```python
from __future__ import print_function
import time
import hep_rest_api
from hep_rest_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hep_rest_api.RestApi()
body = hep_rest_api.RetrieveProofRewardsRequest() # RetrieveProofRewardsRequest | 
api_version = 'api_version_example' # str | 

try:
    api_response = api_instance.rest_proofs_rewards_create(body, api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RestApi->rest_proofs_rewards_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RetrieveProofRewardsRequest**](RetrieveProofRewardsRequest.md)|  | 
 **api_version** | **str**|  | 

### Return type

[**RetrieveProofRewardsResponse**](RetrieveProofRewardsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

