/*
 * HEP REST API
 * The REST API for HEP protocol
 *
 * OpenAPI spec version: v1
 * Contact: xiawu@zeuux.org
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 */

package io.swagger.client.model;

import java.util.Objects;
import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import io.swagger.v3.oas.annotations.media.Schema;
import java.io.IOException;

/**
 * AuthCacheResponse
 */

@javax.annotation.Generated(value = "io.swagger.codegen.v3.generators.java.JavaClientCodegen", date = "2019-06-14T20:03:01.379+08:00[Asia/Shanghai]")public class AuthCacheResponse {

  @SerializedName("dapp_key")
  private String dappKey = null;

  @SerializedName("protocol")
  private String protocol = null;

  @SerializedName("version")
  private String version = null;

  @SerializedName("ts")
  private Integer ts = null;

  @SerializedName("nonce")
  private String nonce = null;

  @SerializedName("os")
  private String os = null;

  @SerializedName("language")
  private String language = null;

  @SerializedName("dapp_signature_method")
  private String dappSignatureMethod = null;

  @SerializedName("dapp_signature")
  private String dappSignature = null;

  @SerializedName("sign_type")
  private String signType = null;

  @SerializedName("signature")
  private String signature = null;

  @SerializedName("dapp_id")
  private String dappId = null;

  @SerializedName("uuid")
  private String uuid = null;

  @SerializedName("action")
  private String action = null;

  @SerializedName("scope")
  private Integer scope = null;

  @SerializedName("expired")
  private Integer expired = null;

  @SerializedName("memo")
  private String memo = null;
  public AuthCacheResponse dappKey(String dappKey) {
    this.dappKey = dappKey;
    return this;
  }

  

  /**
  * The decentralized application access key
  * @return dappKey
  **/
  @Schema(required = true, description = "The decentralized application access key")
  public String getDappKey() {
    return dappKey;
  }
  public void setDappKey(String dappKey) {
    this.dappKey = dappKey;
  }
  public AuthCacheResponse protocol(String protocol) {
    this.protocol = protocol;
    return this;
  }

  

  /**
  * The protocol name. default is &#x27;HEP&#x27;.
  * @return protocol
  **/
  @Schema(required = true, description = "The protocol name. default is 'HEP'.")
  public String getProtocol() {
    return protocol;
  }
  public void setProtocol(String protocol) {
    this.protocol = protocol;
  }
  public AuthCacheResponse version(String version) {
    this.version = version;
    return this;
  }

  

  /**
  * The protocol version such as &#x27;1.0&#x27;
  * @return version
  **/
  @Schema(required = true, description = "The protocol version such as '1.0'")
  public String getVersion() {
    return version;
  }
  public void setVersion(String version) {
    this.version = version;
  }
  public AuthCacheResponse ts(Integer ts) {
    this.ts = ts;
    return this;
  }

  

  /**
  * The current timestamp
  * @return ts
  **/
  @Schema(required = true, description = "The current timestamp")
  public Integer getTs() {
    return ts;
  }
  public void setTs(Integer ts) {
    this.ts = ts;
  }
  public AuthCacheResponse nonce(String nonce) {
    this.nonce = nonce;
    return this;
  }

  

  /**
  * The random string or auto-increment sequence
  * @return nonce
  **/
  @Schema(required = true, description = "The random string or auto-increment sequence")
  public String getNonce() {
    return nonce;
  }
  public void setNonce(String nonce) {
    this.nonce = nonce;
  }
  public AuthCacheResponse os(String os) {
    this.os = os;
    return this;
  }

  

  /**
  * The operating system of client such as ios, android, dweb,etc.
  * @return os
  **/
  @Schema(required = true, description = "The operating system of client such as ios, android, dweb,etc.")
  public String getOs() {
    return os;
  }
  public void setOs(String os) {
    this.os = os;
  }
  public AuthCacheResponse language(String language) {
    this.language = language;
    return this;
  }

  

  /**
  * The i18n language code such as zh, en, etc.
  * @return language
  **/
  @Schema(required = true, description = "The i18n language code such as zh, en, etc.")
  public String getLanguage() {
    return language;
  }
  public void setLanguage(String language) {
    this.language = language;
  }
  public AuthCacheResponse dappSignatureMethod(String dappSignatureMethod) {
    this.dappSignatureMethod = dappSignatureMethod;
    return this;
  }

  

  /**
  * The signature method used by dapp.
  * @return dappSignatureMethod
  **/
  @Schema(required = true, description = "The signature method used by dapp.")
  public String getDappSignatureMethod() {
    return dappSignatureMethod;
  }
  public void setDappSignatureMethod(String dappSignatureMethod) {
    this.dappSignatureMethod = dappSignatureMethod;
  }
  public AuthCacheResponse dappSignature(String dappSignature) {
    this.dappSignature = dappSignature;
    return this;
  }

  

  /**
  * The signature generated by dapp.
  * @return dappSignature
  **/
  @Schema(required = true, description = "The signature generated by dapp.")
  public String getDappSignature() {
    return dappSignature;
  }
  public void setDappSignature(String dappSignature) {
    this.dappSignature = dappSignature;
  }
  public AuthCacheResponse signType(String signType) {
    this.signType = signType;
    return this;
  }

  

  /**
  * The signature Type,aka cryptographic algorithm.
  * @return signType
  **/
  @Schema(required = true, description = "The signature Type,aka cryptographic algorithm.")
  public String getSignType() {
    return signType;
  }
  public void setSignType(String signType) {
    this.signType = signType;
  }
  public AuthCacheResponse signature(String signature) {
    this.signature = signature;
    return this;
  }

  

  /**
  * The signature hex string by application owner. The exclude fields is [sign_type, signature, md5].
  * @return signature
  **/
  @Schema(required = true, description = "The signature hex string by application owner. The exclude fields is [sign_type, signature, md5].")
  public String getSignature() {
    return signature;
  }
  public void setSignature(String signature) {
    this.signature = signature;
  }
  public AuthCacheResponse dappId(String dappId) {
    this.dappId = dappId;
    return this;
  }

  

  /**
  * The decentralized application ID
  * @return dappId
  **/
  @Schema(required = true, description = "The decentralized application ID")
  public String getDappId() {
    return dappId;
  }
  public void setDappId(String dappId) {
    this.dappId = dappId;
  }
  public AuthCacheResponse uuid(String uuid) {
    this.uuid = uuid;
    return this;
  }

  

  /**
  * The request uuid
  * @return uuid
  **/
  @Schema(required = true, description = "The request uuid")
  public String getUuid() {
    return uuid;
  }
  public void setUuid(String uuid) {
    this.uuid = uuid;
  }
  public AuthCacheResponse action(String action) {
    this.action = action;
    return this;
  }

  

  /**
  * The action name which value is &#x27;hep.auth.login&#x27;.
  * @return action
  **/
  @Schema(required = true, description = "The action name which value is 'hep.auth.login'.")
  public String getAction() {
    return action;
  }
  public void setAction(String action) {
    this.action = action;
  }
  public AuthCacheResponse scope(Integer scope) {
    this.scope = scope;
    return this;
  }

  

  /**
  * The request profile type. 1: base profile including name,head,newid; 2: advance profile including cellphone.
  * @return scope
  **/
  @Schema(required = true, description = "The request profile type. 1: base profile including name,head,newid; 2: advance profile including cellphone.")
  public Integer getScope() {
    return scope;
  }
  public void setScope(Integer scope) {
    this.scope = scope;
  }
  public AuthCacheResponse expired(Integer expired) {
    this.expired = expired;
    return this;
  }

  

  /**
  * The expired timestamp
  * @return expired
  **/
  @Schema(required = true, description = "The expired timestamp")
  public Integer getExpired() {
    return expired;
  }
  public void setExpired(Integer expired) {
    this.expired = expired;
  }
  public AuthCacheResponse memo(String memo) {
    this.memo = memo;
    return this;
  }

  

  /**
  * The login Memo,optional.
  * @return memo
  **/
  @Schema(description = "The login Memo,optional.")
  public String getMemo() {
    return memo;
  }
  public void setMemo(String memo) {
    this.memo = memo;
  }
  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    AuthCacheResponse authCacheResponse = (AuthCacheResponse) o;
    return Objects.equals(this.dappKey, authCacheResponse.dappKey) &&
        Objects.equals(this.protocol, authCacheResponse.protocol) &&
        Objects.equals(this.version, authCacheResponse.version) &&
        Objects.equals(this.ts, authCacheResponse.ts) &&
        Objects.equals(this.nonce, authCacheResponse.nonce) &&
        Objects.equals(this.os, authCacheResponse.os) &&
        Objects.equals(this.language, authCacheResponse.language) &&
        Objects.equals(this.dappSignatureMethod, authCacheResponse.dappSignatureMethod) &&
        Objects.equals(this.dappSignature, authCacheResponse.dappSignature) &&
        Objects.equals(this.signType, authCacheResponse.signType) &&
        Objects.equals(this.signature, authCacheResponse.signature) &&
        Objects.equals(this.dappId, authCacheResponse.dappId) &&
        Objects.equals(this.uuid, authCacheResponse.uuid) &&
        Objects.equals(this.action, authCacheResponse.action) &&
        Objects.equals(this.scope, authCacheResponse.scope) &&
        Objects.equals(this.expired, authCacheResponse.expired) &&
        Objects.equals(this.memo, authCacheResponse.memo);
  }

  @Override
  public int hashCode() {
    return java.util.Objects.hash(dappKey, protocol, version, ts, nonce, os, language, dappSignatureMethod, dappSignature, signType, signature, dappId, uuid, action, scope, expired, memo);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class AuthCacheResponse {\n");
    
    sb.append("    dappKey: ").append(toIndentedString(dappKey)).append("\n");
    sb.append("    protocol: ").append(toIndentedString(protocol)).append("\n");
    sb.append("    version: ").append(toIndentedString(version)).append("\n");
    sb.append("    ts: ").append(toIndentedString(ts)).append("\n");
    sb.append("    nonce: ").append(toIndentedString(nonce)).append("\n");
    sb.append("    os: ").append(toIndentedString(os)).append("\n");
    sb.append("    language: ").append(toIndentedString(language)).append("\n");
    sb.append("    dappSignatureMethod: ").append(toIndentedString(dappSignatureMethod)).append("\n");
    sb.append("    dappSignature: ").append(toIndentedString(dappSignature)).append("\n");
    sb.append("    signType: ").append(toIndentedString(signType)).append("\n");
    sb.append("    signature: ").append(toIndentedString(signature)).append("\n");
    sb.append("    dappId: ").append(toIndentedString(dappId)).append("\n");
    sb.append("    uuid: ").append(toIndentedString(uuid)).append("\n");
    sb.append("    action: ").append(toIndentedString(action)).append("\n");
    sb.append("    scope: ").append(toIndentedString(scope)).append("\n");
    sb.append("    expired: ").append(toIndentedString(expired)).append("\n");
    sb.append("    memo: ").append(toIndentedString(memo)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(java.lang.Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }

}
