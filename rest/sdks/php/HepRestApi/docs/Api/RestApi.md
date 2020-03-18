# HepRestApi\RestApi

All URIs are relative to *http://localhost:8000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**restDappsRead**](RestApi.md#restDappsRead) | **GET** /rest/v{api_version}/dapps/{dapp_id}/ | 
[**restDappsRead_0**](RestApi.md#restDappsRead_0) | **GET** /rest/v{api_version}/dapps/{dapp_id}/{date}/ | 
[**restHealthList**](RestApi.md#restHealthList) | **GET** /rest/v{api_version}/health/ | 
[**restNewchainCoinGravityAccountRead**](RestApi.md#restNewchainCoinGravityAccountRead) | **GET** /rest/v{api_version}/newchain/coin/gravity/account/{newid}/ | 
[**restNewchainCoinGravityMintCollectCreate**](RestApi.md#restNewchainCoinGravityMintCollectCreate) | **POST** /rest/v{api_version}/newchain/coin/gravity/mint/collect/ | 
[**restNewchainCoinGravityMintConditionRead**](RestApi.md#restNewchainCoinGravityMintConditionRead) | **GET** /rest/v{api_version}/newchain/coin/gravity/mint/condition/{newid}/ | 
[**restNewchainCoinGravityMintDataCurrentRead**](RestApi.md#restNewchainCoinGravityMintDataCurrentRead) | **GET** /rest/v{api_version}/newchain/coin/gravity/mint/data/current/{newid}/ | 
[**restNewchainCoinGravityMintDataHistoryCreate**](RestApi.md#restNewchainCoinGravityMintDataHistoryCreate) | **POST** /rest/v{api_version}/newchain/coin/gravity/mint/data/history/ | 
[**restNewchainCoinGravityMintSubmitCreate**](RestApi.md#restNewchainCoinGravityMintSubmitCreate) | **POST** /rest/v{api_version}/newchain/coin/gravity/mint/submit/ | 
[**restNewchainCoinGravitySubscriptionConditionRead**](RestApi.md#restNewchainCoinGravitySubscriptionConditionRead) | **GET** /rest/v{api_version}/newchain/coin/gravity/subscription/condition/{newid}/ | 
[**restNewchainCoinGravitySubscriptionSubmitCreate**](RestApi.md#restNewchainCoinGravitySubscriptionSubmitCreate) | **POST** /rest/v{api_version}/newchain/coin/gravity/subscription/submit/ | 
[**restNewchainTxRead**](RestApi.md#restNewchainTxRead) | **GET** /rest/v{api_version}/newchain/tx/{txid}/ | 
[**restNewforceRead**](RestApi.md#restNewforceRead) | **GET** /rest/v{api_version}/newforce/{date}/ | 
[**restNewidsNewforceRewardList**](RestApi.md#restNewidsNewforceRewardList) | **GET** /rest/v{api_version}/newids/{newid}/newforce/reward/ | 
[**restNewidsRead**](RestApi.md#restNewidsRead) | **GET** /rest/v{api_version}/newids/{newid}/ | 
[**restNewnetCachesAuthCreate**](RestApi.md#restNewnetCachesAuthCreate) | **POST** /rest/v{api_version}/newnet/caches/auth/ | 
[**restNewnetCachesAuthRead**](RestApi.md#restNewnetCachesAuthRead) | **GET** /rest/v{api_version}/newnet/caches/auth/{auth_hash}/ | 
[**restNewnetCachesPayCreate**](RestApi.md#restNewnetCachesPayCreate) | **POST** /rest/v{api_version}/newnet/caches/pay/ | 
[**restNewnetCachesPayRead**](RestApi.md#restNewnetCachesPayRead) | **GET** /rest/v{api_version}/newnet/caches/pay/{pay_hash}/ | 
[**restOraclesRead**](RestApi.md#restOraclesRead) | **GET** /rest/v{api_version}/oracles/{oracle_id}/ | 
[**restProofsCreate**](RestApi.md#restProofsCreate) | **POST** /rest/v{api_version}/proofs/ | 
[**restProofsDelete**](RestApi.md#restProofsDelete) | **DELETE** /rest/v{api_version}/proofs/{proof_hash}/ | 
[**restProofsRead**](RestApi.md#restProofsRead) | **GET** /rest/v{api_version}/proofs/{proof_hash}/ | 
[**restProofsReceiptsCreate**](RestApi.md#restProofsReceiptsCreate) | **POST** /rest/v{api_version}/proofs/receipts/ | 
[**restProofsRewardsCreate**](RestApi.md#restProofsRewardsCreate) | **POST** /rest/v{api_version}/proofs/rewards/ | 


# **restDappsRead**
> \HepRestApi\Model\Dapp restDappsRead($api_version, $dapp_id, $dapp_key, $protocol, $version, $ts, $nonce, $os, $language, $dapp_signature_method, $dapp_signature)





### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure HTTP basic authorization: Basic
$config = HepRestApi\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new HepRestApi\Api\RestApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$api_version = "api_version_example"; // string | 
$dapp_id = "dapp_id_example"; // string | 
$dapp_key = "dapp_key_example"; // string | The decentralized application access key
$protocol = "protocol_example"; // string | The protocol name. default is 'HEP'.
$version = "version_example"; // string | The protocol version such as '1.0'
$ts = 56; // int | The current timestamp
$nonce = "nonce_example"; // string | The random string or auto-increment sequence
$os = "os_example"; // string | The operating system of client such as ios, android, dweb,etc.
$language = "language_example"; // string | The i18n language code such as zh, en, etc.
$dapp_signature_method = "dapp_signature_method_example"; // string | The signature method used by dapp.
$dapp_signature = "dapp_signature_example"; // string | The signature generated by dapp.

try {
    $result = $apiInstance->restDappsRead($api_version, $dapp_id, $dapp_key, $protocol, $version, $ts, $nonce, $os, $language, $dapp_signature_method, $dapp_signature);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling RestApi->restDappsRead: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **string**|  |
 **dapp_id** | **string**|  |
 **dapp_key** | **string**| The decentralized application access key |
 **protocol** | **string**| The protocol name. default is &#39;HEP&#39;. |
 **version** | **string**| The protocol version such as &#39;1.0&#39; |
 **ts** | **int**| The current timestamp |
 **nonce** | **string**| The random string or auto-increment sequence |
 **os** | **string**| The operating system of client such as ios, android, dweb,etc. |
 **language** | **string**| The i18n language code such as zh, en, etc. |
 **dapp_signature_method** | **string**| The signature method used by dapp. |
 **dapp_signature** | **string**| The signature generated by dapp. |

### Return type

[**\HepRestApi\Model\Dapp**](../Model/Dapp.md)

### Authorization

[Basic](../../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **restDappsRead_0**
> \HepRestApi\Model\RetrieveDappDailyStatsResponse restDappsRead_0($api_version, $dapp_id, $date, $dapp_key, $protocol, $version, $ts, $nonce, $os, $language, $dapp_signature_method, $dapp_signature)





### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure HTTP basic authorization: Basic
$config = HepRestApi\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new HepRestApi\Api\RestApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$api_version = "api_version_example"; // string | 
$dapp_id = "dapp_id_example"; // string | 
$date = "date_example"; // string | 
$dapp_key = "dapp_key_example"; // string | The decentralized application access key
$protocol = "protocol_example"; // string | The protocol name. default is 'HEP'.
$version = "version_example"; // string | The protocol version such as '1.0'
$ts = 56; // int | The current timestamp
$nonce = "nonce_example"; // string | The random string or auto-increment sequence
$os = "os_example"; // string | The operating system of client such as ios, android, dweb,etc.
$language = "language_example"; // string | The i18n language code such as zh, en, etc.
$dapp_signature_method = "dapp_signature_method_example"; // string | The signature method used by dapp.
$dapp_signature = "dapp_signature_example"; // string | The signature generated by dapp.

try {
    $result = $apiInstance->restDappsRead_0($api_version, $dapp_id, $date, $dapp_key, $protocol, $version, $ts, $nonce, $os, $language, $dapp_signature_method, $dapp_signature);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling RestApi->restDappsRead_0: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **string**|  |
 **dapp_id** | **string**|  |
 **date** | **string**|  |
 **dapp_key** | **string**| The decentralized application access key |
 **protocol** | **string**| The protocol name. default is &#39;HEP&#39;. |
 **version** | **string**| The protocol version such as &#39;1.0&#39; |
 **ts** | **int**| The current timestamp |
 **nonce** | **string**| The random string or auto-increment sequence |
 **os** | **string**| The operating system of client such as ios, android, dweb,etc. |
 **language** | **string**| The i18n language code such as zh, en, etc. |
 **dapp_signature_method** | **string**| The signature method used by dapp. |
 **dapp_signature** | **string**| The signature generated by dapp. |

### Return type

[**\HepRestApi\Model\RetrieveDappDailyStatsResponse**](../Model/RetrieveDappDailyStatsResponse.md)

### Authorization

[Basic](../../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **restHealthList**
> restHealthList($api_version)





### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure HTTP basic authorization: Basic
$config = HepRestApi\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new HepRestApi\Api\RestApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$api_version = "api_version_example"; // string | 

try {
    $apiInstance->restHealthList($api_version);
} catch (Exception $e) {
    echo 'Exception when calling RestApi->restHealthList: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **string**|  |

### Return type

void (empty response body)

### Authorization

[Basic](../../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **restNewchainCoinGravityAccountRead**
> \HepRestApi\Model\AccountResponse restNewchainCoinGravityAccountRead($api_version, $newid, $dapp_key, $protocol, $version, $ts, $nonce, $os, $language, $dapp_signature_method, $dapp_signature)





### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

$apiInstance = new HepRestApi\Api\RestApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$api_version = "api_version_example"; // string | 
$newid = "newid_example"; // string | 
$dapp_key = "dapp_key_example"; // string | The decentralized application access key
$protocol = "protocol_example"; // string | The protocol name. default is 'HEP'.
$version = "version_example"; // string | The protocol version such as '1.0'
$ts = 56; // int | The current timestamp
$nonce = "nonce_example"; // string | The random string or auto-increment sequence
$os = "os_example"; // string | The operating system of client such as ios, android, dweb,etc.
$language = "language_example"; // string | The i18n language code such as zh, en, etc.
$dapp_signature_method = "dapp_signature_method_example"; // string | The signature method used by dapp.
$dapp_signature = "dapp_signature_example"; // string | The signature generated by dapp.

try {
    $result = $apiInstance->restNewchainCoinGravityAccountRead($api_version, $newid, $dapp_key, $protocol, $version, $ts, $nonce, $os, $language, $dapp_signature_method, $dapp_signature);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling RestApi->restNewchainCoinGravityAccountRead: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **string**|  |
 **newid** | **string**|  |
 **dapp_key** | **string**| The decentralized application access key |
 **protocol** | **string**| The protocol name. default is &#39;HEP&#39;. |
 **version** | **string**| The protocol version such as &#39;1.0&#39; |
 **ts** | **int**| The current timestamp |
 **nonce** | **string**| The random string or auto-increment sequence |
 **os** | **string**| The operating system of client such as ios, android, dweb,etc. |
 **language** | **string**| The i18n language code such as zh, en, etc. |
 **dapp_signature_method** | **string**| The signature method used by dapp. |
 **dapp_signature** | **string**| The signature generated by dapp. |

### Return type

[**\HepRestApi\Model\AccountResponse**](../Model/AccountResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **restNewchainCoinGravityMintCollectCreate**
> \HepRestApi\Model\CollectMintResponse restNewchainCoinGravityMintCollectCreate($api_version, $data)





### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

$apiInstance = new HepRestApi\Api\RestApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$api_version = "api_version_example"; // string | 
$data = new \HepRestApi\Model\CollectMintRequest(); // \HepRestApi\Model\CollectMintRequest | 

try {
    $result = $apiInstance->restNewchainCoinGravityMintCollectCreate($api_version, $data);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling RestApi->restNewchainCoinGravityMintCollectCreate: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **string**|  |
 **data** | [**\HepRestApi\Model\CollectMintRequest**](../Model/CollectMintRequest.md)|  |

### Return type

[**\HepRestApi\Model\CollectMintResponse**](../Model/CollectMintResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **restNewchainCoinGravityMintConditionRead**
> \HepRestApi\Model\MintConditionResponse restNewchainCoinGravityMintConditionRead($api_version, $newid, $dapp_key, $protocol, $version, $ts, $nonce, $os, $language, $dapp_signature_method, $dapp_signature)





### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

$apiInstance = new HepRestApi\Api\RestApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$api_version = "api_version_example"; // string | 
$newid = "newid_example"; // string | 
$dapp_key = "dapp_key_example"; // string | The decentralized application access key
$protocol = "protocol_example"; // string | The protocol name. default is 'HEP'.
$version = "version_example"; // string | The protocol version such as '1.0'
$ts = 56; // int | The current timestamp
$nonce = "nonce_example"; // string | The random string or auto-increment sequence
$os = "os_example"; // string | The operating system of client such as ios, android, dweb,etc.
$language = "language_example"; // string | The i18n language code such as zh, en, etc.
$dapp_signature_method = "dapp_signature_method_example"; // string | The signature method used by dapp.
$dapp_signature = "dapp_signature_example"; // string | The signature generated by dapp.

try {
    $result = $apiInstance->restNewchainCoinGravityMintConditionRead($api_version, $newid, $dapp_key, $protocol, $version, $ts, $nonce, $os, $language, $dapp_signature_method, $dapp_signature);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling RestApi->restNewchainCoinGravityMintConditionRead: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **string**|  |
 **newid** | **string**|  |
 **dapp_key** | **string**| The decentralized application access key |
 **protocol** | **string**| The protocol name. default is &#39;HEP&#39;. |
 **version** | **string**| The protocol version such as &#39;1.0&#39; |
 **ts** | **int**| The current timestamp |
 **nonce** | **string**| The random string or auto-increment sequence |
 **os** | **string**| The operating system of client such as ios, android, dweb,etc. |
 **language** | **string**| The i18n language code such as zh, en, etc. |
 **dapp_signature_method** | **string**| The signature method used by dapp. |
 **dapp_signature** | **string**| The signature generated by dapp. |

### Return type

[**\HepRestApi\Model\MintConditionResponse**](../Model/MintConditionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **restNewchainCoinGravityMintDataCurrentRead**
> \HepRestApi\Model\CurrentDataResponse restNewchainCoinGravityMintDataCurrentRead($api_version, $newid, $dapp_key, $protocol, $version, $ts, $nonce, $os, $language, $dapp_signature_method, $dapp_signature)





### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

$apiInstance = new HepRestApi\Api\RestApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$api_version = "api_version_example"; // string | 
$newid = "newid_example"; // string | 
$dapp_key = "dapp_key_example"; // string | The decentralized application access key
$protocol = "protocol_example"; // string | The protocol name. default is 'HEP'.
$version = "version_example"; // string | The protocol version such as '1.0'
$ts = 56; // int | The current timestamp
$nonce = "nonce_example"; // string | The random string or auto-increment sequence
$os = "os_example"; // string | The operating system of client such as ios, android, dweb,etc.
$language = "language_example"; // string | The i18n language code such as zh, en, etc.
$dapp_signature_method = "dapp_signature_method_example"; // string | The signature method used by dapp.
$dapp_signature = "dapp_signature_example"; // string | The signature generated by dapp.

try {
    $result = $apiInstance->restNewchainCoinGravityMintDataCurrentRead($api_version, $newid, $dapp_key, $protocol, $version, $ts, $nonce, $os, $language, $dapp_signature_method, $dapp_signature);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling RestApi->restNewchainCoinGravityMintDataCurrentRead: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **string**|  |
 **newid** | **string**|  |
 **dapp_key** | **string**| The decentralized application access key |
 **protocol** | **string**| The protocol name. default is &#39;HEP&#39;. |
 **version** | **string**| The protocol version such as &#39;1.0&#39; |
 **ts** | **int**| The current timestamp |
 **nonce** | **string**| The random string or auto-increment sequence |
 **os** | **string**| The operating system of client such as ios, android, dweb,etc. |
 **language** | **string**| The i18n language code such as zh, en, etc. |
 **dapp_signature_method** | **string**| The signature method used by dapp. |
 **dapp_signature** | **string**| The signature generated by dapp. |

### Return type

[**\HepRestApi\Model\CurrentDataResponse**](../Model/CurrentDataResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **restNewchainCoinGravityMintDataHistoryCreate**
> \HepRestApi\Model\HistoryDataResponse restNewchainCoinGravityMintDataHistoryCreate($api_version, $data)





### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

$apiInstance = new HepRestApi\Api\RestApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$api_version = "api_version_example"; // string | 
$data = new \HepRestApi\Model\HistoryDataRequest(); // \HepRestApi\Model\HistoryDataRequest | 

try {
    $result = $apiInstance->restNewchainCoinGravityMintDataHistoryCreate($api_version, $data);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling RestApi->restNewchainCoinGravityMintDataHistoryCreate: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **string**|  |
 **data** | [**\HepRestApi\Model\HistoryDataRequest**](../Model/HistoryDataRequest.md)|  |

### Return type

[**\HepRestApi\Model\HistoryDataResponse**](../Model/HistoryDataResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **restNewchainCoinGravityMintSubmitCreate**
> \HepRestApi\Model\SubmitMintResponse restNewchainCoinGravityMintSubmitCreate($api_version, $data)





### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

$apiInstance = new HepRestApi\Api\RestApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$api_version = "api_version_example"; // string | 
$data = new \HepRestApi\Model\SubmitMintRequest(); // \HepRestApi\Model\SubmitMintRequest | 

try {
    $result = $apiInstance->restNewchainCoinGravityMintSubmitCreate($api_version, $data);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling RestApi->restNewchainCoinGravityMintSubmitCreate: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **string**|  |
 **data** | [**\HepRestApi\Model\SubmitMintRequest**](../Model/SubmitMintRequest.md)|  |

### Return type

[**\HepRestApi\Model\SubmitMintResponse**](../Model/SubmitMintResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **restNewchainCoinGravitySubscriptionConditionRead**
> \HepRestApi\Model\SubscribeConditionResponse restNewchainCoinGravitySubscriptionConditionRead($api_version, $newid, $dapp_key, $protocol, $version, $ts, $nonce, $os, $language, $dapp_signature_method, $dapp_signature)





### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

$apiInstance = new HepRestApi\Api\RestApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$api_version = "api_version_example"; // string | 
$newid = "newid_example"; // string | 
$dapp_key = "dapp_key_example"; // string | The decentralized application access key
$protocol = "protocol_example"; // string | The protocol name. default is 'HEP'.
$version = "version_example"; // string | The protocol version such as '1.0'
$ts = 56; // int | The current timestamp
$nonce = "nonce_example"; // string | The random string or auto-increment sequence
$os = "os_example"; // string | The operating system of client such as ios, android, dweb,etc.
$language = "language_example"; // string | The i18n language code such as zh, en, etc.
$dapp_signature_method = "dapp_signature_method_example"; // string | The signature method used by dapp.
$dapp_signature = "dapp_signature_example"; // string | The signature generated by dapp.

try {
    $result = $apiInstance->restNewchainCoinGravitySubscriptionConditionRead($api_version, $newid, $dapp_key, $protocol, $version, $ts, $nonce, $os, $language, $dapp_signature_method, $dapp_signature);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling RestApi->restNewchainCoinGravitySubscriptionConditionRead: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **string**|  |
 **newid** | **string**|  |
 **dapp_key** | **string**| The decentralized application access key |
 **protocol** | **string**| The protocol name. default is &#39;HEP&#39;. |
 **version** | **string**| The protocol version such as &#39;1.0&#39; |
 **ts** | **int**| The current timestamp |
 **nonce** | **string**| The random string or auto-increment sequence |
 **os** | **string**| The operating system of client such as ios, android, dweb,etc. |
 **language** | **string**| The i18n language code such as zh, en, etc. |
 **dapp_signature_method** | **string**| The signature method used by dapp. |
 **dapp_signature** | **string**| The signature generated by dapp. |

### Return type

[**\HepRestApi\Model\SubscribeConditionResponse**](../Model/SubscribeConditionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **restNewchainCoinGravitySubscriptionSubmitCreate**
> \HepRestApi\Model\SubmitSubscribeResponse restNewchainCoinGravitySubscriptionSubmitCreate($api_version, $data)





### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

$apiInstance = new HepRestApi\Api\RestApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$api_version = "api_version_example"; // string | 
$data = new \HepRestApi\Model\SubmitSubscribeRequest(); // \HepRestApi\Model\SubmitSubscribeRequest | 

try {
    $result = $apiInstance->restNewchainCoinGravitySubscriptionSubmitCreate($api_version, $data);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling RestApi->restNewchainCoinGravitySubscriptionSubmitCreate: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **string**|  |
 **data** | [**\HepRestApi\Model\SubmitSubscribeRequest**](../Model/SubmitSubscribeRequest.md)|  |

### Return type

[**\HepRestApi\Model\SubmitSubscribeResponse**](../Model/SubmitSubscribeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **restNewchainTxRead**
> \HepRestApi\Model\NewchainTransactionResponse restNewchainTxRead($api_version, $txid, $dapp_key, $protocol, $version, $ts, $nonce, $os, $language, $dapp_signature_method, $dapp_signature)



Retrieve the transaction information by given txid

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure HTTP basic authorization: Basic
$config = HepRestApi\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new HepRestApi\Api\RestApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$api_version = "api_version_example"; // string | 
$txid = "txid_example"; // string | 
$dapp_key = "dapp_key_example"; // string | The decentralized application access key
$protocol = "protocol_example"; // string | The protocol name. default is 'HEP'.
$version = "version_example"; // string | The protocol version such as '1.0'
$ts = 56; // int | The current timestamp
$nonce = "nonce_example"; // string | The random string or auto-increment sequence
$os = "os_example"; // string | The operating system of client such as ios, android, dweb,etc.
$language = "language_example"; // string | The i18n language code such as zh, en, etc.
$dapp_signature_method = "dapp_signature_method_example"; // string | The signature method used by dapp.
$dapp_signature = "dapp_signature_example"; // string | The signature generated by dapp.

try {
    $result = $apiInstance->restNewchainTxRead($api_version, $txid, $dapp_key, $protocol, $version, $ts, $nonce, $os, $language, $dapp_signature_method, $dapp_signature);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling RestApi->restNewchainTxRead: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **string**|  |
 **txid** | **string**|  |
 **dapp_key** | **string**| The decentralized application access key |
 **protocol** | **string**| The protocol name. default is &#39;HEP&#39;. |
 **version** | **string**| The protocol version such as &#39;1.0&#39; |
 **ts** | **int**| The current timestamp |
 **nonce** | **string**| The random string or auto-increment sequence |
 **os** | **string**| The operating system of client such as ios, android, dweb,etc. |
 **language** | **string**| The i18n language code such as zh, en, etc. |
 **dapp_signature_method** | **string**| The signature method used by dapp. |
 **dapp_signature** | **string**| The signature generated by dapp. |

### Return type

[**\HepRestApi\Model\NewchainTransactionResponse**](../Model/NewchainTransactionResponse.md)

### Authorization

[Basic](../../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **restNewforceRead**
> \HepRestApi\Model\NewforceDailyStatsResponse restNewforceRead($api_version, $date, $dapp_key, $protocol, $version, $ts, $nonce, $os, $language, $dapp_signature_method, $dapp_signature)



Retrieve the daily newforce statistics

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure HTTP basic authorization: Basic
$config = HepRestApi\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new HepRestApi\Api\RestApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$api_version = "api_version_example"; // string | 
$date = "date_example"; // string | 
$dapp_key = "dapp_key_example"; // string | The decentralized application access key
$protocol = "protocol_example"; // string | The protocol name. default is 'HEP'.
$version = "version_example"; // string | The protocol version such as '1.0'
$ts = 56; // int | The current timestamp
$nonce = "nonce_example"; // string | The random string or auto-increment sequence
$os = "os_example"; // string | The operating system of client such as ios, android, dweb,etc.
$language = "language_example"; // string | The i18n language code such as zh, en, etc.
$dapp_signature_method = "dapp_signature_method_example"; // string | The signature method used by dapp.
$dapp_signature = "dapp_signature_example"; // string | The signature generated by dapp.

try {
    $result = $apiInstance->restNewforceRead($api_version, $date, $dapp_key, $protocol, $version, $ts, $nonce, $os, $language, $dapp_signature_method, $dapp_signature);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling RestApi->restNewforceRead: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **string**|  |
 **date** | **string**|  |
 **dapp_key** | **string**| The decentralized application access key |
 **protocol** | **string**| The protocol name. default is &#39;HEP&#39;. |
 **version** | **string**| The protocol version such as &#39;1.0&#39; |
 **ts** | **int**| The current timestamp |
 **nonce** | **string**| The random string or auto-increment sequence |
 **os** | **string**| The operating system of client such as ios, android, dweb,etc. |
 **language** | **string**| The i18n language code such as zh, en, etc. |
 **dapp_signature_method** | **string**| The signature method used by dapp. |
 **dapp_signature** | **string**| The signature generated by dapp. |

### Return type

[**\HepRestApi\Model\NewforceDailyStatsResponse**](../Model/NewforceDailyStatsResponse.md)

### Authorization

[Basic](../../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **restNewforceTokensList**
> \HepRestApi\Model\NewforceRewardAmountResponse restNewforceTokensList($api_version, $newid, $dapp_key, $protocol, $version, $ts, $nonce, $os, $language, $dapp_signature_method, $dapp_signature)



Get the reward tokens amount by newid

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure HTTP basic authorization: Basic
$config = HepRestApi\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new HepRestApi\Api\RestApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$api_version = "api_version_example"; // string | 
$newid = "newid_example"; // string | 
$dapp_key = "dapp_key_example"; // string | The decentralized application access key
$protocol = "protocol_example"; // string | The protocol name. default is 'HEP'.
$version = "version_example"; // string | The protocol version such as '1.0'
$ts = 56; // int | The current timestamp
$nonce = "nonce_example"; // string | The random string or auto-increment sequence
$os = "os_example"; // string | The operating system of client such as ios, android, dweb,etc.
$language = "language_example"; // string | The i18n language code such as zh, en, etc.
$dapp_signature_method = "dapp_signature_method_example"; // string | The signature method used by dapp.
$dapp_signature = "dapp_signature_example"; // string | The signature generated by dapp.

try {
    $result = $apiInstance->restNewforceTokensList($api_version, $newid, $dapp_key, $protocol, $version, $ts, $nonce, $os, $language, $dapp_signature_method, $dapp_signature);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling RestApi->restNewforceTokensList: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **string**|  |
 **newid** | **string**|  |
 **dapp_key** | **string**| The decentralized application access key |
 **protocol** | **string**| The protocol name. default is &#39;HEP&#39;. |
 **version** | **string**| The protocol version such as &#39;1.0&#39; |
 **ts** | **int**| The current timestamp |
 **nonce** | **string**| The random string or auto-increment sequence |
 **os** | **string**| The operating system of client such as ios, android, dweb,etc. |
 **language** | **string**| The i18n language code such as zh, en, etc. |
 **dapp_signature_method** | **string**| The signature method used by dapp. |
 **dapp_signature** | **string**| The signature generated by dapp. |

### Return type

[**\HepRestApi\Model\NewforceRewardAmountResponse**](../Model/NewforceRewardAmountResponse.md)

### Authorization

[Basic](../../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **restNewidsNewforceRewardList**
> \HepRestApi\Model\NewforceRewardAmountResponse restNewidsNewforceRewardList($api_version, $newid, $dapp_key, $protocol, $version, $ts, $nonce, $os, $language, $dapp_signature_method, $dapp_signature)



Get the reward tokens amount by newid

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

$apiInstance = new HepRestApi\Api\RestApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$api_version = "api_version_example"; // string | 
$newid = "newid_example"; // string | 
$dapp_key = "dapp_key_example"; // string | The decentralized application access key
$protocol = "protocol_example"; // string | The protocol name. default is 'HEP'.
$version = "version_example"; // string | The protocol version such as '1.0'
$ts = 56; // int | The current timestamp
$nonce = "nonce_example"; // string | The random string or auto-increment sequence
$os = "os_example"; // string | The operating system of client such as ios, android, dweb,etc.
$language = "language_example"; // string | The i18n language code such as zh, en, etc.
$dapp_signature_method = "dapp_signature_method_example"; // string | The signature method used by dapp.
$dapp_signature = "dapp_signature_example"; // string | The signature generated by dapp.

try {
    $result = $apiInstance->restNewidsNewforceRewardList($api_version, $newid, $dapp_key, $protocol, $version, $ts, $nonce, $os, $language, $dapp_signature_method, $dapp_signature);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling RestApi->restNewidsNewforceRewardList: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **string**|  |
 **newid** | **string**|  |
 **dapp_key** | **string**| The decentralized application access key |
 **protocol** | **string**| The protocol name. default is &#39;HEP&#39;. |
 **version** | **string**| The protocol version such as &#39;1.0&#39; |
 **ts** | **int**| The current timestamp |
 **nonce** | **string**| The random string or auto-increment sequence |
 **os** | **string**| The operating system of client such as ios, android, dweb,etc. |
 **language** | **string**| The i18n language code such as zh, en, etc. |
 **dapp_signature_method** | **string**| The signature method used by dapp. |
 **dapp_signature** | **string**| The signature generated by dapp. |

### Return type

[**\HepRestApi\Model\NewforceRewardAmountResponse**](../Model/NewforceRewardAmountResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **restNewidsRead**
> \HepRestApi\Model\NewidResponse restNewidsRead($api_version, $newid, $dapp_key, $protocol, $version, $ts, $nonce, $os, $language, $dapp_signature_method, $dapp_signature)



Retrieve the information by given NewID

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure HTTP basic authorization: Basic
$config = HepRestApi\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new HepRestApi\Api\RestApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$api_version = "api_version_example"; // string | 
$newid = "newid_example"; // string | 
$dapp_key = "dapp_key_example"; // string | The decentralized application access key
$protocol = "protocol_example"; // string | The protocol name. default is 'HEP'.
$version = "version_example"; // string | The protocol version such as '1.0'
$ts = 56; // int | The current timestamp
$nonce = "nonce_example"; // string | The random string or auto-increment sequence
$os = "os_example"; // string | The operating system of client such as ios, android, dweb,etc.
$language = "language_example"; // string | The i18n language code such as zh, en, etc.
$dapp_signature_method = "dapp_signature_method_example"; // string | The signature method used by dapp.
$dapp_signature = "dapp_signature_example"; // string | The signature generated by dapp.

try {
    $result = $apiInstance->restNewidsRead($api_version, $newid, $dapp_key, $protocol, $version, $ts, $nonce, $os, $language, $dapp_signature_method, $dapp_signature);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling RestApi->restNewidsRead: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **string**|  |
 **newid** | **string**|  |
 **dapp_key** | **string**| The decentralized application access key |
 **protocol** | **string**| The protocol name. default is &#39;HEP&#39;. |
 **version** | **string**| The protocol version such as &#39;1.0&#39; |
 **ts** | **int**| The current timestamp |
 **nonce** | **string**| The random string or auto-increment sequence |
 **os** | **string**| The operating system of client such as ios, android, dweb,etc. |
 **language** | **string**| The i18n language code such as zh, en, etc. |
 **dapp_signature_method** | **string**| The signature method used by dapp. |
 **dapp_signature** | **string**| The signature generated by dapp. |

### Return type

[**\HepRestApi\Model\NewidResponse**](../Model/NewidResponse.md)

### Authorization

[Basic](../../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **restNewnetCachesAuthCreate**
> \HepRestApi\Model\CreateAuthCacheResponse restNewnetCachesAuthCreate($api_version, $data)



Caches the authentication request

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure HTTP basic authorization: Basic
$config = HepRestApi\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new HepRestApi\Api\RestApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$api_version = "api_version_example"; // string | 
$data = new \HepRestApi\Model\AuthCacheRequest(); // \HepRestApi\Model\AuthCacheRequest | 

try {
    $result = $apiInstance->restNewnetCachesAuthCreate($api_version, $data);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling RestApi->restNewnetCachesAuthCreate: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **string**|  |
 **data** | [**\HepRestApi\Model\AuthCacheRequest**](../Model/AuthCacheRequest.md)|  |

### Return type

[**\HepRestApi\Model\CreateAuthCacheResponse**](../Model/CreateAuthCacheResponse.md)

### Authorization

[Basic](../../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **restNewnetCachesAuthRead**
> \HepRestApi\Model\AuthCacheResponse restNewnetCachesAuthRead($api_version, $auth_hash, $dapp_key, $protocol, $version, $ts, $nonce, $os, $language, $dapp_signature_method, $dapp_signature)



Get the authentication information by given request hash.

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure HTTP basic authorization: Basic
$config = HepRestApi\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new HepRestApi\Api\RestApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$api_version = "api_version_example"; // string | 
$auth_hash = "auth_hash_example"; // string | 
$dapp_key = "dapp_key_example"; // string | The decentralized application access key
$protocol = "protocol_example"; // string | The protocol name. default is 'HEP'.
$version = "version_example"; // string | The protocol version such as '1.0'
$ts = 56; // int | The current timestamp
$nonce = "nonce_example"; // string | The random string or auto-increment sequence
$os = "os_example"; // string | The operating system of client such as ios, android, dweb,etc.
$language = "language_example"; // string | The i18n language code such as zh, en, etc.
$dapp_signature_method = "dapp_signature_method_example"; // string | The signature method used by dapp.
$dapp_signature = "dapp_signature_example"; // string | The signature generated by dapp.

try {
    $result = $apiInstance->restNewnetCachesAuthRead($api_version, $auth_hash, $dapp_key, $protocol, $version, $ts, $nonce, $os, $language, $dapp_signature_method, $dapp_signature);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling RestApi->restNewnetCachesAuthRead: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **string**|  |
 **auth_hash** | **string**|  |
 **dapp_key** | **string**| The decentralized application access key |
 **protocol** | **string**| The protocol name. default is &#39;HEP&#39;. |
 **version** | **string**| The protocol version such as &#39;1.0&#39; |
 **ts** | **int**| The current timestamp |
 **nonce** | **string**| The random string or auto-increment sequence |
 **os** | **string**| The operating system of client such as ios, android, dweb,etc. |
 **language** | **string**| The i18n language code such as zh, en, etc. |
 **dapp_signature_method** | **string**| The signature method used by dapp. |
 **dapp_signature** | **string**| The signature generated by dapp. |

### Return type

[**\HepRestApi\Model\AuthCacheResponse**](../Model/AuthCacheResponse.md)

### Authorization

[Basic](../../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **restNewnetCachesPayCreate**
> \HepRestApi\Model\CreatePayCacheResponse restNewnetCachesPayCreate($api_version, $data)



Cache the pay request

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure HTTP basic authorization: Basic
$config = HepRestApi\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new HepRestApi\Api\RestApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$api_version = "api_version_example"; // string | 
$data = new \HepRestApi\Model\PayCacheRequest(); // \HepRestApi\Model\PayCacheRequest | 

try {
    $result = $apiInstance->restNewnetCachesPayCreate($api_version, $data);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling RestApi->restNewnetCachesPayCreate: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **string**|  |
 **data** | [**\HepRestApi\Model\PayCacheRequest**](../Model/PayCacheRequest.md)|  |

### Return type

[**\HepRestApi\Model\CreatePayCacheResponse**](../Model/CreatePayCacheResponse.md)

### Authorization

[Basic](../../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **restNewnetCachesPayRead**
> \HepRestApi\Model\PayCacheResponse restNewnetCachesPayRead($api_version, $pay_hash, $dapp_key, $protocol, $version, $ts, $nonce, $os, $language, $dapp_signature_method, $dapp_signature)



Retrieve the pay information by given pay hash.

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure HTTP basic authorization: Basic
$config = HepRestApi\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new HepRestApi\Api\RestApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$api_version = "api_version_example"; // string | 
$pay_hash = "pay_hash_example"; // string | 
$dapp_key = "dapp_key_example"; // string | The decentralized application access key
$protocol = "protocol_example"; // string | The protocol name. default is 'HEP'.
$version = "version_example"; // string | The protocol version such as '1.0'
$ts = 56; // int | The current timestamp
$nonce = "nonce_example"; // string | The random string or auto-increment sequence
$os = "os_example"; // string | The operating system of client such as ios, android, dweb,etc.
$language = "language_example"; // string | The i18n language code such as zh, en, etc.
$dapp_signature_method = "dapp_signature_method_example"; // string | The signature method used by dapp.
$dapp_signature = "dapp_signature_example"; // string | The signature generated by dapp.

try {
    $result = $apiInstance->restNewnetCachesPayRead($api_version, $pay_hash, $dapp_key, $protocol, $version, $ts, $nonce, $os, $language, $dapp_signature_method, $dapp_signature);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling RestApi->restNewnetCachesPayRead: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **string**|  |
 **pay_hash** | **string**|  |
 **dapp_key** | **string**| The decentralized application access key |
 **protocol** | **string**| The protocol name. default is &#39;HEP&#39;. |
 **version** | **string**| The protocol version such as &#39;1.0&#39; |
 **ts** | **int**| The current timestamp |
 **nonce** | **string**| The random string or auto-increment sequence |
 **os** | **string**| The operating system of client such as ios, android, dweb,etc. |
 **language** | **string**| The i18n language code such as zh, en, etc. |
 **dapp_signature_method** | **string**| The signature method used by dapp. |
 **dapp_signature** | **string**| The signature generated by dapp. |

### Return type

[**\HepRestApi\Model\PayCacheResponse**](../Model/PayCacheResponse.md)

### Authorization

[Basic](../../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **restOraclesRead**
> \HepRestApi\Model\RetrieveOracleResponse restOraclesRead($api_version, $oracle_id, $dapp_key, $protocol, $version, $ts, $nonce, $os, $language, $dapp_signature_method, $dapp_signature)



Get the oracle information by given id.

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure HTTP basic authorization: Basic
$config = HepRestApi\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new HepRestApi\Api\RestApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$api_version = "api_version_example"; // string | 
$oracle_id = "oracle_id_example"; // string | 
$dapp_key = "dapp_key_example"; // string | The decentralized application access key
$protocol = "protocol_example"; // string | The protocol name. default is 'HEP'.
$version = "version_example"; // string | The protocol version such as '1.0'
$ts = 56; // int | The current timestamp
$nonce = "nonce_example"; // string | The random string or auto-increment sequence
$os = "os_example"; // string | The operating system of client such as ios, android, dweb,etc.
$language = "language_example"; // string | The i18n language code such as zh, en, etc.
$dapp_signature_method = "dapp_signature_method_example"; // string | The signature method used by dapp.
$dapp_signature = "dapp_signature_example"; // string | The signature generated by dapp.

try {
    $result = $apiInstance->restOraclesRead($api_version, $oracle_id, $dapp_key, $protocol, $version, $ts, $nonce, $os, $language, $dapp_signature_method, $dapp_signature);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling RestApi->restOraclesRead: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **string**|  |
 **oracle_id** | **string**|  |
 **dapp_key** | **string**| The decentralized application access key |
 **protocol** | **string**| The protocol name. default is &#39;HEP&#39;. |
 **version** | **string**| The protocol version such as &#39;1.0&#39; |
 **ts** | **int**| The current timestamp |
 **nonce** | **string**| The random string or auto-increment sequence |
 **os** | **string**| The operating system of client such as ios, android, dweb,etc. |
 **language** | **string**| The i18n language code such as zh, en, etc. |
 **dapp_signature_method** | **string**| The signature method used by dapp. |
 **dapp_signature** | **string**| The signature generated by dapp. |

### Return type

[**\HepRestApi\Model\RetrieveOracleResponse**](../Model/RetrieveOracleResponse.md)

### Authorization

[Basic](../../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **restProofsCreate**
> \HepRestApi\Model\CreateProofResponse restProofsCreate($api_version, $data)





### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure HTTP basic authorization: Basic
$config = HepRestApi\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new HepRestApi\Api\RestApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$api_version = "api_version_example"; // string | 
$data = new \HepRestApi\Model\CreateProofRequest(); // \HepRestApi\Model\CreateProofRequest | 

try {
    $result = $apiInstance->restProofsCreate($api_version, $data);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling RestApi->restProofsCreate: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **string**|  |
 **data** | [**\HepRestApi\Model\CreateProofRequest**](../Model/CreateProofRequest.md)|  |

### Return type

[**\HepRestApi\Model\CreateProofResponse**](../Model/CreateProofResponse.md)

### Authorization

[Basic](../../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **restProofsDelete**
> \HepRestApi\Model\CancelProofResponse restProofsDelete($api_version, $proof_hash, $data)





### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure HTTP basic authorization: Basic
$config = HepRestApi\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new HepRestApi\Api\RestApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$api_version = "api_version_example"; // string | 
$proof_hash = "proof_hash_example"; // string | 
$data = new \HepRestApi\Model\CancelProofRequest(); // \HepRestApi\Model\CancelProofRequest | 

try {
    $result = $apiInstance->restProofsDelete($api_version, $proof_hash, $data);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling RestApi->restProofsDelete: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **string**|  |
 **proof_hash** | **string**|  |
 **data** | [**\HepRestApi\Model\CancelProofRequest**](../Model/CancelProofRequest.md)|  |

### Return type

[**\HepRestApi\Model\CancelProofResponse**](../Model/CancelProofResponse.md)

### Authorization

[Basic](../../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **restProofsRead**
> \HepRestApi\Model\ProofResponse restProofsRead($api_version, $proof_hash, $dapp_key, $protocol, $version, $ts, $nonce, $os, $language, $dapp_signature_method, $dapp_signature)



Get the proof by given proof hash.

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure HTTP basic authorization: Basic
$config = HepRestApi\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new HepRestApi\Api\RestApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$api_version = "api_version_example"; // string | 
$proof_hash = "proof_hash_example"; // string | 
$dapp_key = "dapp_key_example"; // string | The decentralized application access key
$protocol = "protocol_example"; // string | The protocol name. default is 'HEP'.
$version = "version_example"; // string | The protocol version such as '1.0'
$ts = 56; // int | The current timestamp
$nonce = "nonce_example"; // string | The random string or auto-increment sequence
$os = "os_example"; // string | The operating system of client such as ios, android, dweb,etc.
$language = "language_example"; // string | The i18n language code such as zh, en, etc.
$dapp_signature_method = "dapp_signature_method_example"; // string | The signature method used by dapp.
$dapp_signature = "dapp_signature_example"; // string | The signature generated by dapp.

try {
    $result = $apiInstance->restProofsRead($api_version, $proof_hash, $dapp_key, $protocol, $version, $ts, $nonce, $os, $language, $dapp_signature_method, $dapp_signature);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling RestApi->restProofsRead: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **string**|  |
 **proof_hash** | **string**|  |
 **dapp_key** | **string**| The decentralized application access key |
 **protocol** | **string**| The protocol name. default is &#39;HEP&#39;. |
 **version** | **string**| The protocol version such as &#39;1.0&#39; |
 **ts** | **int**| The current timestamp |
 **nonce** | **string**| The random string or auto-increment sequence |
 **os** | **string**| The operating system of client such as ios, android, dweb,etc. |
 **language** | **string**| The i18n language code such as zh, en, etc. |
 **dapp_signature_method** | **string**| The signature method used by dapp. |
 **dapp_signature** | **string**| The signature generated by dapp. |

### Return type

[**\HepRestApi\Model\ProofResponse**](../Model/ProofResponse.md)

### Authorization

[Basic](../../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **restProofsReceiptsCreate**
> \HepRestApi\Model\RetrieveProofReceiptsResponse restProofsReceiptsCreate($api_version, $data)





### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure HTTP basic authorization: Basic
$config = HepRestApi\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new HepRestApi\Api\RestApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$api_version = "api_version_example"; // string | 
$data = new \HepRestApi\Model\RetrieveProofReceiptsRequest(); // \HepRestApi\Model\RetrieveProofReceiptsRequest | 

try {
    $result = $apiInstance->restProofsReceiptsCreate($api_version, $data);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling RestApi->restProofsReceiptsCreate: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **string**|  |
 **data** | [**\HepRestApi\Model\RetrieveProofReceiptsRequest**](../Model/RetrieveProofReceiptsRequest.md)|  |

### Return type

[**\HepRestApi\Model\RetrieveProofReceiptsResponse**](../Model/RetrieveProofReceiptsResponse.md)

### Authorization

[Basic](../../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **restProofsRewardsCreate**
> \HepRestApi\Model\RetrieveProofRewardsResponse restProofsRewardsCreate($api_version, $data)





### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure HTTP basic authorization: Basic
$config = HepRestApi\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new HepRestApi\Api\RestApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$api_version = "api_version_example"; // string | 
$data = new \HepRestApi\Model\RetrieveProofRewardsRequest(); // \HepRestApi\Model\RetrieveProofRewardsRequest | 

try {
    $result = $apiInstance->restProofsRewardsCreate($api_version, $data);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling RestApi->restProofsRewardsCreate: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **string**|  |
 **data** | [**\HepRestApi\Model\RetrieveProofRewardsRequest**](../Model/RetrieveProofRewardsRequest.md)|  |

### Return type

[**\HepRestApi\Model\RetrieveProofRewardsResponse**](../Model/RetrieveProofRewardsResponse.md)

### Authorization

[Basic](../../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

