# Swagger\Client\RestApi

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

# **restDappsRead**
> \Swagger\Client\Model\Dapp restDappsRead($dapp_id, $version, $dapp_key, $protocol, $version2, $ts, $nonce, $os, $language, $md5)



### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');
// Configure HTTP basic authorization: Basic
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new Swagger\Client\Api\RestApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$dapp_id = "dapp_id_example"; // string | 
$version = "version_example"; // string | 
$dapp_key = "dapp_key_example"; // string | The decentralized application access key
$protocol = "protocol_example"; // string | The protocol name. default is 'HEP'.
$version2 = "version_example"; // string | The protocol version such as '1.0'
$ts = 56; // int | The current timestamp
$nonce = "nonce_example"; // string | The random string or auto-increment sequence
$os = "os_example"; // string | The operating system of client such as ios, android, dweb,etc.
$language = "language_example"; // string | The i18n language code such as zh, en, etc.
$md5 = "md5_example"; // string | The HMAC authentication md5 checksum

try {
    $result = $apiInstance->restDappsRead($dapp_id, $version, $dapp_key, $protocol, $version2, $ts, $nonce, $os, $language, $md5);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling RestApi->restDappsRead: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dapp_id** | **string**|  |
 **version** | **string**|  |
 **dapp_key** | **string**| The decentralized application access key |
 **protocol** | **string**| The protocol name. default is &#x27;HEP&#x27;. |
 **version2** | **string**| The protocol version such as &#x27;1.0&#x27; |
 **ts** | **int**| The current timestamp |
 **nonce** | **string**| The random string or auto-increment sequence |
 **os** | **string**| The operating system of client such as ios, android, dweb,etc. |
 **language** | **string**| The i18n language code such as zh, en, etc. |
 **md5** | **string**| The HMAC authentication md5 checksum |

### Return type

[**\Swagger\Client\Model\Dapp**](../Model/Dapp.md)

### Authorization

[Basic](../../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **restNewidsRead**
> \Swagger\Client\Model\NewidResponse restNewidsRead($newid, $version, $dapp_key, $protocol, $version2, $ts, $nonce, $os, $language, $md5)



Retrieve the information by given NewID

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');
// Configure HTTP basic authorization: Basic
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new Swagger\Client\Api\RestApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$newid = "newid_example"; // string | 
$version = "version_example"; // string | 
$dapp_key = "dapp_key_example"; // string | The decentralized application access key
$protocol = "protocol_example"; // string | The protocol name. default is 'HEP'.
$version2 = "version_example"; // string | The protocol version such as '1.0'
$ts = 56; // int | The current timestamp
$nonce = "nonce_example"; // string | The random string or auto-increment sequence
$os = "os_example"; // string | The operating system of client such as ios, android, dweb,etc.
$language = "language_example"; // string | The i18n language code such as zh, en, etc.
$md5 = "md5_example"; // string | The HMAC authentication md5 checksum

try {
    $result = $apiInstance->restNewidsRead($newid, $version, $dapp_key, $protocol, $version2, $ts, $nonce, $os, $language, $md5);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling RestApi->restNewidsRead: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **newid** | **string**|  |
 **version** | **string**|  |
 **dapp_key** | **string**| The decentralized application access key |
 **protocol** | **string**| The protocol name. default is &#x27;HEP&#x27;. |
 **version2** | **string**| The protocol version such as &#x27;1.0&#x27; |
 **ts** | **int**| The current timestamp |
 **nonce** | **string**| The random string or auto-increment sequence |
 **os** | **string**| The operating system of client such as ios, android, dweb,etc. |
 **language** | **string**| The i18n language code such as zh, en, etc. |
 **md5** | **string**| The HMAC authentication md5 checksum |

### Return type

[**\Swagger\Client\Model\NewidResponse**](../Model/NewidResponse.md)

### Authorization

[Basic](../../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **restNewnetCachesAuthCreate**
> \Swagger\Client\Model\CreateAuthCacheResponse restNewnetCachesAuthCreate($body, $version)



Caches the authentication request

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');
// Configure HTTP basic authorization: Basic
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new Swagger\Client\Api\RestApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$body = new \Swagger\Client\Model\AuthCacheRequest(); // \Swagger\Client\Model\AuthCacheRequest | 
$version = "version_example"; // string | 

try {
    $result = $apiInstance->restNewnetCachesAuthCreate($body, $version);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling RestApi->restNewnetCachesAuthCreate: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**\Swagger\Client\Model\AuthCacheRequest**](../Model/AuthCacheRequest.md)|  |
 **version** | **string**|  |

### Return type

[**\Swagger\Client\Model\CreateAuthCacheResponse**](../Model/CreateAuthCacheResponse.md)

### Authorization

[Basic](../../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **restNewnetCachesAuthRead**
> \Swagger\Client\Model\AuthCacheResponse restNewnetCachesAuthRead($auth_hash, $version, $dapp_key, $protocol, $version2, $ts, $nonce, $os, $language, $md5)



Get the authentication information by given request hash.

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');
// Configure HTTP basic authorization: Basic
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new Swagger\Client\Api\RestApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$auth_hash = "auth_hash_example"; // string | 
$version = "version_example"; // string | 
$dapp_key = "dapp_key_example"; // string | The decentralized application access key
$protocol = "protocol_example"; // string | The protocol name. default is 'HEP'.
$version2 = "version_example"; // string | The protocol version such as '1.0'
$ts = 56; // int | The current timestamp
$nonce = "nonce_example"; // string | The random string or auto-increment sequence
$os = "os_example"; // string | The operating system of client such as ios, android, dweb,etc.
$language = "language_example"; // string | The i18n language code such as zh, en, etc.
$md5 = "md5_example"; // string | The HMAC authentication md5 checksum

try {
    $result = $apiInstance->restNewnetCachesAuthRead($auth_hash, $version, $dapp_key, $protocol, $version2, $ts, $nonce, $os, $language, $md5);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling RestApi->restNewnetCachesAuthRead: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_hash** | **string**|  |
 **version** | **string**|  |
 **dapp_key** | **string**| The decentralized application access key |
 **protocol** | **string**| The protocol name. default is &#x27;HEP&#x27;. |
 **version2** | **string**| The protocol version such as &#x27;1.0&#x27; |
 **ts** | **int**| The current timestamp |
 **nonce** | **string**| The random string or auto-increment sequence |
 **os** | **string**| The operating system of client such as ios, android, dweb,etc. |
 **language** | **string**| The i18n language code such as zh, en, etc. |
 **md5** | **string**| The HMAC authentication md5 checksum |

### Return type

[**\Swagger\Client\Model\AuthCacheResponse**](../Model/AuthCacheResponse.md)

### Authorization

[Basic](../../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **restNewnetCachesPayCreate**
> \Swagger\Client\Model\CreatePayCacheResponse restNewnetCachesPayCreate($body, $version)



Cache the pay request

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');
// Configure HTTP basic authorization: Basic
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new Swagger\Client\Api\RestApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$body = new \Swagger\Client\Model\PayCacheRequest(); // \Swagger\Client\Model\PayCacheRequest | 
$version = "version_example"; // string | 

try {
    $result = $apiInstance->restNewnetCachesPayCreate($body, $version);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling RestApi->restNewnetCachesPayCreate: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**\Swagger\Client\Model\PayCacheRequest**](../Model/PayCacheRequest.md)|  |
 **version** | **string**|  |

### Return type

[**\Swagger\Client\Model\CreatePayCacheResponse**](../Model/CreatePayCacheResponse.md)

### Authorization

[Basic](../../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **restNewnetCachesPayRead**
> \Swagger\Client\Model\PayCacheResponse restNewnetCachesPayRead($pay_hash, $version, $dapp_key, $protocol, $version2, $ts, $nonce, $os, $language, $md5)



Retrieve the pay information by given pay hash.

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');
// Configure HTTP basic authorization: Basic
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new Swagger\Client\Api\RestApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$pay_hash = "pay_hash_example"; // string | 
$version = "version_example"; // string | 
$dapp_key = "dapp_key_example"; // string | The decentralized application access key
$protocol = "protocol_example"; // string | The protocol name. default is 'HEP'.
$version2 = "version_example"; // string | The protocol version such as '1.0'
$ts = 56; // int | The current timestamp
$nonce = "nonce_example"; // string | The random string or auto-increment sequence
$os = "os_example"; // string | The operating system of client such as ios, android, dweb,etc.
$language = "language_example"; // string | The i18n language code such as zh, en, etc.
$md5 = "md5_example"; // string | The HMAC authentication md5 checksum

try {
    $result = $apiInstance->restNewnetCachesPayRead($pay_hash, $version, $dapp_key, $protocol, $version2, $ts, $nonce, $os, $language, $md5);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling RestApi->restNewnetCachesPayRead: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pay_hash** | **string**|  |
 **version** | **string**|  |
 **dapp_key** | **string**| The decentralized application access key |
 **protocol** | **string**| The protocol name. default is &#x27;HEP&#x27;. |
 **version2** | **string**| The protocol version such as &#x27;1.0&#x27; |
 **ts** | **int**| The current timestamp |
 **nonce** | **string**| The random string or auto-increment sequence |
 **os** | **string**| The operating system of client such as ios, android, dweb,etc. |
 **language** | **string**| The i18n language code such as zh, en, etc. |
 **md5** | **string**| The HMAC authentication md5 checksum |

### Return type

[**\Swagger\Client\Model\PayCacheResponse**](../Model/PayCacheResponse.md)

### Authorization

[Basic](../../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **restProofsCreate**
> \Swagger\Client\Model\CreateProofResponse restProofsCreate($body, $version)



### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');
// Configure HTTP basic authorization: Basic
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new Swagger\Client\Api\RestApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$body = new \Swagger\Client\Model\CreateProofRequest(); // \Swagger\Client\Model\CreateProofRequest | 
$version = "version_example"; // string | 

try {
    $result = $apiInstance->restProofsCreate($body, $version);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling RestApi->restProofsCreate: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**\Swagger\Client\Model\CreateProofRequest**](../Model/CreateProofRequest.md)|  |
 **version** | **string**|  |

### Return type

[**\Swagger\Client\Model\CreateProofResponse**](../Model/CreateProofResponse.md)

### Authorization

[Basic](../../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **restProofsDelete**
> \Swagger\Client\Model\CancelProofResponse restProofsDelete($body, $proof_hash, $version)



### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');
// Configure HTTP basic authorization: Basic
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new Swagger\Client\Api\RestApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$body = new \Swagger\Client\Model\CancelProofRequest(); // \Swagger\Client\Model\CancelProofRequest | 
$proof_hash = "proof_hash_example"; // string | 
$version = "version_example"; // string | 

try {
    $result = $apiInstance->restProofsDelete($body, $proof_hash, $version);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling RestApi->restProofsDelete: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**\Swagger\Client\Model\CancelProofRequest**](../Model/CancelProofRequest.md)|  |
 **proof_hash** | **string**|  |
 **version** | **string**|  |

### Return type

[**\Swagger\Client\Model\CancelProofResponse**](../Model/CancelProofResponse.md)

### Authorization

[Basic](../../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **restProofsUpdate**
> \Swagger\Client\Model\UpdateProofResponse restProofsUpdate($body, $proof_hash, $version)



### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');
// Configure HTTP basic authorization: Basic
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new Swagger\Client\Api\RestApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$body = new \Swagger\Client\Model\UpdateProofRequest(); // \Swagger\Client\Model\UpdateProofRequest | 
$proof_hash = "proof_hash_example"; // string | 
$version = "version_example"; // string | 

try {
    $result = $apiInstance->restProofsUpdate($body, $proof_hash, $version);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling RestApi->restProofsUpdate: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**\Swagger\Client\Model\UpdateProofRequest**](../Model/UpdateProofRequest.md)|  |
 **proof_hash** | **string**|  |
 **version** | **string**|  |

### Return type

[**\Swagger\Client\Model\UpdateProofResponse**](../Model/UpdateProofResponse.md)

### Authorization

[Basic](../../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

