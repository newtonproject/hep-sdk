# Swagger\Client\DappsApi

All URIs are relative to *http://127.0.0.1:8000/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dappsRead**](DappsApi.md#dappsRead) | **GET** /dapps/{dapp_id}/ | 

# **dappsRead**
> \Swagger\Client\Model\Dapp dappsRead($dapp_id, $dapp_key, $protocol, $version, $ts, $nonce, $os, $language, $md5)



### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');
// Configure HTTP basic authorization: Basic
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new Swagger\Client\Api\DappsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$dapp_id = "dapp_id_example"; // string | 
$dapp_key = "dapp_key_example"; // string | The decentralized application access key
$protocol = "protocol_example"; // string | The protocol name. default is 'HEP'.
$version = "version_example"; // string | The protocol version such as '1.0'
$ts = 56; // int | The current timestamp
$nonce = "nonce_example"; // string | The random string or auto-increment sequence
$os = "os_example"; // string | The operating system of client such as ios, android, dweb,etc.
$language = "language_example"; // string | The i18n language code such as zh, en, etc.
$md5 = "md5_example"; // string | The HMAC authentication md5 checksum

try {
    $result = $apiInstance->dappsRead($dapp_id, $dapp_key, $protocol, $version, $ts, $nonce, $os, $language, $md5);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling DappsApi->dappsRead: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dapp_id** | **string**|  |
 **dapp_key** | **string**| The decentralized application access key |
 **protocol** | **string**| The protocol name. default is &#x27;HEP&#x27;. |
 **version** | **string**| The protocol version such as &#x27;1.0&#x27; |
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

