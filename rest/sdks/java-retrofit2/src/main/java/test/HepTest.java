package test;

import org.newtonproject.hep.rest.ApiClient;
import org.newtonproject.hep.rest.scenarios.AuthHelper;

import java.util.HashMap;

/**
 * @author weixuefeng@lubangame.com
 * @version $Rev$
 * @time: 2019/11/27--1:17 PM
 * @description
 * @copyright (c) 2019 Newton Foundation. All rights reserved.
 */
public class HepTest {

    public static void main(String args[]) {
        /**
         * this.mApiClient = mApiClient.createService(RestApi.class);
         *         this.baseParameters = baseParameters;
         *         this.dappId = dappId;
         *         this.dappSecret = dappSecret;
         *         this.privateKey = privateKey;
         *         this.apiVersion = apiVersion;
         *         this.chainId = chainId;
         */
        String dappKey = "";
        String protocol = "HEP";
        String version = "1.0";
        String os = "android";
        String language = "en";
        HashMap<String, String> baseParameters = new HashMap<>();
        baseParameters.put("dapp_key", dappKey);
        baseParameters.put("protocol", protocol);
        baseParameters.put("version", version);
        baseParameters.put("os", os);
        baseParameters.put("language", language);
        ApiClient apiClient = new ApiClient();
        String dappId = "";
        String dappSecret = "";
        String apiVersion = "1";
        int chainid = 1007;
        String privateKey = "0x23";
        AuthHelper authHelper = new AuthHelper(apiClient, baseParameters, dappId, dappSecret, privateKey,apiVersion, chainid);
        authHelper.generateAuthRequest("a").subscribe(
                next-> {
                    System.out.println(next.getAuthHash());
                },
                error->{
                    System.out.println(error.getMessage());
                }
        );
    }


}
