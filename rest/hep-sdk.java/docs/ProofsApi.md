# ProofsApi

All URIs are relative to *http://127.0.0.1:8000/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**proofsCreate**](ProofsApi.md#proofsCreate) | **POST** /proofs/ | 
[**proofsDelete**](ProofsApi.md#proofsDelete) | **DELETE** /proofs/{proof_hash}/ | 
[**proofsUpdate**](ProofsApi.md#proofsUpdate) | **PUT** /proofs/{proof_hash}/ | 

<a name="proofsCreate"></a>
# **proofsCreate**
> CreateProofResponse proofsCreate(body)



### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.ProofsApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();
// Configure HTTP basic authorization: Basic
HttpBasicAuth Basic = (HttpBasicAuth) defaultClient.getAuthentication("Basic");
Basic.setUsername("YOUR USERNAME");
Basic.setPassword("YOUR PASSWORD");

ProofsApi apiInstance = new ProofsApi();
CreateProofRequest body = new CreateProofRequest(); // CreateProofRequest | 
try {
    CreateProofResponse result = apiInstance.proofsCreate(body);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling ProofsApi#proofsCreate");
    e.printStackTrace();
}
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

<a name="proofsDelete"></a>
# **proofsDelete**
> CancelProofResponse proofsDelete(body, proofHash)



### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.ProofsApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();
// Configure HTTP basic authorization: Basic
HttpBasicAuth Basic = (HttpBasicAuth) defaultClient.getAuthentication("Basic");
Basic.setUsername("YOUR USERNAME");
Basic.setPassword("YOUR PASSWORD");

ProofsApi apiInstance = new ProofsApi();
CancelProofRequest body = new CancelProofRequest(); // CancelProofRequest | 
String proofHash = "proofHash_example"; // String | 
try {
    CancelProofResponse result = apiInstance.proofsDelete(body, proofHash);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling ProofsApi#proofsDelete");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CancelProofRequest**](CancelProofRequest.md)|  |
 **proofHash** | **String**|  |

### Return type

[**CancelProofResponse**](CancelProofResponse.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="proofsUpdate"></a>
# **proofsUpdate**
> UpdateProofResponse proofsUpdate(body, proofHash)



### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.ProofsApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();
// Configure HTTP basic authorization: Basic
HttpBasicAuth Basic = (HttpBasicAuth) defaultClient.getAuthentication("Basic");
Basic.setUsername("YOUR USERNAME");
Basic.setPassword("YOUR PASSWORD");

ProofsApi apiInstance = new ProofsApi();
UpdateProofRequest body = new UpdateProofRequest(); // UpdateProofRequest | 
String proofHash = "proofHash_example"; // String | 
try {
    UpdateProofResponse result = apiInstance.proofsUpdate(body, proofHash);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling ProofsApi#proofsUpdate");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateProofRequest**](UpdateProofRequest.md)|  |
 **proofHash** | **String**|  |

### Return type

[**UpdateProofResponse**](UpdateProofResponse.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

