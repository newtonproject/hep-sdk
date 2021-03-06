<?php
/**
 * Order
 *
 * PHP version 5
 *
 * @category Class
 * @package  HepRestApi
 * @author   Swagger Codegen team
 * @link     https://github.com/swagger-api/swagger-codegen
 */

/**
 * HEP REST API
 *
 * The REST API for HEP protocol
 *
 * OpenAPI spec version: v1
 * Contact: xiawu@zeuux.org
 * Generated by: https://github.com/swagger-api/swagger-codegen.git
 * Swagger Codegen version: 3.0.8
 */
/**
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen
 * Do not edit the class manually.
 */

namespace HepRestApi\Model;

use \ArrayAccess;
use \HepRestApi\ObjectSerializer;

/**
 * Order Class Doc Comment
 *
 * @category Class
 * @package  HepRestApi
 * @author   Swagger Codegen team
 * @link     https://github.com/swagger-api/swagger-codegen
 */
class Order implements ModelInterface, ArrayAccess
{
    const DISCRIMINATOR = null;

    /**
      * The original name of the model.
      *
      * @var string
      */
    protected static $swaggerModelName = 'Order';

    /**
      * Array of property to type mappings. Used for (de)serialization
      *
      * @var string[]
      */
    protected static $swaggerTypes = [
        'proof_type' => 'string',
'description' => 'string',
'price_currency' => 'string',
'total_price' => 'string',
'order_number' => 'string',
'seller' => 'string',
'customer' => 'string',
'broker' => 'string',
'order_items' => '\HepRestApi\Model\OrderItem[]',
'chain_txid' => 'string'    ];

    /**
      * Array of property to format mappings. Used for (de)serialization
      *
      * @var string[]
      */
    protected static $swaggerFormats = [
        'proof_type' => null,
'description' => null,
'price_currency' => null,
'total_price' => null,
'order_number' => null,
'seller' => null,
'customer' => null,
'broker' => null,
'order_items' => null,
'chain_txid' => null    ];

    /**
     * Array of property to type mappings. Used for (de)serialization
     *
     * @return array
     */
    public static function swaggerTypes()
    {
        return self::$swaggerTypes;
    }

    /**
     * Array of property to format mappings. Used for (de)serialization
     *
     * @return array
     */
    public static function swaggerFormats()
    {
        return self::$swaggerFormats;
    }

    /**
     * Array of attributes where the key is the local name,
     * and the value is the original name
     *
     * @var string[]
     */
    protected static $attributeMap = [
        'proof_type' => 'proof_type',
'description' => 'description',
'price_currency' => 'price_currency',
'total_price' => 'total_price',
'order_number' => 'order_number',
'seller' => 'seller',
'customer' => 'customer',
'broker' => 'broker',
'order_items' => 'order_items',
'chain_txid' => 'chain_txid'    ];

    /**
     * Array of attributes to setter functions (for deserialization of responses)
     *
     * @var string[]
     */
    protected static $setters = [
        'proof_type' => 'setProofType',
'description' => 'setDescription',
'price_currency' => 'setPriceCurrency',
'total_price' => 'setTotalPrice',
'order_number' => 'setOrderNumber',
'seller' => 'setSeller',
'customer' => 'setCustomer',
'broker' => 'setBroker',
'order_items' => 'setOrderItems',
'chain_txid' => 'setChainTxid'    ];

    /**
     * Array of attributes to getter functions (for serialization of requests)
     *
     * @var string[]
     */
    protected static $getters = [
        'proof_type' => 'getProofType',
'description' => 'getDescription',
'price_currency' => 'getPriceCurrency',
'total_price' => 'getTotalPrice',
'order_number' => 'getOrderNumber',
'seller' => 'getSeller',
'customer' => 'getCustomer',
'broker' => 'getBroker',
'order_items' => 'getOrderItems',
'chain_txid' => 'getChainTxid'    ];

    /**
     * Array of attributes where the key is the local name,
     * and the value is the original name
     *
     * @return array
     */
    public static function attributeMap()
    {
        return self::$attributeMap;
    }

    /**
     * Array of attributes to setter functions (for deserialization of responses)
     *
     * @return array
     */
    public static function setters()
    {
        return self::$setters;
    }

    /**
     * Array of attributes to getter functions (for serialization of requests)
     *
     * @return array
     */
    public static function getters()
    {
        return self::$getters;
    }

    /**
     * The original name of the model.
     *
     * @return string
     */
    public function getModelName()
    {
        return self::$swaggerModelName;
    }

    

    /**
     * Associative array for storing property values
     *
     * @var mixed[]
     */
    protected $container = [];

    /**
     * Constructor
     *
     * @param mixed[] $data Associated array of property values
     *                      initializing the model
     */
    public function __construct(array $data = null)
    {
        $this->container['proof_type'] = isset($data['proof_type']) ? $data['proof_type'] : null;
        $this->container['description'] = isset($data['description']) ? $data['description'] : null;
        $this->container['price_currency'] = isset($data['price_currency']) ? $data['price_currency'] : null;
        $this->container['total_price'] = isset($data['total_price']) ? $data['total_price'] : null;
        $this->container['order_number'] = isset($data['order_number']) ? $data['order_number'] : null;
        $this->container['seller'] = isset($data['seller']) ? $data['seller'] : null;
        $this->container['customer'] = isset($data['customer']) ? $data['customer'] : null;
        $this->container['broker'] = isset($data['broker']) ? $data['broker'] : null;
        $this->container['order_items'] = isset($data['order_items']) ? $data['order_items'] : null;
        $this->container['chain_txid'] = isset($data['chain_txid']) ? $data['chain_txid'] : null;
    }

    /**
     * Show all the invalid properties with reasons.
     *
     * @return array invalid properties with reasons
     */
    public function listInvalidProperties()
    {
        $invalidProperties = [];

        if ($this->container['proof_type'] === null) {
            $invalidProperties[] = "'proof_type' can't be null";
        }
        if ($this->container['description'] === null) {
            $invalidProperties[] = "'description' can't be null";
        }
        if ($this->container['price_currency'] === null) {
            $invalidProperties[] = "'price_currency' can't be null";
        }
        if ($this->container['total_price'] === null) {
            $invalidProperties[] = "'total_price' can't be null";
        }
        if ($this->container['order_number'] === null) {
            $invalidProperties[] = "'order_number' can't be null";
        }
        if ($this->container['seller'] === null) {
            $invalidProperties[] = "'seller' can't be null";
        }
        if ($this->container['customer'] === null) {
            $invalidProperties[] = "'customer' can't be null";
        }
        if ($this->container['broker'] === null) {
            $invalidProperties[] = "'broker' can't be null";
        }
        if ($this->container['order_items'] === null) {
            $invalidProperties[] = "'order_items' can't be null";
        }
        return $invalidProperties;
    }

    /**
     * Validate all the properties in the model
     * return true if all passed
     *
     * @return bool True if all properties are valid
     */
    public function valid()
    {
        return count($this->listInvalidProperties()) === 0;
    }


    /**
     * Gets proof_type
     *
     * @return string
     */
    public function getProofType()
    {
        return $this->container['proof_type'];
    }

    /**
     * Sets proof_type
     *
     * @param string $proof_type The proof type which value is 'order'.
     *
     * @return $this
     */
    public function setProofType($proof_type)
    {
        $this->container['proof_type'] = $proof_type;

        return $this;
    }

    /**
     * Gets description
     *
     * @return string
     */
    public function getDescription()
    {
        return $this->container['description'];
    }

    /**
     * Sets description
     *
     * @param string $description The order description
     *
     * @return $this
     */
    public function setDescription($description)
    {
        $this->container['description'] = $description;

        return $this;
    }

    /**
     * Gets price_currency
     *
     * @return string
     */
    public function getPriceCurrency()
    {
        return $this->container['price_currency'];
    }

    /**
     * Sets price_currency
     *
     * @param string $price_currency The symbol of fiat or digital token, such as USD, RMB, NEW,BTC,ETH.
     *
     * @return $this
     */
    public function setPriceCurrency($price_currency)
    {
        $this->container['price_currency'] = $price_currency;

        return $this;
    }

    /**
     * Gets total_price
     *
     * @return string
     */
    public function getTotalPrice()
    {
        return $this->container['total_price'];
    }

    /**
     * Sets total_price
     *
     * @param string $total_price The amount of fiat or digital token, unit is the minimum unit of given fiat or digital token.
     *
     * @return $this
     */
    public function setTotalPrice($total_price)
    {
        $this->container['total_price'] = $total_price;

        return $this;
    }

    /**
     * Gets order_number
     *
     * @return string
     */
    public function getOrderNumber()
    {
        return $this->container['order_number'];
    }

    /**
     * Sets order_number
     *
     * @param string $order_number The order number
     *
     * @return $this
     */
    public function setOrderNumber($order_number)
    {
        $this->container['order_number'] = $order_number;

        return $this;
    }

    /**
     * Gets seller
     *
     * @return string
     */
    public function getSeller()
    {
        return $this->container['seller'];
    }

    /**
     * Sets seller
     *
     * @param string $seller The seller's NewID
     *
     * @return $this
     */
    public function setSeller($seller)
    {
        $this->container['seller'] = $seller;

        return $this;
    }

    /**
     * Gets customer
     *
     * @return string
     */
    public function getCustomer()
    {
        return $this->container['customer'];
    }

    /**
     * Sets customer
     *
     * @param string $customer The customer's NewID
     *
     * @return $this
     */
    public function setCustomer($customer)
    {
        $this->container['customer'] = $customer;

        return $this;
    }

    /**
     * Gets broker
     *
     * @return string
     */
    public function getBroker()
    {
        return $this->container['broker'];
    }

    /**
     * Sets broker
     *
     * @param string $broker The broker's NewID. optional.
     *
     * @return $this
     */
    public function setBroker($broker)
    {
        $this->container['broker'] = $broker;

        return $this;
    }

    /**
     * Gets order_items
     *
     * @return \HepRestApi\Model\OrderItem[]
     */
    public function getOrderItems()
    {
        return $this->container['order_items'];
    }

    /**
     * Sets order_items
     *
     * @param \HepRestApi\Model\OrderItem[] $order_items order_items
     *
     * @return $this
     */
    public function setOrderItems($order_items)
    {
        $this->container['order_items'] = $order_items;

        return $this;
    }

    /**
     * Gets chain_txid
     *
     * @return string
     */
    public function getChainTxid()
    {
        return $this->container['chain_txid'];
    }

    /**
     * Sets chain_txid
     *
     * @param string $chain_txid The seller's NewID
     *
     * @return $this
     */
    public function setChainTxid($chain_txid)
    {
        $this->container['chain_txid'] = $chain_txid;

        return $this;
    }
    /**
     * Returns true if offset exists. False otherwise.
     *
     * @param integer $offset Offset
     *
     * @return boolean
     */
    public function offsetExists($offset)
    {
        return isset($this->container[$offset]);
    }

    /**
     * Gets offset.
     *
     * @param integer $offset Offset
     *
     * @return mixed
     */
    public function offsetGet($offset)
    {
        return isset($this->container[$offset]) ? $this->container[$offset] : null;
    }

    /**
     * Sets value based on offset.
     *
     * @param integer $offset Offset
     * @param mixed   $value  Value to be set
     *
     * @return void
     */
    public function offsetSet($offset, $value)
    {
        if (is_null($offset)) {
            $this->container[] = $value;
        } else {
            $this->container[$offset] = $value;
        }
    }

    /**
     * Unsets offset.
     *
     * @param integer $offset Offset
     *
     * @return void
     */
    public function offsetUnset($offset)
    {
        unset($this->container[$offset]);
    }

    /**
     * Gets the string presentation of the object
     *
     * @return string
     */
    public function __toString()
    {
        if (defined('JSON_PRETTY_PRINT')) { // use JSON pretty print
            return json_encode(
                ObjectSerializer::sanitizeForSerialization($this),
                JSON_PRETTY_PRINT
            );
        }

        return json_encode(ObjectSerializer::sanitizeForSerialization($this));
    }
}
