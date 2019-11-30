package org.newtonproject.hep.rest.scenarios;

import org.newtonproject.hep.rest.ApiClient;
import org.newtonproject.hep.rest.Utils;
import org.newtonproject.hep.rest.api.RestApi;
import org.web3j.utils.Numeric;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.UUID;

public class BaseHelper {
    protected RestApi mApiClient;
    protected HashMap<String, String> baseParameters;
    protected String dappId;
    protected String dappSecret;
    protected String privateKey;
    protected String apiVersion = "1";
    protected int chainId = 1012;
    protected String actionAuthLogin = "hep.auth.login";
    protected String actionAuthPay = "hep.pay.order";
    protected String actionAuthProof = "hep.proof.submit";

    public BaseHelper(ApiClient mApiClient, HashMap<String, String> baseParameters, String dappId, String dappSecret, String privateKey, String apiVersion, int chainId) {
        this.mApiClient = mApiClient.createService(RestApi.class);
        this.baseParameters = baseParameters;
        this.dappId = dappId;
        this.dappSecret = dappSecret;
        this.privateKey = privateKey;
        this.apiVersion = apiVersion;
        this.chainId = chainId;
        if(!baseParameters.containsKey("dapp_key") || baseParameters.get("dapp_key") == null){
            throw new IllegalArgumentException("Missing the required parameter `dapp_key` when calling `BaseHelper");
        }
        if(!baseParameters.containsKey("protocol") || baseParameters.get("protocol") == null){
            throw new IllegalArgumentException("Missing the required parameter `protocol` when calling `BaseHelper");
        }
        if(!baseParameters.containsKey("version") || baseParameters.get("version") == null){
            throw new IllegalArgumentException("Missing the required parameter `version` when calling `BaseHelper");
        }
        if(!baseParameters.containsKey("os") || baseParameters.get("os") == null){
            throw new IllegalArgumentException("Missing the required parameter `os` when calling `BaseHelper");
        }
        if(!baseParameters.containsKey("language") || baseParameters.get("language") == null){
            throw new IllegalArgumentException("Missing the required parameter `language` when calling `BaseHelper");
        }

    }

    public BaseHelper(ApiClient mApiClient, HashMap<String, String> baseParameters, String dappId, String dappSecret, String keyPath) {
        this(mApiClient,baseParameters, dappId, dappSecret, keyPath, "1", 1012);
    }

    public BaseHelper(ApiClient mApiClient, HashMap<String, String> baseParameters, String dappId, String dappSecret, String keyPath, int chainId) {
        this(mApiClient,baseParameters, dappId, dappSecret, keyPath, "1", chainId);
    }

    public ArrayList<String> getDefaultTrustOracle() {
        HashMap<String, String> map = new HashMap<>();
        HashMap<String, String> signData = generateSignData(map);
        HashMap<String, String> signHmac = signHmac(signData);
        signHmac.put("api_version", apiVersion);
        signHmac.put("oracle_id", "default");
        //Observable<RetrieveOracleResponse> retrieveOracleResponseObservable = mApiClient.restOraclesRead();
        return null;
    }

    public HashMap<String, String> generateSignData(HashMap<String, String> data) {
        HashMap<String, String> signData = data;
        signData.put("ts", System.currentTimeMillis() / 1000 + "");
        signData.put("nonce", UUID.randomUUID().toString());
        signData.putAll(baseParameters);
        return signData;
    }

    public HashMap<String, String> signHmac(HashMap<String, String> data) {
        String hmac = Utils.signHmac(data, dappSecret, "&");
        data.put("dapp_signature", hmac);
        data.put("dapp_signature_method", "HMAC-MD5");
        return data;
    }

    public String concatSignature(String r, String s) {
        return Numeric.prependHexPrefix(r) + Numeric.cleanHexPrefix(s);
    }

    public HashMap<String, String> signSecp256r1(HashMap<String,String> data) {
        String message = Utils.generateSignatureBaseString(data, "&");
        String res = Utils.signSecp256r1(message, privateKey);
        data.put("signature", res);
        data.put("sign_type", "secp256r1");
        return data;
    }

    public boolean validateR1Data(HashMap<String, String> data) {
        String message = Utils.generateSignatureBaseString(data, "&");
        HashMap<String, String> map = Utils.splitSignature(data.get("signature"));
        ArrayList<String> defaultTrustOracle = getDefaultTrustOracle();
        return Utils.validateSecp256r1Signature(map.get("r"), map.get("s"), message, defaultTrustOracle);
    }

    public boolean validateR1DataByPublic(HashMap<String, String> data, String publicKey) {
        String message = Utils.generateSignatureBaseString(data, "&");
        HashMap<String, String> map = Utils.splitSignature(data.get("signature"));
        ArrayList<String> defaultTrustOracle = new ArrayList<>();
        defaultTrustOracle.add(publicKey);
        return Utils.validateSecp256r1Signature(map.get("r"), map.get("s"), message, defaultTrustOracle);
    }

    public HashMap<String, String> getClientBaseParams(HashMap<String, String> data) {
        HashMap<String, String> map = new HashMap<>();
        map.put("dapp_id", dappId);
        map.put("protocol", baseParameters.get("protocol"));
        map.put("version", baseParameters.get("version"));
        map.put("ts", String.valueOf(System.currentTimeMillis() / 1000));
        map.put("nonce", UUID.randomUUID().toString());
        map.put("sign_type", "secp256r1");
        data.putAll(map);
        String message = Utils.generateSignatureBaseString(data, "&");
        String signature = Utils.signSecp256r1(message, privateKey);
        data.put("signature", signature);
        return data;
    }
}
