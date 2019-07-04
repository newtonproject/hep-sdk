<?php


namespace HepRestApi\Scenarios;

use HepRestApi\Utils;
use HepRestApi\Api\RestApi;
use Ramsey\Uuid\Uuid;

class BaseHelper
{
    /* @var RestApi $api_client */
    protected $api_client;

    protected $base_parameters, $dapp_id, $dapp_secret, $private_key, $api_version, $chain_id;

    public function __construct(RestApi $api_client, $base_parameters, $dapp_id, $dapp_secret, $key_path, $api_version='1', $chain_id=1012)
    {
        if (!isset($base_parameters['dapp_key']) || empty($base_parameters['dapp_key'])) {
            throw new \InvalidArgumentException("Missing the required parameter `dapp_key` when calling `BaseHelper`");
        }
        # verify the required parameter 'protocol' is set
        if (!isset($base_parameters['protocol']) || empty($base_parameters['protocol'])) {
            throw new \InvalidArgumentException("Missing the required parameter `protocol` when calling `BaseHelper`");
        }
        # verify the required parameter 'version' is set
        if (!isset($base_parameters['version']) || empty($base_parameters['version'])) {
            throw new \InvalidArgumentException("Missing the required parameter `version` when calling `BaseHelper`");
        }# noqa: E501
        if (!isset($base_parameters['os']) || empty($base_parameters['os'])) {
            throw new \InvalidArgumentException("Missing the required parameter `os` when calling `BaseHelper`");
        }  # noqa: E501
        # verify the required parameter 'language' is set
        if (!isset($base_parameters['language']) || empty($base_parameters['language'])) {
            throw new \InvalidArgumentException("Missing the required parameter `language` when calling `BaseHelper`");
        }
        if (!file_exists($key_path) || !is_file($key_path)) {
            throw new \InvalidArgumentException("The required parameter `key_path` is invalid");
        }
        $private_key = Utils::get_private_key_from_file($key_path);
        if (!$private_key) {
            throw new \InvalidArgumentException("Can not get private key from `key_path`");
        }

        $this->api_client = $api_client;
        $this->base_parameters = $base_parameters;
        $this->private_key = $private_key;
        $this->api_version = $api_version;
        $this->dapp_secret = $dapp_secret;
        $this->action_auth_login = 'hep.auth.login';
        $this->action_auth_pay = "hep.pay.order";
        $this->action_auth_proof = "hep.proof.submit";
        $this->chain_id = $chain_id;
        $this->dapp_id = $dapp_id;
    }

    /**
     * Retrieve the public key of default trust oracle from hep node
     * @return string The public key of default trust oracle
     */
    public function get_default_trust_oracle()
    {
        $params = [];
        $sign_data = $this->generate_sign_data($params);
        $hmac_data = $this->sign_hmac($sign_data);

        $hmac_data['oracle_id'] = 'default';

        $res = $this->api_client->restOraclesRead(
            $this->api_version,
            $hmac_data['oracle_id'],
            $this->base_parameters['dapp_key'],
            $this->base_parameters['protocol'],
            $this->base_parameters['version'],
            $hmac_data['ts'],
            $hmac_data['nonce'],
            $this->base_parameters['os'],
            $this->base_parameters['language'],
            $hmac_data['dapp_signature_method'],
            $hmac_data['dapp_signature']
        );

        return $res['public_key'];
    }

    protected function generate_sign_data(array $data = [])
    {
        $sign_data = array_merge($data, $this->base_parameters);
        # dynamic fields
        $sign_data['ts'] = time();
        $sign_data['nonce'] = Uuid::uuid4()->toString();
        return $sign_data;
    }

    public function sign_hmac(array $data, $dapp_signature_method='HMAC-MD5')
    {
        $dapp_signature = Utils::sign_hmac($data, $this->dapp_secret, '', false, '&', $dapp_signature_method);

        $data['dapp_signature'] = $dapp_signature;
        $data['dapp_signature_method'] = $dapp_signature_method;

        return $data;
    }

    protected function concat_signature($r, $s)
    {
        if (strpos($r, '0x') === 0) {
            $r = substr($r, 2);
        }
        if (strlen($r) < 64) {
            $r = str_pad($r, 64, "0", STR_PAD_LEFT);
        }

        if (strpos($s, '0x') === 0) {
            $s = substr($s, 2);
        }
        if (strlen($s) < 64) {
            $s = str_pad($s, 64, "0", STR_PAD_LEFT);
        }

        return "0x{$r}{$s}";
    }

    public function sign_secp256r1($data)
    {
        $sign_string = Utils::generate_signature_base_string($data, '&');
        $sign = Utils::sign($sign_string, $this->private_key);
        $r = $sign[0];
        $s = $sign[1];
        $signature = $this->concat_signature($r, $s);
        $data['signature'] = $signature;
        $data['sign_type'] = 'secp256r1';
        return $data;
    }

    public function validate_r1_data($data)
    {
        $signed_message = Utils::generate_signature_base_string($data, "&");
        list($r, $s) = $this->split_signature($data['signature']);
        $valid_public_keys = $this->get_default_trust_oracle();

        return Utils::verify($signed_message, $r, $s, $valid_public_keys);
    }

    protected function split_signature($signature)
    {
        if (empty($signature)) {
            throw new \InvalidArgumentException("Missing the required parameter 'signature' when calling split_signature");
        }

        if (strpos($signature, '0x') === 0) {
            $signature = substr($signature, 2);
        }

        $sig_half_len = strlen($signature) / 2;
        $r = '0x' . substr($signature, 0, $sig_half_len);
        $s = '0x' . substr($signature, $sig_half_len);

        return [$r, $s];
    }
}