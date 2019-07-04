<?php


namespace HepRestApi\Scenarios;

use HepRestApi\Model\PayCacheRequest;
use HepRestApi\Model\CreatePayCacheResponse;
use HepRestApi\Model\NewchainTransactionResponse;

class PayHelper extends BaseHelper
{

    /**
     * Generate the payment request
     * @param string dapp_id: The DApp ID
     * @param string order_number: The order number
     * @param string price_currency: The symbol of fiat or digital token, such as USD, CNY, NEW,BTC,ETH.
     * @param string total_price: The amount of fiat or digital token, unit is the minimum unit of given fiat or digital token.
     * @param string description: The order description
     * @param string seller: The seller's NewID
     * @param string customer: The customer's NewID
     * @param string broker: The broker's NewID. optional.
     * @param int expired: The expired time of request
     * @param string uuid: The request uuid for desktop-browser. optional.
     * @return mixed|CreatePayCacheResponse The request information including signature
     */
    public function generate_pay_request(
        $order_number,
        $price_currency,
        $total_price,
        $description,
        $seller,
        $customer,
        $broker = '',
        $expired = 300,
        $uuid = null
    )
    {
        if (empty($uuid)) {
            throw new \InvalidArgumentException("uuid can not be None");
        }
        if (empty($order_number)) {
            throw new \InvalidArgumentException("order number can not be None");
        }

        $data = [
            'action'         => $this->action_auth_pay,
            'order_number'   => $order_number,
            'expired'        => time() + $expired,
            'price_currency' => $price_currency,
            'total_price'    => $total_price,
            'description'    => $description,
            'seller'         => $seller,
            'customer'       => $customer,
            'broker'         => $broker,
            'uuid'           => $uuid,
            'dapp_id'        => $this->dapp_id
        ];

        $sign_data  = $this->generate_sign_data($data);
        $hmac_data  = $this->sign_hmac($sign_data);
        $final_data = $this->sign_secp256r1($hmac_data);

        # start request
        $auth_cache    = new PayCacheRequest($final_data);
        $auth_response = $this->api_client->restNewnetCachesPayCreate($auth_cache, $this->api_version);
        return $auth_response;
    }

    /**
     * Generate the hep-based scheme string string for QRCode
     * @param string $pay_hash The pay request hash
     * @return string The QRcode string
     */
    public function generate_qrcode_string($pay_hash)
    {
        $protocol = $this->base_parameters['protocol'];
        $action = $this->action_auth_pay;
        $format = "%s://%s/?action=%s&pay_hash=%s";
        $qrcode_str = sprintf($format, strtolower($protocol), $this->dapp_id, $action, $pay_hash);
        return $qrcode_str;
    }

    /**
     * Validate the response of pay callback sent by end users such as NewPay users
     * @param array $data The callback data
     * @return bool True if valid data, otherwise False
     */
    public function validate_pay_callback($data)
    {
        return $this->validate_r1_data($data);
    }

    /**
     * Validate transaction by transaction id. and you can get the order_number, block height and etc.
     * @param int $transaction_id
     * @return NewchainTransactionResponse dict about transaction
     */
    public function get_confirmed_transaction($transaction_id)
    {
        $params = [];
        $sign_data = $this->generate_sign_data($params);
        $hmac_data = $this->sign_hmac($sign_data);

        $response = $this->api_client->restNewchainTxRead(
            $this->api_version,
            $transaction_id,
            $hmac_data['dapp_key'],
            $hmac_data['protocol'],
            $hmac_data['version'],
            $hmac_data['ts'],
            $hmac_data['nonce'],
            $hmac_data['os'],
            $hmac_data['language'],
            $hmac_data['dapp_signature_method'],
            $hmac_data['dapp_signature']
        );
        return $response;

    }

}