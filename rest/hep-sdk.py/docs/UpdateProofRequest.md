# UpdateProofRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dapp_key** | **str** | The decentralized application access key | 
**protocol** | **str** | The protocol name. default is &#x27;HEP&#x27;. | 
**version** | **str** | The protocol version such as &#x27;1.0&#x27; | 
**ts** | **int** | The current timestamp | 
**nonce** | **str** | The random string or auto-increment sequence | 
**os** | **str** | The operating system of client such as ios, android, dweb,etc. | 
**language** | **str** | The i18n language code such as zh, en, etc. | 
**md5** | **str** | The HMAC authentication md5 checksum | 
**sign_type** | **str** | The signature Type,aka cryptographic algorithm. | 
**signature** | **str** | The signature hex string by application owner. The exclude fields is [sign_type, signature, md5]. | 
**confirmer** | **str** | The confirmer&#x27;s NewID | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

