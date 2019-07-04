<?php


namespace HepRestApi\Scenarios;

use HepRestApi\Model\AuthCacheRequest;
use HepRestApi\Utils;

class AuthHelper extends BaseHelper
{

    /**
     * Generate the authentication request
     * @param int scope: The request scope. 1: base profile including name,head,newid; 2: advance profile including cellphone.
     * @param int expired: The expired time of request
     * @param string memo: The memo of request to end user
     * @param string uuid: The request uuid for desktop-browser. optional.
     * @return mixed
     * @throws \HepRestApi\ApiException
     */
    public function generate_auth_request($uuid, $scope = 1, $expired = 300, $memo = '')
    {
        if (empty($uuid)) {
            throw new \InvalidArgumentException("uuid can not be None");
        }
        if (empty($memo)) {
            $memo = "default";
        }

        $data = [
            'action'  => $this->action_auth_login,
            'scope'   => $scope,
            'expired' => time() + $expired,
            'memo'    => $memo,
            'uuid'    => $uuid,
            'dapp_id' => $this->dapp_id
        ];

        $sign_data  = $this->generate_sign_data($data);
        $hmac_data  = $this->sign_hmac($sign_data);
        $final_data = $this->sign_secp256r1($hmac_data);
        # start request
        $auth_cache    = new AuthCacheRequest($final_data);
        $auth_response = $this->api_client->restNewnetCachesAuthCreate($auth_cache, $this->api_version);
        return $auth_response;
    }

    /**
     * Generate the hep-based scheme string string for QRCode
     * @param string $auth_hash The auth request hash
     * @return string
     */
    public function generate_qrcode_string($auth_hash)
    {
        $protocol = $this->base_parameters['protocol'];
        $action   = $this->action_auth_login;

        $format     = "%s://%s/?action=%s&auth_hash=%s";
        $qrcode_str = sprintf($format, strtolower($protocol), $this->dapp_id, $action, $auth_hash);
        return $qrcode_str;
    }

    /**
     * Validate the response of auth callback sent by end users such as NewPay users
     * @param array $data The callback data
     * @return bool True if valid data, otherwise False
     */
    public function validate_auth_callback($data)
    {
        $newid     = $data['newid'];
        $signature = $data['signature'];

        $signed_string = Utils::generate_signature_base_string($data, "&");
        list($r, $s) = $this->split_signature($signature);

        return Utils::validate_newid($r, $s, $signed_string, $newid, $this->chain_id);
    }
}