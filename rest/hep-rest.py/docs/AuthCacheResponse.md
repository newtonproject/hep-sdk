# AuthCacheResponse

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
**dapp_id** | **str** | The decentralized application ID | 
**uuid** | **str** | The request uuid | 
**action** | **str** | The action name which value is &#x27;hep.auth.login&#x27;. | 
**scope** | **int** | The request profile type. 1: base profile including name,head,newid; 2: advance profile including cellphone. | 
**expired** | **int** | The expired timestamp | 
**memo** | **str** | The login Memo,optional. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

