# RestApi

All URIs are relative to *http://127.0.0.1:8000/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**restDappsRead**](RestApi.md#restDappsRead) | **GET** /rest/v{version}/dapps/{dapp_id}/ | 
[**restNewidsRead**](RestApi.md#restNewidsRead) | **GET** /rest/v{version}/newids/{newid}/ | 
[**restNewnetCachesAuthCreate**](RestApi.md#restNewnetCachesAuthCreate) | **POST** /rest/v{version}/newnet/caches/auth/ | 
[**restNewnetCachesAuthRead**](RestApi.md#restNewnetCachesAuthRead) | **GET** /rest/v{version}/newnet/caches/auth/{auth_hash}/ | 
[**restNewnetCachesPayCreate**](RestApi.md#restNewnetCachesPayCreate) | **POST** /rest/v{version}/newnet/caches/pay/ | 
[**restNewnetCachesPayRead**](RestApi.md#restNewnetCachesPayRead) | **GET** /rest/v{version}/newnet/caches/pay/{pay_hash}/ | 
[**restProofsCreate**](RestApi.md#restProofsCreate) | **POST** /rest/v{version}/proofs/ | 
[**restProofsDelete**](RestApi.md#restProofsDelete) | **DELETE** /rest/v{version}/proofs/{proof_hash}/ | 
[**restProofsUpdate**](RestApi.md#restProofsUpdate) | **PUT** /rest/v{version}/proofs/{proof_hash}/ | 

<a name="restDappsRead"></a>
# **restDappsRead**
> Dapp restDappsRead(dappId, version, dappKey, protocol, version2, ts, nonce, os, language, md5)



### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.RestApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();
// Configure HTTP basic authorization: Basic
HttpBasicAuth Basic = (HttpBasicAuth) defaultClient.getAuthentication("Basic");
Basic.setUsername("YOUR USERNAME");
Basic.setPassword("YOUR PASSWORD");

RestApi apiInstance = new RestApi();
String dappId = "dappId_example"; // String | 
String version = "version_example"; // String | 
String dappKey = "dappKey_example"; // String | The decentralized application access key
String protocol = "protocol_example"; // String | The protocol name. default is 'HEP'.
String version2 = "version_example"; // String | The protocol version such as '1.0'
Integer ts = 56; // Integer | The current timestamp
String nonce = "nonce_example"; // String | The random string or auto-increment sequence
String os = "os_example"; // String | The operating system of client such as ios, android, dweb,etc.
String language = "language_example"; // String | The i18n language code such as zh, en, etc.
String md5 = "md5_example"; // String | The HMAC authentication md5 checksum
try {
    Dapp result = apiInstance.restDappsRead(dappId, version, dappKey, protocol, version2, ts, nonce, os, language, md5);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling RestApi#restDappsRead");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dappId** | **String**|  |
 **version** | **String**|  |
 **dappKey** | **String**| The decentralized application access key |
 **protocol** | **String**| The protocol name. default is &#x27;HEP&#x27;. |
 **version2** | **String**| The protocol version such as &#x27;1.0&#x27; |
 **ts** | **Integer**| The current timestamp |
 **nonce** | **String**| The random string or auto-increment sequence |
 **os** | **String**| The operating system of client such as ios, android, dweb,etc. |
 **language** | **String**| The i18n language code such as zh, en, etc. |
 **md5** | **String**| The HMAC authentication md5 checksum |

### Return type

[**Dapp**](Dapp.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="restNewidsRead"></a>
# **restNewidsRead**
> NewidResponse restNewidsRead(newid, version, dappKey, protocol, version2, ts, nonce, os, language, md5)



Retrieve the information by given NewID

### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.RestApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();
// Configure HTTP basic authorization: Basic
HttpBasicAuth Basic = (HttpBasicAuth) defaultClient.getAuthentication("Basic");
Basic.setUsername("YOUR USERNAME");
Basic.setPassword("YOUR PASSWORD");

RestApi apiInstance = new RestApi();
String newid = "newid_example"; // String | 
String version = "version_example"; // String | 
String dappKey = "dappKey_example"; // String | The decentralized application access key
String protocol = "protocol_example"; // String | The protocol name. default is 'HEP'.
String version2 = "version_example"; // String | The protocol version such as '1.0'
Integer ts = 56; // Integer | The current timestamp
String nonce = "nonce_example"; // String | The random string or auto-increment sequence
String os = "os_example"; // String | The operating system of client such as ios, android, dweb,etc.
String language = "language_example"; // String | The i18n language code such as zh, en, etc.
String md5 = "md5_example"; // String | The HMAC authentication md5 checksum
try {
    NewidResponse result = apiInstance.restNewidsRead(newid, version, dappKey, protocol, version2, ts, nonce, os, language, md5);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling RestApi#restNewidsRead");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **newid** | **String**|  |
 **version** | **String**|  |
 **dappKey** | **String**| The decentralized application access key |
 **protocol** | **String**| The protocol name. default is &#x27;HEP&#x27;. |
 **version2** | **String**| The protocol version such as &#x27;1.0&#x27; |
 **ts** | **Integer**| The current timestamp |
 **nonce** | **String**| The random string or auto-increment sequence |
 **os** | **String**| The operating system of client such as ios, android, dweb,etc. |
 **language** | **String**| The i18n language code such as zh, en, etc. |
 **md5** | **String**| The HMAC authentication md5 checksum |

### Return type

[**NewidResponse**](NewidResponse.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="restNewnetCachesAuthCreate"></a>
# **restNewnetCachesAuthCreate**
> CreateAuthCacheResponse restNewnetCachesAuthCreate(body, version)



Caches the authentication request

### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.RestApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();
// Configure HTTP basic authorization: Basic
HttpBasicAuth Basic = (HttpBasicAuth) defaultClient.getAuthentication("Basic");
Basic.setUsername("YOUR USERNAME");
Basic.setPassword("YOUR PASSWORD");

RestApi apiInstance = new RestApi();
AuthCacheRequest body = new AuthCacheRequest(); // AuthCacheRequest | 
String version = "version_example"; // String | 
try {
    CreateAuthCacheResponse result = apiInstance.restNewnetCachesAuthCreate(body, version);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling RestApi#restNewnetCachesAuthCreate");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AuthCacheRequest**](AuthCacheRequest.md)|  |
 **version** | **String**|  |

### Return type

[**CreateAuthCacheResponse**](CreateAuthCacheResponse.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="restNewnetCachesAuthRead"></a>
# **restNewnetCachesAuthRead**
> AuthCacheResponse restNewnetCachesAuthRead(authHash, version, dappKey, protocol, version2, ts, nonce, os, language, md5)



Get the authentication information by given request hash.

### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.RestApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();
// Configure HTTP basic authorization: Basic
HttpBasicAuth Basic = (HttpBasicAuth) defaultClient.getAuthentication("Basic");
Basic.setUsername("YOUR USERNAME");
Basic.setPassword("YOUR PASSWORD");

RestApi apiInstance = new RestApi();
String authHash = "authHash_example"; // String | 
String version = "version_example"; // String | 
String dappKey = "dappKey_example"; // String | The decentralized application access key
String protocol = "protocol_example"; // String | The protocol name. default is 'HEP'.
String version2 = "version_example"; // String | The protocol version such as '1.0'
Integer ts = 56; // Integer | The current timestamp
String nonce = "nonce_example"; // String | The random string or auto-increment sequence
String os = "os_example"; // String | The operating system of client such as ios, android, dweb,etc.
String language = "language_example"; // String | The i18n language code such as zh, en, etc.
String md5 = "md5_example"; // String | The HMAC authentication md5 checksum
try {
    AuthCacheResponse result = apiInstance.restNewnetCachesAuthRead(authHash, version, dappKey, protocol, version2, ts, nonce, os, language, md5);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling RestApi#restNewnetCachesAuthRead");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authHash** | **String**|  |
 **version** | **String**|  |
 **dappKey** | **String**| The decentralized application access key |
 **protocol** | **String**| The protocol name. default is &#x27;HEP&#x27;. |
 **version2** | **String**| The protocol version such as &#x27;1.0&#x27; |
 **ts** | **Integer**| The current timestamp |
 **nonce** | **String**| The random string or auto-increment sequence |
 **os** | **String**| The operating system of client such as ios, android, dweb,etc. |
 **language** | **String**| The i18n language code such as zh, en, etc. |
 **md5** | **String**| The HMAC authentication md5 checksum |

### Return type

[**AuthCacheResponse**](AuthCacheResponse.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="restNewnetCachesPayCreate"></a>
# **restNewnetCachesPayCreate**
> CreatePayCacheResponse restNewnetCachesPayCreate(body, version)



Cache the pay request

### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.RestApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();
// Configure HTTP basic authorization: Basic
HttpBasicAuth Basic = (HttpBasicAuth) defaultClient.getAuthentication("Basic");
Basic.setUsername("YOUR USERNAME");
Basic.setPassword("YOUR PASSWORD");

RestApi apiInstance = new RestApi();
PayCacheRequest body = new PayCacheRequest(); // PayCacheRequest | 
String version = "version_example"; // String | 
try {
    CreatePayCacheResponse result = apiInstance.restNewnetCachesPayCreate(body, version);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling RestApi#restNewnetCachesPayCreate");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PayCacheRequest**](PayCacheRequest.md)|  |
 **version** | **String**|  |

### Return type

[**CreatePayCacheResponse**](CreatePayCacheResponse.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="restNewnetCachesPayRead"></a>
# **restNewnetCachesPayRead**
> PayCacheResponse restNewnetCachesPayRead(payHash, version, dappKey, protocol, version2, ts, nonce, os, language, md5)



Retrieve the pay information by given pay hash.

### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.RestApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();
// Configure HTTP basic authorization: Basic
HttpBasicAuth Basic = (HttpBasicAuth) defaultClient.getAuthentication("Basic");
Basic.setUsername("YOUR USERNAME");
Basic.setPassword("YOUR PASSWORD");

RestApi apiInstance = new RestApi();
String payHash = "payHash_example"; // String | 
String version = "version_example"; // String | 
String dappKey = "dappKey_example"; // String | The decentralized application access key
String protocol = "protocol_example"; // String | The protocol name. default is 'HEP'.
String version2 = "version_example"; // String | The protocol version such as '1.0'
Integer ts = 56; // Integer | The current timestamp
String nonce = "nonce_example"; // String | The random string or auto-increment sequence
String os = "os_example"; // String | The operating system of client such as ios, android, dweb,etc.
String language = "language_example"; // String | The i18n language code such as zh, en, etc.
String md5 = "md5_example"; // String | The HMAC authentication md5 checksum
try {
    PayCacheResponse result = apiInstance.restNewnetCachesPayRead(payHash, version, dappKey, protocol, version2, ts, nonce, os, language, md5);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling RestApi#restNewnetCachesPayRead");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payHash** | **String**|  |
 **version** | **String**|  |
 **dappKey** | **String**| The decentralized application access key |
 **protocol** | **String**| The protocol name. default is &#x27;HEP&#x27;. |
 **version2** | **String**| The protocol version such as &#x27;1.0&#x27; |
 **ts** | **Integer**| The current timestamp |
 **nonce** | **String**| The random string or auto-increment sequence |
 **os** | **String**| The operating system of client such as ios, android, dweb,etc. |
 **language** | **String**| The i18n language code such as zh, en, etc. |
 **md5** | **String**| The HMAC authentication md5 checksum |

### Return type

[**PayCacheResponse**](PayCacheResponse.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="restProofsCreate"></a>
# **restProofsCreate**
> CreateProofResponse restProofsCreate(body, version)



### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.RestApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();
// Configure HTTP basic authorization: Basic
HttpBasicAuth Basic = (HttpBasicAuth) defaultClient.getAuthentication("Basic");
Basic.setUsername("YOUR USERNAME");
Basic.setPassword("YOUR PASSWORD");

RestApi apiInstance = new RestApi();
CreateProofRequest body = new CreateProofRequest(); // CreateProofRequest | 
String version = "version_example"; // String | 
try {
    CreateProofResponse result = apiInstance.restProofsCreate(body, version);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling RestApi#restProofsCreate");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateProofRequest**](CreateProofRequest.md)|  |
 **version** | **String**|  |

### Return type

[**CreateProofResponse**](CreateProofResponse.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="restProofsDelete"></a>
# **restProofsDelete**
> CancelProofResponse restProofsDelete(body, proofHash, version)



### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.RestApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();
// Configure HTTP basic authorization: Basic
HttpBasicAuth Basic = (HttpBasicAuth) defaultClient.getAuthentication("Basic");
Basic.setUsername("YOUR USERNAME");
Basic.setPassword("YOUR PASSWORD");

RestApi apiInstance = new RestApi();
CancelProofRequest body = new CancelProofRequest(); // CancelProofRequest | 
String proofHash = "proofHash_example"; // String | 
String version = "version_example"; // String | 
try {
    CancelProofResponse result = apiInstance.restProofsDelete(body, proofHash, version);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling RestApi#restProofsDelete");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CancelProofRequest**](CancelProofRequest.md)|  |
 **proofHash** | **String**|  |
 **version** | **String**|  |

### Return type

[**CancelProofResponse**](CancelProofResponse.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="restProofsUpdate"></a>
# **restProofsUpdate**
> UpdateProofResponse restProofsUpdate(body, proofHash, version)



### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.RestApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();
// Configure HTTP basic authorization: Basic
HttpBasicAuth Basic = (HttpBasicAuth) defaultClient.getAuthentication("Basic");
Basic.setUsername("YOUR USERNAME");
Basic.setPassword("YOUR PASSWORD");

RestApi apiInstance = new RestApi();
UpdateProofRequest body = new UpdateProofRequest(); // UpdateProofRequest | 
String proofHash = "proofHash_example"; // String | 
String version = "version_example"; // String | 
try {
    UpdateProofResponse result = apiInstance.restProofsUpdate(body, proofHash, version);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling RestApi#restProofsUpdate");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateProofRequest**](UpdateProofRequest.md)|  |
 **proofHash** | **String**|  |
 **version** | **String**|  |

### Return type

[**UpdateProofResponse**](UpdateProofResponse.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

