# PayCacheResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dapp_key** | **string** | The decentralized application access key | 
**protocol** | **string** | The protocol name. default is &#x27;HEP&#x27;. | 
**version** | **string** | The protocol version such as &#x27;1.0&#x27; | 
**ts** | **int** | The current timestamp | 
**nonce** | **string** | The random string or auto-increment sequence | 
**os** | **string** | The operating system of client such as ios, android, dweb,etc. | 
**language** | **string** | The i18n language code such as zh, en, etc. | 
**md5** | **string** | The HMAC authentication md5 checksum | 
**sign_type** | **string** | The signature Type,aka cryptographic algorithm. | 
**signature** | **string** | The signature hex string by application owner. The exclude fields is [sign_type, signature, md5]. | 
**uuid** | **string** | The request uuid | 
**dapp_id** | **string** | The decentralized application ID | 
**action** | **string** | The action name which value is &#x27;hep.pay.order&#x27; | 
**expired** | **int** | The expired timestamp | 
**description** | **string** | The order description | 
**price_currency** | **string** | The symbol of fiat or digital token, such as USD, CNY, NEW,BTC,ETH. | 
**total_price** | **string** | The amount of fiat or digital token, unit is the minimum unit of given fiat or digital token. | 
**order_number** | **string** | The order number | 
**seller** | **string** | The seller&#x27;s NewID | 
**customer** | **string** | The customer&#x27;s NewID | 
**broker** | **string** | The broker&#x27;s NewID. optional. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

