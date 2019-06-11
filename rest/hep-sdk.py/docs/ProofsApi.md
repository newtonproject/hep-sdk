# swagger_client.ProofsApi

All URIs are relative to *http://127.0.0.1:8000/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**proofs_create**](ProofsApi.md#proofs_create) | **POST** /proofs/ | 
[**proofs_delete**](ProofsApi.md#proofs_delete) | **DELETE** /proofs/{proof_hash}/ | 
[**proofs_update**](ProofsApi.md#proofs_update) | **PUT** /proofs/{proof_hash}/ | 

# **proofs_create**
> CreateProofResponse proofs_create(body)



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
api_instance = swagger_client.ProofsApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreateProofRequest() # CreateProofRequest | 

try:
    api_response = api_instance.proofs_create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProofsApi->proofs_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateProofRequest**](CreateProofRequest.md)|  | 

### Return type

[**CreateProofResponse**](CreateProofResponse.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **proofs_delete**
> CancelProofResponse proofs_delete(body, proof_hash)



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
api_instance = swagger_client.ProofsApi(swagger_client.ApiClient(configuration))
body = swagger_client.CancelProofRequest() # CancelProofRequest | 
proof_hash = 'proof_hash_example' # str | 

try:
    api_response = api_instance.proofs_delete(body, proof_hash)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProofsApi->proofs_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CancelProofRequest**](CancelProofRequest.md)|  | 
 **proof_hash** | **str**|  | 

### Return type

[**CancelProofResponse**](CancelProofResponse.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **proofs_update**
> UpdateProofResponse proofs_update(body, proof_hash)



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
api_instance = swagger_client.ProofsApi(swagger_client.ApiClient(configuration))
body = swagger_client.UpdateProofRequest() # UpdateProofRequest | 
proof_hash = 'proof_hash_example' # str | 

try:
    api_response = api_instance.proofs_update(body, proof_hash)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProofsApi->proofs_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateProofRequest**](UpdateProofRequest.md)|  | 
 **proof_hash** | **str**|  | 

### Return type

[**UpdateProofResponse**](UpdateProofResponse.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

