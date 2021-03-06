
# PayCacheResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dappKey** | **String** | The decentralized application access key | 
**protocol** | **String** | The protocol name. default is &#39;HEP&#39;. | 
**version** | **String** | The protocol version such as &#39;1.0&#39; | 
**ts** | **Integer** | The current timestamp | 
**nonce** | **String** | The random string or auto-increment sequence | 
**os** | **String** | The operating system of client such as ios, android, dweb,etc. | 
**language** | **String** | The i18n language code such as zh, en, etc. | 
**dappSignatureMethod** | **String** | The signature method used by dapp. | 
**dappSignature** | **String** | The signature generated by dapp. | 
**signType** | **String** | The signature Type,aka cryptographic algorithm. | 
**signature** | **String** | The signature hex string by application owner. The exclude fields is [sign_type, signature, md5]. | 
**uuid** | **String** | The request uuid | 
**dappId** | **String** | The decentralized application ID | 
**action** | **String** | The action name which value is &#39;hep.pay.order&#39; | 
**expired** | **Integer** | The expired timestamp | 
**description** | **String** | The order description | 
**priceCurrency** | **String** | The symbol of fiat or digital token, such as USD, CNY, NEW,BTC,ETH. | 
**totalPrice** | **String** | The amount of fiat or digital token, unit is the minimum unit of given fiat or digital token. | 
**orderNumber** | **String** | The order number | 
**seller** | **String** | The seller&#39;s NewID | 
**customer** | **String** | The customer&#39;s NewID | 
**broker** | **String** | The broker&#39;s NewID. optional. |  [optional]



