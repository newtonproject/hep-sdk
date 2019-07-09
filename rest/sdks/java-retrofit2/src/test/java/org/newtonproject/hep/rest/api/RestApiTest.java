package org.newtonproject.hep.rest.api;

import org.newtonproject.hep.rest.ApiClient;
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

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for RestApi
 */
public class RestApiTest {

    private RestApi api;

    @Before
    public void setup() {
        api = new ApiClient().createService(RestApi.class);
    }

    /**
     * 
     *
     * 
     */
    @Test
    public void restDappsReadTest() {
        String apiVersion = null;
        String dappId = null;
        String dappKey = null;
        String protocol = null;
        String version = null;
        Integer ts = null;
        String nonce = null;
        String os = null;
        String language = null;
        String dappSignatureMethod = null;
        String dappSignature = null;
        // Dapp response = api.restDappsRead(apiVersion, dappId, dappKey, protocol, version, ts, nonce, os, language, dappSignatureMethod, dappSignature);

        // TODO: test validations
    }
    /**
     * 
     *
     * 
     */
    @Test
    public void restHealthListTest() {
        String apiVersion = null;
        // api.restHealthList(apiVersion);

        // TODO: test validations
    }
    /**
     * 
     *
     * Retrieve the transaction information by given txid
     */
    @Test
    public void restNewchainTxReadTest() {
        String apiVersion = null;
        String txid = null;
        String dappKey = null;
        String protocol = null;
        String version = null;
        Integer ts = null;
        String nonce = null;
        String os = null;
        String language = null;
        String dappSignatureMethod = null;
        String dappSignature = null;
        // NewchainTransactionResponse response = api.restNewchainTxRead(apiVersion, txid, dappKey, protocol, version, ts, nonce, os, language, dappSignatureMethod, dappSignature);

        // TODO: test validations
    }
    /**
     * 
     *
     * Retrieve the daily newforce statistics
     */
    @Test
    public void restNewforceReadTest() {
        String apiVersion = null;
        String date = null;
        String dappKey = null;
        String protocol = null;
        String version = null;
        Integer ts = null;
        String nonce = null;
        String os = null;
        String language = null;
        String dappSignatureMethod = null;
        String dappSignature = null;
        // NewforceDailyStatsResponse response = api.restNewforceRead(apiVersion, date, dappKey, protocol, version, ts, nonce, os, language, dappSignatureMethod, dappSignature);

        // TODO: test validations
    }
    /**
     * 
     *
     * Retrieve the information by given NewID
     */
    @Test
    public void restNewidsReadTest() {
        String apiVersion = null;
        String newid = null;
        String dappKey = null;
        String protocol = null;
        String version = null;
        Integer ts = null;
        String nonce = null;
        String os = null;
        String language = null;
        String dappSignatureMethod = null;
        String dappSignature = null;
        // NewidResponse response = api.restNewidsRead(apiVersion, newid, dappKey, protocol, version, ts, nonce, os, language, dappSignatureMethod, dappSignature);

        // TODO: test validations
    }
    /**
     * 
     *
     * Caches the authentication request
     */
    @Test
    public void restNewnetCachesAuthCreateTest() {
        String apiVersion = null;
        AuthCacheRequest data = null;
        // CreateAuthCacheResponse response = api.restNewnetCachesAuthCreate(apiVersion, data);

        // TODO: test validations
    }
    /**
     * 
     *
     * Get the authentication information by given request hash.
     */
    @Test
    public void restNewnetCachesAuthReadTest() {
        String apiVersion = null;
        String authHash = null;
        String dappKey = null;
        String protocol = null;
        String version = null;
        Integer ts = null;
        String nonce = null;
        String os = null;
        String language = null;
        String dappSignatureMethod = null;
        String dappSignature = null;
        // AuthCacheResponse response = api.restNewnetCachesAuthRead(apiVersion, authHash, dappKey, protocol, version, ts, nonce, os, language, dappSignatureMethod, dappSignature);

        // TODO: test validations
    }
    /**
     * 
     *
     * Cache the pay request
     */
    @Test
    public void restNewnetCachesPayCreateTest() {
        String apiVersion = null;
        PayCacheRequest data = null;
        // CreatePayCacheResponse response = api.restNewnetCachesPayCreate(apiVersion, data);

        // TODO: test validations
    }
    /**
     * 
     *
     * Retrieve the pay information by given pay hash.
     */
    @Test
    public void restNewnetCachesPayReadTest() {
        String apiVersion = null;
        String payHash = null;
        String dappKey = null;
        String protocol = null;
        String version = null;
        Integer ts = null;
        String nonce = null;
        String os = null;
        String language = null;
        String dappSignatureMethod = null;
        String dappSignature = null;
        // PayCacheResponse response = api.restNewnetCachesPayRead(apiVersion, payHash, dappKey, protocol, version, ts, nonce, os, language, dappSignatureMethod, dappSignature);

        // TODO: test validations
    }
    /**
     * 
     *
     * Get the oracle information by given id.
     */
    @Test
    public void restOraclesReadTest() {
        String apiVersion = null;
        String oracleId = null;
        String dappKey = null;
        String protocol = null;
        String version = null;
        Integer ts = null;
        String nonce = null;
        String os = null;
        String language = null;
        String dappSignatureMethod = null;
        String dappSignature = null;
        // RetrieveOracleResponse response = api.restOraclesRead(apiVersion, oracleId, dappKey, protocol, version, ts, nonce, os, language, dappSignatureMethod, dappSignature);

        // TODO: test validations
    }
    /**
     * 
     *
     * 
     */
    @Test
    public void restProofsCreateTest() {
        String apiVersion = null;
        CreateProofRequest data = null;
        // CreateProofResponse response = api.restProofsCreate(apiVersion, data);

        // TODO: test validations
    }
    /**
     * 
     *
     * 
     */
    @Test
    public void restProofsDeleteTest() {
        String apiVersion = null;
        String proofHash = null;
        CancelProofRequest data = null;
        // CancelProofResponse response = api.restProofsDelete(apiVersion, proofHash, data);

        // TODO: test validations
    }
    /**
     * 
     *
     * Get the proof by given proof hash.
     */
    @Test
    public void restProofsReadTest() {
        String apiVersion = null;
        String proofHash = null;
        String dappKey = null;
        String protocol = null;
        String version = null;
        Integer ts = null;
        String nonce = null;
        String os = null;
        String language = null;
        String dappSignatureMethod = null;
        String dappSignature = null;
        // ProofResponse response = api.restProofsRead(apiVersion, proofHash, dappKey, protocol, version, ts, nonce, os, language, dappSignatureMethod, dappSignature);

        // TODO: test validations
    }
    /**
     * 
     *
     * 
     */
    @Test
    public void restProofsReceiptsCreateTest() {
        String apiVersion = null;
        RetrieveProofReceiptsRequest data = null;
        // RetrieveProofReceiptsResponse response = api.restProofsReceiptsCreate(apiVersion, data);

        // TODO: test validations
    }
}
