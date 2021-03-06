<?php
/**
 * Dapp
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
 * Dapp Class Doc Comment
 *
 * @category Class
 * @package  HepRestApi
 * @author   Swagger Codegen team
 * @link     https://github.com/swagger-api/swagger-codegen
 */
class Dapp implements ModelInterface, ArrayAccess
{
    const DISCRIMINATOR = null;

    /**
      * The original name of the model.
      *
      * @var string
      */
    protected static $swaggerModelName = 'Dapp';

    /**
      * Array of property to type mappings. Used for (de)serialization
      *
      * @var string[]
      */
    protected static $swaggerTypes = [
        'dapp_id' => 'string',
'dapp_name' => 'string',
'icon' => 'string',
'dapp_public_key' => 'string',
'package_name' => 'string',
'bundle_id' => 'string',
'schema' => 'string',
'website' => 'string',
'download_url' => 'string',
'deposit_contract_address' => 'string',
'dapp_type_id' => 'int',
'dapp_category_id' => 'int',
'auth_login_callback' => 'string',
'pay_order_callback' => 'string',
'proof_submit_callback' => 'string'    ];

    /**
      * Array of property to format mappings. Used for (de)serialization
      *
      * @var string[]
      */
    protected static $swaggerFormats = [
        'dapp_id' => null,
'dapp_name' => null,
'icon' => null,
'dapp_public_key' => null,
'package_name' => null,
'bundle_id' => null,
'schema' => null,
'website' => null,
'download_url' => null,
'deposit_contract_address' => null,
'dapp_type_id' => null,
'dapp_category_id' => null,
'auth_login_callback' => null,
'pay_order_callback' => null,
'proof_submit_callback' => null    ];

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
        'dapp_id' => 'dapp_id',
'dapp_name' => 'dapp_name',
'icon' => 'icon',
'dapp_public_key' => 'dapp_public_key',
'package_name' => 'package_name',
'bundle_id' => 'bundle_id',
'schema' => 'schema',
'website' => 'website',
'download_url' => 'download_url',
'deposit_contract_address' => 'deposit_contract_address',
'dapp_type_id' => 'dapp_type_id',
'dapp_category_id' => 'dapp_category_id',
'auth_login_callback' => 'auth_login_callback',
'pay_order_callback' => 'pay_order_callback',
'proof_submit_callback' => 'proof_submit_callback'    ];

    /**
     * Array of attributes to setter functions (for deserialization of responses)
     *
     * @var string[]
     */
    protected static $setters = [
        'dapp_id' => 'setDappId',
'dapp_name' => 'setDappName',
'icon' => 'setIcon',
'dapp_public_key' => 'setDappPublicKey',
'package_name' => 'setPackageName',
'bundle_id' => 'setBundleId',
'schema' => 'setSchema',
'website' => 'setWebsite',
'download_url' => 'setDownloadUrl',
'deposit_contract_address' => 'setDepositContractAddress',
'dapp_type_id' => 'setDappTypeId',
'dapp_category_id' => 'setDappCategoryId',
'auth_login_callback' => 'setAuthLoginCallback',
'pay_order_callback' => 'setPayOrderCallback',
'proof_submit_callback' => 'setProofSubmitCallback'    ];

    /**
     * Array of attributes to getter functions (for serialization of requests)
     *
     * @var string[]
     */
    protected static $getters = [
        'dapp_id' => 'getDappId',
'dapp_name' => 'getDappName',
'icon' => 'getIcon',
'dapp_public_key' => 'getDappPublicKey',
'package_name' => 'getPackageName',
'bundle_id' => 'getBundleId',
'schema' => 'getSchema',
'website' => 'getWebsite',
'download_url' => 'getDownloadUrl',
'deposit_contract_address' => 'getDepositContractAddress',
'dapp_type_id' => 'getDappTypeId',
'dapp_category_id' => 'getDappCategoryId',
'auth_login_callback' => 'getAuthLoginCallback',
'pay_order_callback' => 'getPayOrderCallback',
'proof_submit_callback' => 'getProofSubmitCallback'    ];

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
        $this->container['dapp_id'] = isset($data['dapp_id']) ? $data['dapp_id'] : null;
        $this->container['dapp_name'] = isset($data['dapp_name']) ? $data['dapp_name'] : null;
        $this->container['icon'] = isset($data['icon']) ? $data['icon'] : null;
        $this->container['dapp_public_key'] = isset($data['dapp_public_key']) ? $data['dapp_public_key'] : null;
        $this->container['package_name'] = isset($data['package_name']) ? $data['package_name'] : null;
        $this->container['bundle_id'] = isset($data['bundle_id']) ? $data['bundle_id'] : null;
        $this->container['schema'] = isset($data['schema']) ? $data['schema'] : null;
        $this->container['website'] = isset($data['website']) ? $data['website'] : null;
        $this->container['download_url'] = isset($data['download_url']) ? $data['download_url'] : null;
        $this->container['deposit_contract_address'] = isset($data['deposit_contract_address']) ? $data['deposit_contract_address'] : null;
        $this->container['dapp_type_id'] = isset($data['dapp_type_id']) ? $data['dapp_type_id'] : null;
        $this->container['dapp_category_id'] = isset($data['dapp_category_id']) ? $data['dapp_category_id'] : null;
        $this->container['auth_login_callback'] = isset($data['auth_login_callback']) ? $data['auth_login_callback'] : null;
        $this->container['pay_order_callback'] = isset($data['pay_order_callback']) ? $data['pay_order_callback'] : null;
        $this->container['proof_submit_callback'] = isset($data['proof_submit_callback']) ? $data['proof_submit_callback'] : null;
    }

    /**
     * Show all the invalid properties with reasons.
     *
     * @return array invalid properties with reasons
     */
    public function listInvalidProperties()
    {
        $invalidProperties = [];

        if ($this->container['dapp_id'] === null) {
            $invalidProperties[] = "'dapp_id' can't be null";
        }
        if ($this->container['dapp_name'] === null) {
            $invalidProperties[] = "'dapp_name' can't be null";
        }
        if ($this->container['icon'] === null) {
            $invalidProperties[] = "'icon' can't be null";
        }
        if ($this->container['dapp_public_key'] === null) {
            $invalidProperties[] = "'dapp_public_key' can't be null";
        }
        if ($this->container['package_name'] === null) {
            $invalidProperties[] = "'package_name' can't be null";
        }
        if ($this->container['bundle_id'] === null) {
            $invalidProperties[] = "'bundle_id' can't be null";
        }
        if ($this->container['schema'] === null) {
            $invalidProperties[] = "'schema' can't be null";
        }
        if ($this->container['website'] === null) {
            $invalidProperties[] = "'website' can't be null";
        }
        if ($this->container['download_url'] === null) {
            $invalidProperties[] = "'download_url' can't be null";
        }
        if ($this->container['deposit_contract_address'] === null) {
            $invalidProperties[] = "'deposit_contract_address' can't be null";
        }
        if ($this->container['dapp_type_id'] === null) {
            $invalidProperties[] = "'dapp_type_id' can't be null";
        }
        if ($this->container['dapp_category_id'] === null) {
            $invalidProperties[] = "'dapp_category_id' can't be null";
        }
        if ($this->container['auth_login_callback'] === null) {
            $invalidProperties[] = "'auth_login_callback' can't be null";
        }
        if ($this->container['pay_order_callback'] === null) {
            $invalidProperties[] = "'pay_order_callback' can't be null";
        }
        if ($this->container['proof_submit_callback'] === null) {
            $invalidProperties[] = "'proof_submit_callback' can't be null";
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
     * Gets dapp_id
     *
     * @return string
     */
    public function getDappId()
    {
        return $this->container['dapp_id'];
    }

    /**
     * Sets dapp_id
     *
     * @param string $dapp_id The decentralized application ID
     *
     * @return $this
     */
    public function setDappId($dapp_id)
    {
        $this->container['dapp_id'] = $dapp_id;

        return $this;
    }

    /**
     * Gets dapp_name
     *
     * @return string
     */
    public function getDappName()
    {
        return $this->container['dapp_name'];
    }

    /**
     * Sets dapp_name
     *
     * @param string $dapp_name The decentralized application name
     *
     * @return $this
     */
    public function setDappName($dapp_name)
    {
        $this->container['dapp_name'] = $dapp_name;

        return $this;
    }

    /**
     * Gets icon
     *
     * @return string
     */
    public function getIcon()
    {
        return $this->container['icon'];
    }

    /**
     * Sets icon
     *
     * @param string $icon The icon of application
     *
     * @return $this
     */
    public function setIcon($icon)
    {
        $this->container['icon'] = $icon;

        return $this;
    }

    /**
     * Gets dapp_public_key
     *
     * @return string
     */
    public function getDappPublicKey()
    {
        return $this->container['dapp_public_key'];
    }

    /**
     * Sets dapp_public_key
     *
     * @param string $dapp_public_key The public key of DApp
     *
     * @return $this
     */
    public function setDappPublicKey($dapp_public_key)
    {
        $this->container['dapp_public_key'] = $dapp_public_key;

        return $this;
    }

    /**
     * Gets package_name
     *
     * @return string
     */
    public function getPackageName()
    {
        return $this->container['package_name'];
    }

    /**
     * Sets package_name
     *
     * @param string $package_name The package name such as com.demo.dev.android
     *
     * @return $this
     */
    public function setPackageName($package_name)
    {
        $this->container['package_name'] = $package_name;

        return $this;
    }

    /**
     * Gets bundle_id
     *
     * @return string
     */
    public function getBundleId()
    {
        return $this->container['bundle_id'];
    }

    /**
     * Sets bundle_id
     *
     * @param string $bundle_id The bundle id such as com.demo.dev.ios for iOS platform
     *
     * @return $this
     */
    public function setBundleId($bundle_id)
    {
        $this->container['bundle_id'] = $bundle_id;

        return $this;
    }

    /**
     * Gets schema
     *
     * @return string
     */
    public function getSchema()
    {
        return $this->container['schema'];
    }

    /**
     * Sets schema
     *
     * @param string $schema The routing schema
     *
     * @return $this
     */
    public function setSchema($schema)
    {
        $this->container['schema'] = $schema;

        return $this;
    }

    /**
     * Gets website
     *
     * @return string
     */
    public function getWebsite()
    {
        return $this->container['website'];
    }

    /**
     * Sets website
     *
     * @param string $website The dapp website link
     *
     * @return $this
     */
    public function setWebsite($website)
    {
        $this->container['website'] = $website;

        return $this;
    }

    /**
     * Gets download_url
     *
     * @return string
     */
    public function getDownloadUrl()
    {
        return $this->container['download_url'];
    }

    /**
     * Sets download_url
     *
     * @param string $download_url The dapp download link
     *
     * @return $this
     */
    public function setDownloadUrl($download_url)
    {
        $this->container['download_url'] = $download_url;

        return $this;
    }

    /**
     * Gets deposit_contract_address
     *
     * @return string
     */
    public function getDepositContractAddress()
    {
        return $this->container['deposit_contract_address'];
    }

    /**
     * Sets deposit_contract_address
     *
     * @param string $deposit_contract_address The deposit contract Address, the example is NEW182....
     *
     * @return $this
     */
    public function setDepositContractAddress($deposit_contract_address)
    {
        $this->container['deposit_contract_address'] = $deposit_contract_address;

        return $this;
    }

    /**
     * Gets dapp_type_id
     *
     * @return int
     */
    public function getDappTypeId()
    {
        return $this->container['dapp_type_id'];
    }

    /**
     * Sets dapp_type_id
     *
     * @param int $dapp_type_id The dapp type ID.
     *
     * @return $this
     */
    public function setDappTypeId($dapp_type_id)
    {
        $this->container['dapp_type_id'] = $dapp_type_id;

        return $this;
    }

    /**
     * Gets dapp_category_id
     *
     * @return int
     */
    public function getDappCategoryId()
    {
        return $this->container['dapp_category_id'];
    }

    /**
     * Sets dapp_category_id
     *
     * @param int $dapp_category_id The dapp category ID.
     *
     * @return $this
     */
    public function setDappCategoryId($dapp_category_id)
    {
        $this->container['dapp_category_id'] = $dapp_category_id;

        return $this;
    }

    /**
     * Gets auth_login_callback
     *
     * @return string
     */
    public function getAuthLoginCallback()
    {
        return $this->container['auth_login_callback'];
    }

    /**
     * Sets auth_login_callback
     *
     * @param string $auth_login_callback For Mobile Native DApp, it is redirect schema; For website DApp, it is callback url; For  NewDApp, it is HEP-based url.
     *
     * @return $this
     */
    public function setAuthLoginCallback($auth_login_callback)
    {
        $this->container['auth_login_callback'] = $auth_login_callback;

        return $this;
    }

    /**
     * Gets pay_order_callback
     *
     * @return string
     */
    public function getPayOrderCallback()
    {
        return $this->container['pay_order_callback'];
    }

    /**
     * Sets pay_order_callback
     *
     * @param string $pay_order_callback For Mobile Native DApp, it is redirect schema; For website DApp, it is callback url; For  NewDApp, it is HEP-based url.
     *
     * @return $this
     */
    public function setPayOrderCallback($pay_order_callback)
    {
        $this->container['pay_order_callback'] = $pay_order_callback;

        return $this;
    }

    /**
     * Gets proof_submit_callback
     *
     * @return string
     */
    public function getProofSubmitCallback()
    {
        return $this->container['proof_submit_callback'];
    }

    /**
     * Sets proof_submit_callback
     *
     * @param string $proof_submit_callback For Mobile Native DApp, it is redirect schema; For website DApp, it is callback url; For  NewDApp, it is HEP-based url.
     *
     * @return $this
     */
    public function setProofSubmitCallback($proof_submit_callback)
    {
        $this->container['proof_submit_callback'] = $proof_submit_callback;

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
