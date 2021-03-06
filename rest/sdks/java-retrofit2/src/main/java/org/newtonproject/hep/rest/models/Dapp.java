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


package org.newtonproject.hep.rest.models;

import java.util.Objects;
import java.util.Arrays;
import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import java.io.IOException;

/**
 * Dapp
 */
@javax.annotation.Generated(value = "io.swagger.codegen.languages.JavaClientCodegen", date = "2019-06-30T20:36:48.159+08:00")
public class Dapp {
  @SerializedName("dapp_id")
  private String dappId = null;

  @SerializedName("dapp_name")
  private String dappName = null;

  @SerializedName("icon")
  private String icon = null;

  @SerializedName("dapp_public_key")
  private String dappPublicKey = null;

  @SerializedName("package_name")
  private String packageName = null;

  @SerializedName("bundle_id")
  private String bundleId = null;

  @SerializedName("schema")
  private String schema = null;

  @SerializedName("website")
  private String website = null;

  @SerializedName("download_url")
  private String downloadUrl = null;

  @SerializedName("deposit_contract_address")
  private String depositContractAddress = null;

  @SerializedName("dapp_type_id")
  private Integer dappTypeId = null;

  @SerializedName("dapp_category_id")
  private Integer dappCategoryId = null;

  @SerializedName("auth_login_callback")
  private String authLoginCallback = null;

  @SerializedName("pay_order_callback")
  private String payOrderCallback = null;

  @SerializedName("proof_submit_callback")
  private String proofSubmitCallback = null;

  public Dapp dappId(String dappId) {
    this.dappId = dappId;
    return this;
  }

   /**
   * The decentralized application ID
   * @return dappId
  **/
  @ApiModelProperty(required = true, value = "The decentralized application ID")
  public String getDappId() {
    return dappId;
  }

  public void setDappId(String dappId) {
    this.dappId = dappId;
  }

  public Dapp dappName(String dappName) {
    this.dappName = dappName;
    return this;
  }

   /**
   * The decentralized application name
   * @return dappName
  **/
  @ApiModelProperty(required = true, value = "The decentralized application name")
  public String getDappName() {
    return dappName;
  }

  public void setDappName(String dappName) {
    this.dappName = dappName;
  }

  public Dapp icon(String icon) {
    this.icon = icon;
    return this;
  }

   /**
   * The icon of application
   * @return icon
  **/
  @ApiModelProperty(required = true, value = "The icon of application")
  public String getIcon() {
    return icon;
  }

  public void setIcon(String icon) {
    this.icon = icon;
  }

  public Dapp dappPublicKey(String dappPublicKey) {
    this.dappPublicKey = dappPublicKey;
    return this;
  }

   /**
   * The public key of DApp
   * @return dappPublicKey
  **/
  @ApiModelProperty(required = true, value = "The public key of DApp")
  public String getDappPublicKey() {
    return dappPublicKey;
  }

  public void setDappPublicKey(String dappPublicKey) {
    this.dappPublicKey = dappPublicKey;
  }

  public Dapp packageName(String packageName) {
    this.packageName = packageName;
    return this;
  }

   /**
   * The package name such as com.demo.dev.android
   * @return packageName
  **/
  @ApiModelProperty(required = true, value = "The package name such as com.demo.dev.android")
  public String getPackageName() {
    return packageName;
  }

  public void setPackageName(String packageName) {
    this.packageName = packageName;
  }

  public Dapp bundleId(String bundleId) {
    this.bundleId = bundleId;
    return this;
  }

   /**
   * The bundle id such as com.demo.dev.ios for iOS platform
   * @return bundleId
  **/
  @ApiModelProperty(required = true, value = "The bundle id such as com.demo.dev.ios for iOS platform")
  public String getBundleId() {
    return bundleId;
  }

  public void setBundleId(String bundleId) {
    this.bundleId = bundleId;
  }

  public Dapp schema(String schema) {
    this.schema = schema;
    return this;
  }

   /**
   * The routing schema
   * @return schema
  **/
  @ApiModelProperty(required = true, value = "The routing schema")
  public String getSchema() {
    return schema;
  }

  public void setSchema(String schema) {
    this.schema = schema;
  }

  public Dapp website(String website) {
    this.website = website;
    return this;
  }

   /**
   * The dapp website link
   * @return website
  **/
  @ApiModelProperty(required = true, value = "The dapp website link")
  public String getWebsite() {
    return website;
  }

  public void setWebsite(String website) {
    this.website = website;
  }

  public Dapp downloadUrl(String downloadUrl) {
    this.downloadUrl = downloadUrl;
    return this;
  }

   /**
   * The dapp download link
   * @return downloadUrl
  **/
  @ApiModelProperty(required = true, value = "The dapp download link")
  public String getDownloadUrl() {
    return downloadUrl;
  }

  public void setDownloadUrl(String downloadUrl) {
    this.downloadUrl = downloadUrl;
  }

  public Dapp depositContractAddress(String depositContractAddress) {
    this.depositContractAddress = depositContractAddress;
    return this;
  }

   /**
   * The deposit contract Address, the example is NEW182....
   * @return depositContractAddress
  **/
  @ApiModelProperty(required = true, value = "The deposit contract Address, the example is NEW182....")
  public String getDepositContractAddress() {
    return depositContractAddress;
  }

  public void setDepositContractAddress(String depositContractAddress) {
    this.depositContractAddress = depositContractAddress;
  }

  public Dapp dappTypeId(Integer dappTypeId) {
    this.dappTypeId = dappTypeId;
    return this;
  }

   /**
   * The dapp type ID.
   * @return dappTypeId
  **/
  @ApiModelProperty(required = true, value = "The dapp type ID.")
  public Integer getDappTypeId() {
    return dappTypeId;
  }

  public void setDappTypeId(Integer dappTypeId) {
    this.dappTypeId = dappTypeId;
  }

  public Dapp dappCategoryId(Integer dappCategoryId) {
    this.dappCategoryId = dappCategoryId;
    return this;
  }

   /**
   * The dapp category ID.
   * @return dappCategoryId
  **/
  @ApiModelProperty(required = true, value = "The dapp category ID.")
  public Integer getDappCategoryId() {
    return dappCategoryId;
  }

  public void setDappCategoryId(Integer dappCategoryId) {
    this.dappCategoryId = dappCategoryId;
  }

  public Dapp authLoginCallback(String authLoginCallback) {
    this.authLoginCallback = authLoginCallback;
    return this;
  }

   /**
   * For Mobile Native DApp, it is redirect schema; For website DApp, it is callback url; For  NewDApp, it is HEP-based url.
   * @return authLoginCallback
  **/
  @ApiModelProperty(required = true, value = "For Mobile Native DApp, it is redirect schema; For website DApp, it is callback url; For  NewDApp, it is HEP-based url.")
  public String getAuthLoginCallback() {
    return authLoginCallback;
  }

  public void setAuthLoginCallback(String authLoginCallback) {
    this.authLoginCallback = authLoginCallback;
  }

  public Dapp payOrderCallback(String payOrderCallback) {
    this.payOrderCallback = payOrderCallback;
    return this;
  }

   /**
   * For Mobile Native DApp, it is redirect schema; For website DApp, it is callback url; For  NewDApp, it is HEP-based url.
   * @return payOrderCallback
  **/
  @ApiModelProperty(required = true, value = "For Mobile Native DApp, it is redirect schema; For website DApp, it is callback url; For  NewDApp, it is HEP-based url.")
  public String getPayOrderCallback() {
    return payOrderCallback;
  }

  public void setPayOrderCallback(String payOrderCallback) {
    this.payOrderCallback = payOrderCallback;
  }

  public Dapp proofSubmitCallback(String proofSubmitCallback) {
    this.proofSubmitCallback = proofSubmitCallback;
    return this;
  }

   /**
   * For Mobile Native DApp, it is redirect schema; For website DApp, it is callback url; For  NewDApp, it is HEP-based url.
   * @return proofSubmitCallback
  **/
  @ApiModelProperty(required = true, value = "For Mobile Native DApp, it is redirect schema; For website DApp, it is callback url; For  NewDApp, it is HEP-based url.")
  public String getProofSubmitCallback() {
    return proofSubmitCallback;
  }

  public void setProofSubmitCallback(String proofSubmitCallback) {
    this.proofSubmitCallback = proofSubmitCallback;
  }


  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Dapp dapp = (Dapp) o;
    return Objects.equals(this.dappId, dapp.dappId) &&
        Objects.equals(this.dappName, dapp.dappName) &&
        Objects.equals(this.icon, dapp.icon) &&
        Objects.equals(this.dappPublicKey, dapp.dappPublicKey) &&
        Objects.equals(this.packageName, dapp.packageName) &&
        Objects.equals(this.bundleId, dapp.bundleId) &&
        Objects.equals(this.schema, dapp.schema) &&
        Objects.equals(this.website, dapp.website) &&
        Objects.equals(this.downloadUrl, dapp.downloadUrl) &&
        Objects.equals(this.depositContractAddress, dapp.depositContractAddress) &&
        Objects.equals(this.dappTypeId, dapp.dappTypeId) &&
        Objects.equals(this.dappCategoryId, dapp.dappCategoryId) &&
        Objects.equals(this.authLoginCallback, dapp.authLoginCallback) &&
        Objects.equals(this.payOrderCallback, dapp.payOrderCallback) &&
        Objects.equals(this.proofSubmitCallback, dapp.proofSubmitCallback);
  }

  @Override
  public int hashCode() {
    return Objects.hash(dappId, dappName, icon, dappPublicKey, packageName, bundleId, schema, website, downloadUrl, depositContractAddress, dappTypeId, dappCategoryId, authLoginCallback, payOrderCallback, proofSubmitCallback);
  }


  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class Dapp {\n");
    
    sb.append("    dappId: ").append(toIndentedString(dappId)).append("\n");
    sb.append("    dappName: ").append(toIndentedString(dappName)).append("\n");
    sb.append("    icon: ").append(toIndentedString(icon)).append("\n");
    sb.append("    dappPublicKey: ").append(toIndentedString(dappPublicKey)).append("\n");
    sb.append("    packageName: ").append(toIndentedString(packageName)).append("\n");
    sb.append("    bundleId: ").append(toIndentedString(bundleId)).append("\n");
    sb.append("    schema: ").append(toIndentedString(schema)).append("\n");
    sb.append("    website: ").append(toIndentedString(website)).append("\n");
    sb.append("    downloadUrl: ").append(toIndentedString(downloadUrl)).append("\n");
    sb.append("    depositContractAddress: ").append(toIndentedString(depositContractAddress)).append("\n");
    sb.append("    dappTypeId: ").append(toIndentedString(dappTypeId)).append("\n");
    sb.append("    dappCategoryId: ").append(toIndentedString(dappCategoryId)).append("\n");
    sb.append("    authLoginCallback: ").append(toIndentedString(authLoginCallback)).append("\n");
    sb.append("    payOrderCallback: ").append(toIndentedString(payOrderCallback)).append("\n");
    sb.append("    proofSubmitCallback: ").append(toIndentedString(proofSubmitCallback)).append("\n");
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

