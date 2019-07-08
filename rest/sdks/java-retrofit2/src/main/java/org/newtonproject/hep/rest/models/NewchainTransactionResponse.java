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
 * NewchainTransactionResponse
 */
@javax.annotation.Generated(value = "io.swagger.codegen.languages.JavaClientCodegen", date = "2019-06-30T20:36:48.159+08:00")
public class NewchainTransactionResponse {
  @SerializedName("txid")
  private String txid = null;

  @SerializedName("order_number")
  private String orderNumber = null;

  @SerializedName("from_address")
  private String fromAddress = null;

  @SerializedName("to_address")
  private String toAddress = null;

  @SerializedName("value")
  private String value = null;

  @SerializedName("block_height")
  private Integer blockHeight = null;

  @SerializedName("status")
  private Integer status = null;

  public NewchainTransactionResponse txid(String txid) {
    this.txid = txid;
    return this;
  }

   /**
   * The transaction ID
   * @return txid
  **/
  @ApiModelProperty(required = true, value = "The transaction ID")
  public String getTxid() {
    return txid;
  }

  public void setTxid(String txid) {
    this.txid = txid;
  }

  public NewchainTransactionResponse orderNumber(String orderNumber) {
    this.orderNumber = orderNumber;
    return this;
  }

   /**
   * The order number
   * @return orderNumber
  **/
  @ApiModelProperty(required = true, value = "The order number")
  public String getOrderNumber() {
    return orderNumber;
  }

  public void setOrderNumber(String orderNumber) {
    this.orderNumber = orderNumber;
  }

  public NewchainTransactionResponse fromAddress(String fromAddress) {
    this.fromAddress = fromAddress;
    return this;
  }

   /**
   * The from address
   * @return fromAddress
  **/
  @ApiModelProperty(required = true, value = "The from address")
  public String getFromAddress() {
    return fromAddress;
  }

  public void setFromAddress(String fromAddress) {
    this.fromAddress = fromAddress;
  }

  public NewchainTransactionResponse toAddress(String toAddress) {
    this.toAddress = toAddress;
    return this;
  }

   /**
   * The from address
   * @return toAddress
  **/
  @ApiModelProperty(required = true, value = "The from address")
  public String getToAddress() {
    return toAddress;
  }

  public void setToAddress(String toAddress) {
    this.toAddress = toAddress;
  }

  public NewchainTransactionResponse value(String value) {
    this.value = value;
    return this;
  }

   /**
   * The transfer amount
   * @return value
  **/
  @ApiModelProperty(required = true, value = "The transfer amount")
  public String getValue() {
    return value;
  }

  public void setValue(String value) {
    this.value = value;
  }

  public NewchainTransactionResponse blockHeight(Integer blockHeight) {
    this.blockHeight = blockHeight;
    return this;
  }

   /**
   * The block height
   * @return blockHeight
  **/
  @ApiModelProperty(required = true, value = "The block height")
  public Integer getBlockHeight() {
    return blockHeight;
  }

  public void setBlockHeight(Integer blockHeight) {
    this.blockHeight = blockHeight;
  }

  public NewchainTransactionResponse status(Integer status) {
    this.status = status;
    return this;
  }

   /**
   * The status of transaction
   * @return status
  **/
  @ApiModelProperty(required = true, value = "The status of transaction")
  public Integer getStatus() {
    return status;
  }

  public void setStatus(Integer status) {
    this.status = status;
  }


  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    NewchainTransactionResponse newchainTransactionResponse = (NewchainTransactionResponse) o;
    return Objects.equals(this.txid, newchainTransactionResponse.txid) &&
        Objects.equals(this.orderNumber, newchainTransactionResponse.orderNumber) &&
        Objects.equals(this.fromAddress, newchainTransactionResponse.fromAddress) &&
        Objects.equals(this.toAddress, newchainTransactionResponse.toAddress) &&
        Objects.equals(this.value, newchainTransactionResponse.value) &&
        Objects.equals(this.blockHeight, newchainTransactionResponse.blockHeight) &&
        Objects.equals(this.status, newchainTransactionResponse.status);
  }

  @Override
  public int hashCode() {
    return Objects.hash(txid, orderNumber, fromAddress, toAddress, value, blockHeight, status);
  }


  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class NewchainTransactionResponse {\n");
    
    sb.append("    txid: ").append(toIndentedString(txid)).append("\n");
    sb.append("    orderNumber: ").append(toIndentedString(orderNumber)).append("\n");
    sb.append("    fromAddress: ").append(toIndentedString(fromAddress)).append("\n");
    sb.append("    toAddress: ").append(toIndentedString(toAddress)).append("\n");
    sb.append("    value: ").append(toIndentedString(value)).append("\n");
    sb.append("    blockHeight: ").append(toIndentedString(blockHeight)).append("\n");
    sb.append("    status: ").append(toIndentedString(status)).append("\n");
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
