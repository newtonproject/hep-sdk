# Swagger\Client\ProofsApi

All URIs are relative to *http://127.0.0.1:8000/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**proofsCreate**](ProofsApi.md#proofsCreate) | **POST** /proofs/ | 
[**proofsDelete**](ProofsApi.md#proofsDelete) | **DELETE** /proofs/{proof_hash}/ | 
[**proofsUpdate**](ProofsApi.md#proofsUpdate) | **PUT** /proofs/{proof_hash}/ | 

# **proofsCreate**
> \Swagger\Client\Model\CreateProofResponse proofsCreate($body)



### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');
// Configure HTTP basic authorization: Basic
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new Swagger\Client\Api\ProofsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$body = new \Swagger\Client\Model\CreateProofRequest(); // \Swagger\Client\Model\CreateProofRequest | 

try {
    $result = $apiInstance->proofsCreate($body);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ProofsApi->proofsCreate: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**\Swagger\Client\Model\CreateProofRequest**](../Model/CreateProofRequest.md)|  |

### Return type

[**\Swagger\Client\Model\CreateProofResponse**](../Model/CreateProofResponse.md)

### Authorization

[Basic](../../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **proofsDelete**
> \Swagger\Client\Model\CancelProofResponse proofsDelete($body, $proof_hash)



### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');
// Configure HTTP basic authorization: Basic
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new Swagger\Client\Api\ProofsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$body = new \Swagger\Client\Model\CancelProofRequest(); // \Swagger\Client\Model\CancelProofRequest | 
$proof_hash = "proof_hash_example"; // string | 

try {
    $result = $apiInstance->proofsDelete($body, $proof_hash);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ProofsApi->proofsDelete: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**\Swagger\Client\Model\CancelProofRequest**](../Model/CancelProofRequest.md)|  |
 **proof_hash** | **string**|  |

### Return type

[**\Swagger\Client\Model\CancelProofResponse**](../Model/CancelProofResponse.md)

### Authorization

[Basic](../../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **proofsUpdate**
> \Swagger\Client\Model\UpdateProofResponse proofsUpdate($body, $proof_hash)



### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');
// Configure HTTP basic authorization: Basic
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new Swagger\Client\Api\ProofsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$body = new \Swagger\Client\Model\UpdateProofRequest(); // \Swagger\Client\Model\UpdateProofRequest | 
$proof_hash = "proof_hash_example"; // string | 

try {
    $result = $apiInstance->proofsUpdate($body, $proof_hash);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ProofsApi->proofsUpdate: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**\Swagger\Client\Model\UpdateProofRequest**](../Model/UpdateProofRequest.md)|  |
 **proof_hash** | **string**|  |

### Return type

[**\Swagger\Client\Model\UpdateProofResponse**](../Model/UpdateProofResponse.md)

### Authorization

[Basic](../../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

