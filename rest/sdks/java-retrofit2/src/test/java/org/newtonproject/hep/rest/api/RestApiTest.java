package org.newtonproject.hep.rest.api;

import org.newtonproject.hep.rest.ApiClient;
import org.newtonproject.hep.rest.JSON;
import org.newtonproject.hep.rest.models.AuthCacheRequest;
import org.newtonproject.hep.rest.models.AuthCacheResponse;
import org.newtonproject.hep.rest.models.CancelProofRequest;
import org.newtonproject.hep.rest.models.CancelProofResponse;
import org.newtonproject.hep.rest.models.CreateAuthCacheResponse;
import org.newtonproject.hep.rest.models.CreatePayCacheResponse;
import org.newtonproject.hep.rest.models.CreateProofRequest;
import org.newtonproject.hep.rest.models.CreateProofResponse;
import org.newtonproject.hep.rest.models.Dapp;
import org.newtonproject.hep.rest.models.NewchainTransactionResponse;
import org.newtonproject.hep.rest.models.NewforceDailyStatsResponse;
import org.newtonproject.hep.rest.models.NewidResponse;
import org.newtonproject.hep.rest.models.PayCacheRequest;
import org.newtonproject.hep.rest.models.PayCacheResponse;
import org.newtonproject.hep.rest.models.ProofResponse;
import org.newtonproject.hep.rest.models.RetrieveOracleResponse;
import org.newtonproject.hep.rest.models.RetrieveProofReceiptsRequest;
import org.newtonproject.hep.rest.models.RetrieveProofReceiptsResponse;
import org.junit.Before;
import org.junit.Test;
import org.newtonproject.hep.rest.scenarios.AuthHelper;

import java.util.*;

/**
 * API tests for RestApi
 */
public class RestApiTest {

    private RestApi api;
    private String dappKey = "02c3119710714730b000db31d73052ce";

    private String protocol = "HEP";
    private String version = "1.0";
    private String os = "android";
    private String language = "en";

    private HashMap<String, String> baseParameters = new HashMap<>();
    private String baseUrl = "http://hep.newtonproject.dev.diynova.com/";

    private String dappId = "d32db928a0034598a69bdf375551f822";
    private String dappSecret = "eae92dbda0454049b8016a43c2d7025e";
    private String apiVersion = "1";
    private int chainid = 1007;
    private String privateKey = "0xed3be0b0c9862339dbec1cef295ada174c26d2812e81ba0f0f51b73cd42fc99b";

    private AuthHelper authHelper;
    @Before
    public void setup() {
        api = new ApiClient(baseUrl).createService(RestApi.class);
        baseParameters.put("dapp_key", dappKey);
        baseParameters.put("protocol", protocol);
        baseParameters.put("version", version);
        baseParameters.put("os", os);
        baseParameters.put("language", language);
        authHelper = new AuthHelper(api, baseParameters, dappId, dappSecret, privateKey,apiVersion, chainid);
    }

    @Test
    public void getAuthHash() {
        authHelper.generateAuthRequest(UUID.randomUUID().toString())
                .subscribe(
                        next-> {
                            System.out.println(next.getAuthHash());
                        },
                        error-> {
                            System.out.println(error.getMessage());
                        }
                );
    }

}
