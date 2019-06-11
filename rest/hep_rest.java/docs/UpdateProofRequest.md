# UpdateProofRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dappKey** | **String** | The decentralized application access key | 
**protocol** | **String** | The protocol name. default is &#x27;HEP&#x27;. | 
**version** | **String** | The protocol version such as &#x27;1.0&#x27; | 
**ts** | **Integer** | The current timestamp | 
**nonce** | **String** | The random string or auto-increment sequence | 
**os** | **String** | The operating system of client such as ios, android, dweb,etc. | 
**language** | **String** | The i18n language code such as zh, en, etc. | 
**md5** | **String** | The HMAC authentication md5 checksum | 
**signType** | **String** | The signature Type,aka cryptographic algorithm. | 
**signature** | **String** | The signature hex string by application owner. The exclude fields is [sign_type, signature, md5]. | 
**confirmer** | **String** | The confirmer&#x27;s NewID | 