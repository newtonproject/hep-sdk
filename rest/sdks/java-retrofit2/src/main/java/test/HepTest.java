package test;

import org.newtonproject.hep.rest.ApiClient;
import org.newtonproject.hep.rest.scenarios.AuthHelper;

import java.util.HashMap;
import java.util.UUID;

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
        String dappKey = "02c3119710714730b000db31d73052ce";
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
        String dappId = "d32db928a0034598a69bdf375551f822";
        String dappSecret = "eae92dbda0454049b8016a43c2d7025e";
        String apiVersion = "1";
        int chainid = 1007;
        String privateKey = "0xed3be0b0c9862339dbec1cef295ada174c26d2812e81ba0f0f51b73cd42fc99b";
        AuthHelper authHelper = new AuthHelper(apiClient, baseParameters, dappId, dappSecret, privateKey,apiVersion, chainid);
        authHelper.generateAuthRequest(UUID.randomUUID().toString()).subscribe(
                next-> {
                    System.out.println(next.getAuthHash());
                },
                error->{
                    System.out.println(error.toString());
                }
        );
        authHelper.generateQrCodeString("be6cbf0944155fe9dbdb293ba08291a1400e11c65b8deddd5360018da7416ec4");
    }


}
