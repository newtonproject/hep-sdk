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
 * PayCacheRequest
 */

@javax.annotation.Generated(value = "io.swagger.codegen.v3.generators.java.JavaClientCodegen", date = "2019-06-13T17:16:26.272+08:00[Asia/Shanghai]")public class PayCacheRequest {

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

  @SerializedName("md5")
  private String md5 = null;

  @SerializedName("sign_type")
  private String signType = null;

  @SerializedName("signature")
  private String signature = null;

  @SerializedName("uuid")
  private String uuid = null;

  @SerializedName("dapp_id")
  private String dappId = null;

  @SerializedName("action")
  private String action = null;

  @SerializedName("expired")
  private Integer expired = null;

  @SerializedName("description")
  private String description = null;

  @SerializedName("price_currency")
  private String priceCurrency = null;

  @SerializedName("total_price")
  private String totalPrice = null;

  @SerializedName("order_number")
  private String orderNumber = null;

  @SerializedName("seller")
  private String seller = null;

  @SerializedName("customer")
  private String customer = null;

  @SerializedName("broker")
  private String broker = null;
  public PayCacheRequest dappKey(String dappKey) {
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
  public PayCacheRequest protocol(String protocol) {
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
  public PayCacheRequest version(String version) {
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
  public PayCacheRequest ts(Integer ts) {
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
  public PayCacheRequest nonce(String nonce) {
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
  public PayCacheRequest os(String os) {
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
  public PayCacheRequest language(String language) {
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
  public PayCacheRequest md5(String md5) {
    this.md5 = md5;
    return this;
  }

  

  /**
  * The HMAC authentication md5 checksum
  * @return md5
  **/
  @Schema(required = true, description = "The HMAC authentication md5 checksum")
  public String getMd5() {
    return md5;
  }
  public void setMd5(String md5) {
    this.md5 = md5;
  }
  public PayCacheRequest signType(String signType) {
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
  public PayCacheRequest signature(String signature) {
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
  public PayCacheRequest uuid(String uuid) {
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
  public PayCacheRequest dappId(String dappId) {
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
  public PayCacheRequest action(String action) {
    this.action = action;
    return this;
  }

  

  /**
  * The action name which value is &#x27;hep.pay.order&#x27;
  * @return action
  **/
  @Schema(required = true, description = "The action name which value is 'hep.pay.order'")
  public String getAction() {
    return action;
  }
  public void setAction(String action) {
    this.action = action;
  }
  public PayCacheRequest expired(Integer expired) {
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
  public PayCacheRequest description(String description) {
    this.description = description;
    return this;
  }

  

  /**
  * The order description
  * @return description
  **/
  @Schema(required = true, description = "The order description")
  public String getDescription() {
    return description;
  }
  public void setDescription(String description) {
    this.description = description;
  }
  public PayCacheRequest priceCurrency(String priceCurrency) {
    this.priceCurrency = priceCurrency;
    return this;
  }

  

  /**
  * The symbol of fiat or digital token, such as USD, CNY, NEW,BTC,ETH.
  * @return priceCurrency
  **/
  @Schema(required = true, description = "The symbol of fiat or digital token, such as USD, CNY, NEW,BTC,ETH.")
  public String getPriceCurrency() {
    return priceCurrency;
  }
  public void setPriceCurrency(String priceCurrency) {
    this.priceCurrency = priceCurrency;
  }
  public PayCacheRequest totalPrice(String totalPrice) {
    this.totalPrice = totalPrice;
    return this;
  }

  

  /**
  * The amount of fiat or digital token, unit is the minimum unit of given fiat or digital token.
  * @return totalPrice
  **/
  @Schema(required = true, description = "The amount of fiat or digital token, unit is the minimum unit of given fiat or digital token.")
  public String getTotalPrice() {
    return totalPrice;
  }
  public void setTotalPrice(String totalPrice) {
    this.totalPrice = totalPrice;
  }
  public PayCacheRequest orderNumber(String orderNumber) {
    this.orderNumber = orderNumber;
    return this;
  }

  

  /**
  * The order number
  * @return orderNumber
  **/
  @Schema(required = true, description = "The order number")
  public String getOrderNumber() {
    return orderNumber;
  }
  public void setOrderNumber(String orderNumber) {
    this.orderNumber = orderNumber;
  }
  public PayCacheRequest seller(String seller) {
    this.seller = seller;
    return this;
  }

  

  /**
  * The seller&#x27;s NewID
  * @return seller
  **/
  @Schema(required = true, description = "The seller's NewID")
  public String getSeller() {
    return seller;
  }
  public void setSeller(String seller) {
    this.seller = seller;
  }
  public PayCacheRequest customer(String customer) {
    this.customer = customer;
    return this;
  }

  

  /**
  * The customer&#x27;s NewID
  * @return customer
  **/
  @Schema(required = true, description = "The customer's NewID")
  public String getCustomer() {
    return customer;
  }
  public void setCustomer(String customer) {
    this.customer = customer;
  }
  public PayCacheRequest broker(String broker) {
    this.broker = broker;
    return this;
  }

  

  /**
  * The broker&#x27;s NewID. optional.
  * @return broker
  **/
  @Schema(description = "The broker's NewID. optional.")
  public String getBroker() {
    return broker;
  }
  public void setBroker(String broker) {
    this.broker = broker;
  }
  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    PayCacheRequest payCacheRequest = (PayCacheRequest) o;
    return Objects.equals(this.dappKey, payCacheRequest.dappKey) &&
        Objects.equals(this.protocol, payCacheRequest.protocol) &&
        Objects.equals(this.version, payCacheRequest.version) &&
        Objects.equals(this.ts, payCacheRequest.ts) &&
        Objects.equals(this.nonce, payCacheRequest.nonce) &&
        Objects.equals(this.os, payCacheRequest.os) &&
        Objects.equals(this.language, payCacheRequest.language) &&
        Objects.equals(this.md5, payCacheRequest.md5) &&
        Objects.equals(this.signType, payCacheRequest.signType) &&
        Objects.equals(this.signature, payCacheRequest.signature) &&
        Objects.equals(this.uuid, payCacheRequest.uuid) &&
        Objects.equals(this.dappId, payCacheRequest.dappId) &&
        Objects.equals(this.action, payCacheRequest.action) &&
        Objects.equals(this.expired, payCacheRequest.expired) &&
        Objects.equals(this.description, payCacheRequest.description) &&
        Objects.equals(this.priceCurrency, payCacheRequest.priceCurrency) &&
        Objects.equals(this.totalPrice, payCacheRequest.totalPrice) &&
        Objects.equals(this.orderNumber, payCacheRequest.orderNumber) &&
        Objects.equals(this.seller, payCacheRequest.seller) &&
        Objects.equals(this.customer, payCacheRequest.customer) &&
        Objects.equals(this.broker, payCacheRequest.broker);
  }

  @Override
  public int hashCode() {
    return java.util.Objects.hash(dappKey, protocol, version, ts, nonce, os, language, md5, signType, signature, uuid, dappId, action, expired, description, priceCurrency, totalPrice, orderNumber, seller, customer, broker);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class PayCacheRequest {\n");
    
    sb.append("    dappKey: ").append(toIndentedString(dappKey)).append("\n");
    sb.append("    protocol: ").append(toIndentedString(protocol)).append("\n");
    sb.append("    version: ").append(toIndentedString(version)).append("\n");
    sb.append("    ts: ").append(toIndentedString(ts)).append("\n");
    sb.append("    nonce: ").append(toIndentedString(nonce)).append("\n");
    sb.append("    os: ").append(toIndentedString(os)).append("\n");
    sb.append("    language: ").append(toIndentedString(language)).append("\n");
    sb.append("    md5: ").append(toIndentedString(md5)).append("\n");
    sb.append("    signType: ").append(toIndentedString(signType)).append("\n");
    sb.append("    signature: ").append(toIndentedString(signature)).append("\n");
    sb.append("    uuid: ").append(toIndentedString(uuid)).append("\n");
    sb.append("    dappId: ").append(toIndentedString(dappId)).append("\n");
    sb.append("    action: ").append(toIndentedString(action)).append("\n");
    sb.append("    expired: ").append(toIndentedString(expired)).append("\n");
    sb.append("    description: ").append(toIndentedString(description)).append("\n");
    sb.append("    priceCurrency: ").append(toIndentedString(priceCurrency)).append("\n");
    sb.append("    totalPrice: ").append(toIndentedString(totalPrice)).append("\n");
    sb.append("    orderNumber: ").append(toIndentedString(orderNumber)).append("\n");
    sb.append("    seller: ").append(toIndentedString(seller)).append("\n");
    sb.append("    customer: ").append(toIndentedString(customer)).append("\n");
    sb.append("    broker: ").append(toIndentedString(broker)).append("\n");
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
