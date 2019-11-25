package org.newtonproject.hep.rest.scenarios;

import io.reactivex.Observable;
import org.newtonproject.hep.rest.ApiClient;
import org.newtonproject.hep.rest.Utils;
import org.newtonproject.hep.rest.models.AuthCacheRequest;
import org.newtonproject.hep.rest.models.CreateAuthCacheResponse;

import java.util.HashMap;

public class AuthHelper extends BaseHelper{
    public AuthHelper(ApiClient mApiClient, HashMap<String, String> baseParameters, String dappId, String dappSecret, String privateKey, String apiVersion, int chainId) {
        super(mApiClient, baseParameters, dappId, dappSecret, privateKey, apiVersion, chainId);
    }

    public AuthHelper(ApiClient mApiClient, HashMap<String, String> baseParameters, String dappId, String dappSecret, String keyPath) {
        super(mApiClient, baseParameters, dappId, dappSecret, keyPath);
    }

    public AuthHelper(ApiClient mApiClient, HashMap<String, String> baseParameters, String dappId, String dappSecret, String keyPath, int chainId) {
        super(mApiClient, baseParameters, dappId, dappSecret, keyPath, chainId);
    }

    public Observable<CreateAuthCacheResponse> generateAuthRequest(String uuid) {
        HashMap<String, String> map = new HashMap<>();
        map.put("action", actionAuthLogin);
        map.put("scope", "2");
        map.put("expired", "600");
        map.put("memo", "default");
        map.put("uuid", uuid);
        map.put("dapp_id", dappId);
        HashMap<String, String> signData = generateSignData(map);
        HashMap<String, String> signHmac = signHmac(signData);
        HashMap<String, String> signR1Data = signSecp256r1(signHmac);
        AuthCacheRequest request = new AuthCacheRequest();
        //todo: generate authrequest
        //request.setAction();
        return mApiClient.restNewnetCachesAuthCreate(apiVersion, request);
    }

    public String generateQrCodeString(String authHash) {
        String protocol = baseParameters.get("protocol");
        String action = actionAuthLogin;
        return String.format("%s://%s/?action=%s&auth_hash=%s", protocol.toLowerCase(), dappId, action, authHash);
    }

    public boolean validateAuthCallback(HashMap<String, String> data) {
        String newid = data.get("newid");
        String signature = data.get("signature");
        String message = Utils.generateSignatureBaseString(data, "&");
        HashMap<String, String> map = Utils.splitSignature(signature);
        return Utils.validateNewid(map.get("r"), map.get("s"), message, newid, chainId);
    }

    public HashMap<String, String> getClientLoginParams(String uuid) {
        HashMap<String, String> params = new HashMap<>();
        params.put("action", actionAuthLogin);
        params.put("scope", "2");
        params.put("memo", "default");
        params.put("uuid", uuid);
        return getClientBaseParams(params);
    }

}
