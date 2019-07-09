<?php


namespace HepRestApi\Scenarios;

use HepRestApi\ApiException;
use HepRestApi\Model\CreateProofRequest;
use HepRestApi\Model\RetrieveProofReceiptsRequest;

class ProofHelper extends BaseHelper
{

    /**
     * Generate the payment request
     * @param array $content it can be generated by OrderProof utility.
     * @param string $uuid The request uuid for desktop-browser. optional.
     * @return \HepRestApi\Model\CreateProofResponse
     * @throws ApiException
     */
    public function generate_proof_request($content, $uuid = null)
    {
        if (empty($uuid)) {
            throw new ApiException("uuid can not be None");
        }
        if (empty($content)) {
            throw new ApiException("content can not be None");
        }

        $data = [
            'action' => $this->action_auth_proof,
            'uuid' => $uuid,
            'content' => $content,
            'dapp_id' => $this->dapp_id
        ];

        $sign_data = $this->generate_sign_data($data);
        $hmac_data = $this->sign_hmac($sign_data);
        $final_data = $this->sign_secp256r1($hmac_data);

        # start request
        $proofs = new CreateProofRequest($final_data);
        $auth_response = $this->api_client->restProofsCreate($this->api_version, $proofs);
        return $auth_response;
    }

    /**
     * Generate the hep-based scheme string string for QRCode
     * @param array $proof_hash The proof request hash
     * @return string The QRcode string
     */
    public function generate_qrcode_string($proof_hash)
    {
        $protocol = $this->base_parameters['protocol'];
        $action = $this->action_auth_proof;
        $format = "%s://%s/?action=%s&proof_hash=%s";
        $qrcode_str = sprintf($format, strtolower($protocol), $this->dapp_id, $action, $proof_hash);
        return $qrcode_str;
    }

    /**
     * Validate the response of proof callback sent by end users such as NewPay users
     * @param array $data The callback data
     * @return mixed True if valid data, otherwise False
     */
    public function validate_proof_callback($data)
    {
        return $this->validate_r1_data($data);
    }

    /**
     * Get the status of given proof_hashes.eg: SUBMIT, CONFIRM, PROCESSING, PART_CANCELED, CANCELED
     * @param array $proof_hashes list
     * @return \HepRestApi\Model\RetrieveProofReceiptsResponse
     * @throws ApiException
     */
    public function get_status_of_proofs($proof_hashes)
    {
        $params = [
            'proof_hashes' => $proof_hashes
        ];
        $sign_data = $this->generate_sign_data($params);
        $hmac_data = $this->sign_hmac($sign_data);

        $proof_request = new RetrieveProofReceiptsRequest($hmac_data);
        $response = $this->api_client->restProofsReceiptsCreate($this->api_version, $proof_request);

        return $response;
    }
}
