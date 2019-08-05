package org.newtonproject.hep.rest;

import org.bouncycastle.openssl.PEMKeyPair;
import org.bouncycastle.openssl.PEMParser;
import org.bouncycastle.openssl.PEMWriter;
import org.bouncycastle.openssl.jcajce.JcaPEMKeyConverter;
import sun.security.provider.SecureRandom;

import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.io.StringReader;
import java.security.KeyPair;
import java.security.KeyPairGenerator;
import java.security.PrivateKey;
import java.security.spec.ECGenParameterSpec;

public class PrivateKeyTest {
    private static final String KEY_ALGORITHM           = "EC";
    private static final String SIGNATURE_ALGORITHM     = "SHA512withECDSA";
    private static final String PROVIDER                = "BC";
    private static final String CURVE_NAME              = "secp521r1";
    private static final String WRAPPING_CIPHER_SPEC    = "ECIESwithAES";

    private ECGenParameterSpec  ecGenSpec;
    private KeyPairGenerator keyGen_;
    private SecureRandom rand_;

    public void run()
    {
        try
        {
            rand_       = new SecureRandom();
            ecGenSpec   = new ECGenParameterSpec(CURVE_NAME);
            keyGen_     = KeyPairGenerator.getInstance(KEY_ALGORITHM, PROVIDER);

            keyGen_.initialize(ecGenSpec, rand_);


            PrivateKey privateKey = keyGen_.generateKeyPair().getPrivate();





            String der = privateKeyToDER(privateKey);

            PrivateKey recoveredKey = privateKeyFromDER(der);

            System.out.println("privateKey=" + privateKey);
            System.out.println("privateKey.getAlgorithm()=" + privateKey.getAlgorithm());
            System.out.println("der=" + der);
            System.out.println("recoveredKey=" + privateKey);
            System.out.println("recoveredKey.getAlgorithm()=" + recoveredKey.getAlgorithm());
            System.out.println();

            if(privateKey.equals(recoveredKey))
                System.out.println("Key recovery ok");
            else
                System.err.println("Private key recovery failed");

            if(privateKey.getAlgorithm().equals(recoveredKey.getAlgorithm()))
                System.out.println("Key algorithm ok");
            else
                System.err.println("Key algorithms do not match");
        }
        catch(Exception e)
        {
            e.printStackTrace();
        }
    }

    public static   String      privateKeyToDER(PrivateKey key) throws IOException
    {
        ByteArrayOutputStream   bos = new ByteArrayOutputStream();

        PEMWriter               pemWriter = new PEMWriter(new OutputStreamWriter(bos));

        pemWriter.writeObject(key);

        pemWriter.close();

        return new String(bos.toByteArray());
    }

    private static PrivateKey privateKeyFromDER(String der) throws IOException
    {
        StringReader reader = new StringReader(der);
        try (PEMParser pemParser = new PEMParser(reader)) {
            Object o = pemParser.readObject();

            if (!(o instanceof PEMKeyPair)) {
                throw new IOException("Not an OpenSSL key");
            }
            KeyPair kp = new JcaPEMKeyConverter().setProvider("BC").getKeyPair((PEMKeyPair) o);
            return kp.getPrivate();
        }
    }
}
