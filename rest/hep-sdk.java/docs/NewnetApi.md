# NewnetApi

All URIs are relative to *http://127.0.0.1:8000/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**newnetCachesAuthCreate**](NewnetApi.md#newnetCachesAuthCreate) | **POST** /newnet/caches/auth/ | 
[**newnetCachesAuthRead**](NewnetApi.md#newnetCachesAuthRead) | **GET** /newnet/caches/auth/{auth_hash}/ | 
[**newnetCachesPayCreate**](NewnetApi.md#newnetCachesPayCreate) | **POST** /newnet/caches/pay/ | 
[**newnetCachesPayRead**](NewnetApi.md#newnetCachesPayRead) | **GET** /newnet/caches/pay/{pay_hash}/ | 

<a name="newnetCachesAuthCreate"></a>
# **newnetCachesAuthCreate**
> CreateAuthCacheResponse newnetCachesAuthCreate(body)



Caches the authentication request

### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.NewnetApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();
// Configure HTTP basic authorization: Basic
HttpBasicAuth Basic = (HttpBasicAuth) defaultClient.getAuthentication("Basic");
Basic.setUsername("YOUR USERNAME");
Basic.setPassword("YOUR PASSWORD");

NewnetApi apiInstance = new NewnetApi();
AuthCacheRequest body = new AuthCacheRequest(); // AuthCacheRequest | 
try {
    CreateAuthCacheResponse result = apiInstance.newnetCachesAuthCreate(body);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling NewnetApi#newnetCachesAuthCreate");
    e.printStackTrace();
}
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

<a name="newnetCachesAuthRead"></a>
# **newnetCachesAuthRead**
> AuthCacheResponse newnetCachesAuthRead(authHash, dappKey, protocol, version, ts, nonce, os, language, md5)



Get the authentication information by given request hash.

### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.NewnetApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();
// Configure HTTP basic authorization: Basic
HttpBasicAuth Basic = (HttpBasicAuth) defaultClient.getAuthentication("Basic");
Basic.setUsername("YOUR USERNAME");
Basic.setPassword("YOUR PASSWORD");

NewnetApi apiInstance = new NewnetApi();
String authHash = "authHash_example"; // String | 
String dappKey = "dappKey_example"; // String | The decentralized application access key
String protocol = "protocol_example"; // String | The protocol name. default is 'HEP'.
String version = "version_example"; // String | The protocol version such as '1.0'
Integer ts = 56; // Integer | The current timestamp
String nonce = "nonce_example"; // String | The random string or auto-increment sequence
String os = "os_example"; // String | The operating system of client such as ios, android, dweb,etc.
String language = "language_example"; // String | The i18n language code such as zh, en, etc.
String md5 = "md5_example"; // String | The HMAC authentication md5 checksum
try {
    AuthCacheResponse result = apiInstance.newnetCachesAuthRead(authHash, dappKey, protocol, version, ts, nonce, os, language, md5);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling NewnetApi#newnetCachesAuthRead");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authHash** | **String**|  |
 **dappKey** | **String**| The decentralized application access key |
 **protocol** | **String**| The protocol name. default is &#x27;HEP&#x27;. |
 **version** | **String**| The protocol version such as &#x27;1.0&#x27; |
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

<a name="newnetCachesPayCreate"></a>
# **newnetCachesPayCreate**
> CreatePayCacheResponse newnetCachesPayCreate(body)



Cache the pay request

### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.NewnetApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();
// Configure HTTP basic authorization: Basic
HttpBasicAuth Basic = (HttpBasicAuth) defaultClient.getAuthentication("Basic");
Basic.setUsername("YOUR USERNAME");
Basic.setPassword("YOUR PASSWORD");

NewnetApi apiInstance = new NewnetApi();
PayCacheRequest body = new PayCacheRequest(); // PayCacheRequest | 
try {
    CreatePayCacheResponse result = apiInstance.newnetCachesPayCreate(body);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling NewnetApi#newnetCachesPayCreate");
    e.printStackTrace();
}
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

<a name="newnetCachesPayRead"></a>
# **newnetCachesPayRead**
> PayCacheResponse newnetCachesPayRead(payHash, dappKey, protocol, version, ts, nonce, os, language, md5)



Retrieve the pay information by given pay hash.

### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.NewnetApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();
// Configure HTTP basic authorization: Basic
HttpBasicAuth Basic = (HttpBasicAuth) defaultClient.getAuthentication("Basic");
Basic.setUsername("YOUR USERNAME");
Basic.setPassword("YOUR PASSWORD");

NewnetApi apiInstance = new NewnetApi();
String payHash = "payHash_example"; // String | 
String dappKey = "dappKey_example"; // String | The decentralized application access key
String protocol = "protocol_example"; // String | The protocol name. default is 'HEP'.
String version = "version_example"; // String | The protocol version such as '1.0'
Integer ts = 56; // Integer | The current timestamp
String nonce = "nonce_example"; // String | The random string or auto-increment sequence
String os = "os_example"; // String | The operating system of client such as ios, android, dweb,etc.
String language = "language_example"; // String | The i18n language code such as zh, en, etc.
String md5 = "md5_example"; // String | The HMAC authentication md5 checksum
try {
    PayCacheResponse result = apiInstance.newnetCachesPayRead(payHash, dappKey, protocol, version, ts, nonce, os, language, md5);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling NewnetApi#newnetCachesPayRead");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payHash** | **String**|  |
 **dappKey** | **String**| The decentralized application access key |
 **protocol** | **String**| The protocol name. default is &#x27;HEP&#x27;. |
 **version** | **String**| The protocol version such as &#x27;1.0&#x27; |
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

