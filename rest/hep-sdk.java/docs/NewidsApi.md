# NewidsApi

All URIs are relative to *http://127.0.0.1:8000/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**newidsRead**](NewidsApi.md#newidsRead) | **GET** /newids/{newid}/ | 

<a name="newidsRead"></a>
# **newidsRead**
> NewidResponse newidsRead(newid, dappKey, protocol, version, ts, nonce, os, language, md5)



Retrieve the information by given NewID

### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.NewidsApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();
// Configure HTTP basic authorization: Basic
HttpBasicAuth Basic = (HttpBasicAuth) defaultClient.getAuthentication("Basic");
Basic.setUsername("YOUR USERNAME");
Basic.setPassword("YOUR PASSWORD");

NewidsApi apiInstance = new NewidsApi();
String newid = "newid_example"; // String | 
String dappKey = "dappKey_example"; // String | The decentralized application access key
String protocol = "protocol_example"; // String | The protocol name. default is 'HEP'.
String version = "version_example"; // String | The protocol version such as '1.0'
Integer ts = 56; // Integer | The current timestamp
String nonce = "nonce_example"; // String | The random string or auto-increment sequence
String os = "os_example"; // String | The operating system of client such as ios, android, dweb,etc.
String language = "language_example"; // String | The i18n language code such as zh, en, etc.
String md5 = "md5_example"; // String | The HMAC authentication md5 checksum
try {
    NewidResponse result = apiInstance.newidsRead(newid, dappKey, protocol, version, ts, nonce, os, language, md5);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling NewidsApi#newidsRead");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **newid** | **String**|  |
 **dappKey** | **String**| The decentralized application access key |
 **protocol** | **String**| The protocol name. default is &#x27;HEP&#x27;. |
 **version** | **String**| The protocol version such as &#x27;1.0&#x27; |
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

