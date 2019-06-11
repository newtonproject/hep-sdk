<?php
/**
 * CreateProofRequest
 *
 * PHP version 5
 *
 * @category Class
 * @package  Swagger\Client
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

namespace Swagger\Client\Model;

use \ArrayAccess;
use \Swagger\Client\ObjectSerializer;

/**
 * CreateProofRequest Class Doc Comment
 *
 * @category Class
 * @package  Swagger\Client
 * @author   Swagger Codegen team
 * @link     https://github.com/swagger-api/swagger-codegen
 */
class CreateProofRequest implements ModelInterface, ArrayAccess
{
    const DISCRIMINATOR = null;

    /**
      * The original name of the model.
      *
      * @var string
      */
    protected static $swaggerModelName = 'CreateProofRequest';

    /**
      * Array of property to type mappings. Used for (de)serialization
      *
      * @var string[]
      */
    protected static $swaggerTypes = [
        'dapp_key' => 'string',
'protocol' => 'string',
'version' => 'string',
'ts' => 'int',
'nonce' => 'string',
'os' => 'string',
'language' => 'string',
'md5' => 'string',
'sign_type' => 'string',
'signature' => 'string',
'uuid' => 'string',
'dapp_id' => 'string',
'content' => '\Swagger\Client\Model\Order'    ];

    /**
      * Array of property to format mappings. Used for (de)serialization
      *
      * @var string[]
      */
    protected static $swaggerFormats = [
        'dapp_key' => null,
'protocol' => null,
'version' => null,
'ts' => null,
'nonce' => null,
'os' => null,
'language' => null,
'md5' => null,
'sign_type' => null,
'signature' => null,
'uuid' => null,
'dapp_id' => null,
'content' => null    ];

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
        'dapp_key' => 'dapp_key',
'protocol' => 'protocol',
'version' => 'version',
'ts' => 'ts',
'nonce' => 'nonce',
'os' => 'os',
'language' => 'language',
'md5' => 'md5',
'sign_type' => 'sign_type',
'signature' => 'signature',
'uuid' => 'uuid',
'dapp_id' => 'dapp_id',
'content' => 'content'    ];

    /**
     * Array of attributes to setter functions (for deserialization of responses)
     *
     * @var string[]
     */
    protected static $setters = [
        'dapp_key' => 'setDappKey',
'protocol' => 'setProtocol',
'version' => 'setVersion',
'ts' => 'setTs',
'nonce' => 'setNonce',
'os' => 'setOs',
'language' => 'setLanguage',
'md5' => 'setMd5',
'sign_type' => 'setSignType',
'signature' => 'setSignature',
'uuid' => 'setUuid',
'dapp_id' => 'setDappId',
'content' => 'setContent'    ];

    /**
     * Array of attributes to getter functions (for serialization of requests)
     *
     * @var string[]
     */
    protected static $getters = [
        'dapp_key' => 'getDappKey',
'protocol' => 'getProtocol',
'version' => 'getVersion',
'ts' => 'getTs',
'nonce' => 'getNonce',
'os' => 'getOs',
'language' => 'getLanguage',
'md5' => 'getMd5',
'sign_type' => 'getSignType',
'signature' => 'getSignature',
'uuid' => 'getUuid',
'dapp_id' => 'getDappId',
'content' => 'getContent'    ];

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
        $this->container['dapp_key'] = isset($data['dapp_key']) ? $data['dapp_key'] : null;
        $this->container['protocol'] = isset($data['protocol']) ? $data['protocol'] : null;
        $this->container['version'] = isset($data['version']) ? $data['version'] : null;
        $this->container['ts'] = isset($data['ts']) ? $data['ts'] : null;
        $this->container['nonce'] = isset($data['nonce']) ? $data['nonce'] : null;
        $this->container['os'] = isset($data['os']) ? $data['os'] : null;
        $this->container['language'] = isset($data['language']) ? $data['language'] : null;
        $this->container['md5'] = isset($data['md5']) ? $data['md5'] : null;
        $this->container['sign_type'] = isset($data['sign_type']) ? $data['sign_type'] : null;
        $this->container['signature'] = isset($data['signature']) ? $data['signature'] : null;
        $this->container['uuid'] = isset($data['uuid']) ? $data['uuid'] : null;
        $this->container['dapp_id'] = isset($data['dapp_id']) ? $data['dapp_id'] : null;
        $this->container['content'] = isset($data['content']) ? $data['content'] : null;
    }

    /**
     * Show all the invalid properties with reasons.
     *
     * @return array invalid properties with reasons
     */
    public function listInvalidProperties()
    {
        $invalidProperties = [];

        if ($this->container['dapp_key'] === null) {
            $invalidProperties[] = "'dapp_key' can't be null";
        }
        if ($this->container['protocol'] === null) {
            $invalidProperties[] = "'protocol' can't be null";
        }
        if ($this->container['version'] === null) {
            $invalidProperties[] = "'version' can't be null";
        }
        if ($this->container['ts'] === null) {
            $invalidProperties[] = "'ts' can't be null";
        }
        if ($this->container['nonce'] === null) {
            $invalidProperties[] = "'nonce' can't be null";
        }
        if ($this->container['os'] === null) {
            $invalidProperties[] = "'os' can't be null";
        }
        if ($this->container['language'] === null) {
            $invalidProperties[] = "'language' can't be null";
        }
        if ($this->container['md5'] === null) {
            $invalidProperties[] = "'md5' can't be null";
        }
        if ($this->container['sign_type'] === null) {
            $invalidProperties[] = "'sign_type' can't be null";
        }
        if ($this->container['signature'] === null) {
            $invalidProperties[] = "'signature' can't be null";
        }
        if ($this->container['uuid'] === null) {
            $invalidProperties[] = "'uuid' can't be null";
        }
        if ($this->container['dapp_id'] === null) {
            $invalidProperties[] = "'dapp_id' can't be null";
        }
        if ($this->container['content'] === null) {
            $invalidProperties[] = "'content' can't be null";
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
     * Gets dapp_key
     *
     * @return string
     */
    public function getDappKey()
    {
        return $this->container['dapp_key'];
    }

    /**
     * Sets dapp_key
     *
     * @param string $dapp_key The decentralized application access key
     *
     * @return $this
     */
    public function setDappKey($dapp_key)
    {
        $this->container['dapp_key'] = $dapp_key;

        return $this;
    }

    /**
     * Gets protocol
     *
     * @return string
     */
    public function getProtocol()
    {
        return $this->container['protocol'];
    }

    /**
     * Sets protocol
     *
     * @param string $protocol The protocol name. default is 'HEP'.
     *
     * @return $this
     */
    public function setProtocol($protocol)
    {
        $this->container['protocol'] = $protocol;

        return $this;
    }

    /**
     * Gets version
     *
     * @return string
     */
    public function getVersion()
    {
        return $this->container['version'];
    }

    /**
     * Sets version
     *
     * @param string $version The protocol version such as '1.0'
     *
     * @return $this
     */
    public function setVersion($version)
    {
        $this->container['version'] = $version;

        return $this;
    }

    /**
     * Gets ts
     *
     * @return int
     */
    public function getTs()
    {
        return $this->container['ts'];
    }

    /**
     * Sets ts
     *
     * @param int $ts The current timestamp
     *
     * @return $this
     */
    public function setTs($ts)
    {
        $this->container['ts'] = $ts;

        return $this;
    }

    /**
     * Gets nonce
     *
     * @return string
     */
    public function getNonce()
    {
        return $this->container['nonce'];
    }

    /**
     * Sets nonce
     *
     * @param string $nonce The random string or auto-increment sequence
     *
     * @return $this
     */
    public function setNonce($nonce)
    {
        $this->container['nonce'] = $nonce;

        return $this;
    }

    /**
     * Gets os
     *
     * @return string
     */
    public function getOs()
    {
        return $this->container['os'];
    }

    /**
     * Sets os
     *
     * @param string $os The operating system of client such as ios, android, dweb,etc.
     *
     * @return $this
     */
    public function setOs($os)
    {
        $this->container['os'] = $os;

        return $this;
    }

    /**
     * Gets language
     *
     * @return string
     */
    public function getLanguage()
    {
        return $this->container['language'];
    }

    /**
     * Sets language
     *
     * @param string $language The i18n language code such as zh, en, etc.
     *
     * @return $this
     */
    public function setLanguage($language)
    {
        $this->container['language'] = $language;

        return $this;
    }

    /**
     * Gets md5
     *
     * @return string
     */
    public function getMd5()
    {
        return $this->container['md5'];
    }

    /**
     * Sets md5
     *
     * @param string $md5 The HMAC authentication md5 checksum
     *
     * @return $this
     */
    public function setMd5($md5)
    {
        $this->container['md5'] = $md5;

        return $this;
    }

    /**
     * Gets sign_type
     *
     * @return string
     */
    public function getSignType()
    {
        return $this->container['sign_type'];
    }

    /**
     * Sets sign_type
     *
     * @param string $sign_type The signature Type,aka cryptographic algorithm.
     *
     * @return $this
     */
    public function setSignType($sign_type)
    {
        $this->container['sign_type'] = $sign_type;

        return $this;
    }

    /**
     * Gets signature
     *
     * @return string
     */
    public function getSignature()
    {
        return $this->container['signature'];
    }

    /**
     * Sets signature
     *
     * @param string $signature The signature hex string by application owner. The exclude fields is [sign_type, signature, md5].
     *
     * @return $this
     */
    public function setSignature($signature)
    {
        $this->container['signature'] = $signature;

        return $this;
    }

    /**
     * Gets uuid
     *
     * @return string
     */
    public function getUuid()
    {
        return $this->container['uuid'];
    }

    /**
     * Sets uuid
     *
     * @param string $uuid The request uuid
     *
     * @return $this
     */
    public function setUuid($uuid)
    {
        $this->container['uuid'] = $uuid;

        return $this;
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
     * Gets content
     *
     * @return \Swagger\Client\Model\Order
     */
    public function getContent()
    {
        return $this->container['content'];
    }

    /**
     * Sets content
     *
     * @param \Swagger\Client\Model\Order $content content
     *
     * @return $this
     */
    public function setContent($content)
    {
        $this->container['content'] = $content;

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