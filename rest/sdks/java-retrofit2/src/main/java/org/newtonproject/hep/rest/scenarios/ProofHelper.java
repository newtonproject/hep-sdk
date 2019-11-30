package org.newtonproject.hep.rest.scenarios;

import org.newtonproject.hep.rest.api.RestApi;

import java.util.HashMap;

public class ProofHelper extends BaseHelper {

    public ProofHelper(RestApi mApiClient, HashMap<String, String> baseParameters, String dappId, String dappSecret, String keyPath, String apiVersion, int chainId) {
        super(mApiClient, baseParameters, dappId, dappSecret, keyPath, apiVersion, chainId);
    }
}
