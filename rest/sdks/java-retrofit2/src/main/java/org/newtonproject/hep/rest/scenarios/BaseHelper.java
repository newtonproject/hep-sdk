package org.newtonproject.hep.rest.scenarios;

import org.newtonproject.hep.rest.ApiClient;
import org.newtonproject.hep.rest.Utils;

import java.util.HashMap;
import java.util.UUID;

public class BaseHelper {
    protected ApiClient mApiClient;
    protected HashMap<String, String> baseParameters;
    protected String dappId;
    protected String dappSecret;
    protected String keyPath;
    protected String apiVersion = "1";
    protected int chainId = 1012;
    protected String actionAuthLogin = "hep.auth.login";
    protected String actionAuthPay = "hep.pay.order";
    protected String actionAuthProof = "hep.proof.submit";

    public BaseHelper(ApiClient mApiClient, HashMap<String, String> baseParameters, String dappId, String dappSecret, String keyPath, String apiVersion, int chainId) {
        this.mApiClient = mApiClient;
        this.baseParameters = baseParameters;
        this.dappId = dappId;
        this.dappSecret = dappSecret;
        this.keyPath = keyPath;
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

    public HashMap<String, String> generateSignData(HashMap<String, String> data) {
        HashMap<String, String> signData = data;
        signData.put("ts", System.currentTimeMillis() + "");
        signData.put("nonce", UUID.randomUUID().toString());
        return signData;
    }

    public HashMap<String, String> signHmac(HashMap<String, String> data) {
        String s = Utils.signHmac(data, dappSecret, "&");
        return null;
    }
}
