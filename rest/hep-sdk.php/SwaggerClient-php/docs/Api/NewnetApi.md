# Swagger\Client\NewnetApi

All URIs are relative to *http://127.0.0.1:8000/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**newnetCachesAuthCreate**](NewnetApi.md#newnetCachesAuthCreate) | **POST** /newnet/caches/auth/ | 
[**newnetCachesAuthRead**](NewnetApi.md#newnetCachesAuthRead) | **GET** /newnet/caches/auth/{auth_hash}/ | 
[**newnetCachesPayCreate**](NewnetApi.md#newnetCachesPayCreate) | **POST** /newnet/caches/pay/ | 
[**newnetCachesPayRead**](NewnetApi.md#newnetCachesPayRead) | **GET** /newnet/caches/pay/{pay_hash}/ | 

# **newnetCachesAuthCreate**
> \Swagger\Client\Model\CreateAuthCacheResponse newnetCachesAuthCreate($body)



Caches the authentication request

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');
// Configure HTTP basic authorization: Basic
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new Swagger\Client\Api\NewnetApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$body = new \Swagger\Client\Model\AuthCacheRequest(); // \Swagger\Client\Model\AuthCacheRequest | 

try {
    $result = $apiInstance->newnetCachesAuthCreate($body);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling NewnetApi->newnetCachesAuthCreate: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**\Swagger\Client\Model\AuthCacheRequest**](../Model/AuthCacheRequest.md)|  |

### Return type

[**\Swagger\Client\Model\CreateAuthCacheResponse**](../Model/CreateAuthCacheResponse.md)

### Authorization

[Basic](../../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **newnetCachesAuthRead**
> \Swagger\Client\Model\AuthCacheResponse newnetCachesAuthRead($auth_hash, $dapp_key, $protocol, $version, $ts, $nonce, $os, $language, $md5)



Get the authentication information by given request hash.

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');
// Configure HTTP basic authorization: Basic
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new Swagger\Client\Api\NewnetApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$auth_hash = "auth_hash_example"; // string | 
$dapp_key = "dapp_key_example"; // string | The decentralized application access key
$protocol = "protocol_example"; // string | The protocol name. default is 'HEP'.
$version = "version_example"; // string | The protocol version such as '1.0'
$ts = 56; // int | The current timestamp
$nonce = "nonce_example"; // string | The random string or auto-increment sequence
$os = "os_example"; // string | The operating system of client such as ios, android, dweb,etc.
$language = "language_example"; // string | The i18n language code such as zh, en, etc.
$md5 = "md5_example"; // string | The HMAC authentication md5 checksum

try {
    $result = $apiInstance->newnetCachesAuthRead($auth_hash, $dapp_key, $protocol, $version, $ts, $nonce, $os, $language, $md5);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling NewnetApi->newnetCachesAuthRead: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_hash** | **string**|  |
 **dapp_key** | **string**| The decentralized application access key |
 **protocol** | **string**| The protocol name. default is &#x27;HEP&#x27;. |
 **version** | **string**| The protocol version such as &#x27;1.0&#x27; |
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

# **newnetCachesPayCreate**
> \Swagger\Client\Model\CreatePayCacheResponse newnetCachesPayCreate($body)



Cache the pay request

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');
// Configure HTTP basic authorization: Basic
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new Swagger\Client\Api\NewnetApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$body = new \Swagger\Client\Model\PayCacheRequest(); // \Swagger\Client\Model\PayCacheRequest | 

try {
    $result = $apiInstance->newnetCachesPayCreate($body);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling NewnetApi->newnetCachesPayCreate: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**\Swagger\Client\Model\PayCacheRequest**](../Model/PayCacheRequest.md)|  |

### Return type

[**\Swagger\Client\Model\CreatePayCacheResponse**](../Model/CreatePayCacheResponse.md)

### Authorization

[Basic](../../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **newnetCachesPayRead**
> \Swagger\Client\Model\PayCacheResponse newnetCachesPayRead($pay_hash, $dapp_key, $protocol, $version, $ts, $nonce, $os, $language, $md5)



Retrieve the pay information by given pay hash.

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');
// Configure HTTP basic authorization: Basic
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new Swagger\Client\Api\NewnetApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$pay_hash = "pay_hash_example"; // string | 
$dapp_key = "dapp_key_example"; // string | The decentralized application access key
$protocol = "protocol_example"; // string | The protocol name. default is 'HEP'.
$version = "version_example"; // string | The protocol version such as '1.0'
$ts = 56; // int | The current timestamp
$nonce = "nonce_example"; // string | The random string or auto-increment sequence
$os = "os_example"; // string | The operating system of client such as ios, android, dweb,etc.
$language = "language_example"; // string | The i18n language code such as zh, en, etc.
$md5 = "md5_example"; // string | The HMAC authentication md5 checksum

try {
    $result = $apiInstance->newnetCachesPayRead($pay_hash, $dapp_key, $protocol, $version, $ts, $nonce, $os, $language, $md5);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling NewnetApi->newnetCachesPayRead: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pay_hash** | **string**|  |
 **dapp_key** | **string**| The decentralized application access key |
 **protocol** | **string**| The protocol name. default is &#x27;HEP&#x27;. |
 **version** | **string**| The protocol version such as &#x27;1.0&#x27; |
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

