package org.newtonproject.hep.rest;

import com.google.gson.Gson;
import org.newtonproject.hep.rest.utils.Base58;
import org.newtonproject.hep.rest.utils.SecureRandomUtils;
import org.web3j.crypto.*;
import org.web3j.utils.Numeric;

import java.io.File;
import java.io.IOException;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.math.BigInteger;
import java.security.InvalidAlgorithmParameterException;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.security.NoSuchProviderException;
import java.util.*;

public class Utils {

    static JSON json = new JSON();
    static String privateKey = null;

    public static String generateMd5(String data) {
        MessageDigest messageDigest;
        try {
            messageDigest = MessageDigest.getInstance("MD5");
            messageDigest.reset();
            messageDigest.update(data.getBytes("UTF8"));
            final byte[] resultByte = messageDigest.digest();
            return Numeric.toHexString(resultByte).replace("0x", "");
        } catch (Exception e) {
            e.printStackTrace();
        }
        return null;
    }

    public static String generateSignatureBaseString(HashMap<String, String> data, String joint) {
        String jsonContent = json.getGson().toJson(data);
        TreeMap<String, Object> treeMap = new TreeMap<>(new Comparator<String>() {
            @Override
            public int compare(String o1, String o2) {
                return o1.compareTo(o2);
            }
        });
        TreeMap<String, Object> map = json.getGson().fromJson(jsonContent, treeMap.getClass());
        ArrayList<String> keys = new ArrayList<>();
        keys.add("dapp_signature");
        keys.add("signature");
        keys.add("sign_type");
        keys.add("dapp_signature_method");
        int index = 0;
        StringBuilder builder = new StringBuilder();
        Set<Map.Entry<String, Object>> entries = map.entrySet();
        for(Map.Entry<String, Object> entry : entries) {
            String key = entry.getKey();
            Object value = entry.getValue();
            if(keys.contains(key)) {
                continue;
            }
            if(index != 0) {
                builder.append(joint);
            }
            if(value instanceof Map) {
                builder.append(String.format("%s=%s", key, json.getGson().toJson(sortMap((Map<String, Object>) value))));
            } else if(value instanceof ArrayList){
                builder.append(String.format("%s=%s", key, json.getGson().toJson(sortList((ArrayList) value))));
            } else {
                if (null == value) continue;
                builder.append(String.format("%s=%s", key, value));
            }
            index += 1;
        }
        return builder.toString();
    }

    public static String signHmac(HashMap<String, String> data, String secret, String joint) {
        String signString = generateSignatureBaseString(data, joint);
        signString += secret;
        return generateMd5(signString);
    }

    /**
     * generate wallet file.
     * @param destinationDirectory
     * @param password
     * @return
     * @throws IOException
     * @throws CipherException
     * @throws InvalidAlgorithmParameterException
     * @throws NoSuchAlgorithmException
     * @throws NoSuchProviderException
     */
    public static String generateECKeyPair(String destinationDirectory, String password) throws IOException, CipherException, InvalidAlgorithmParameterException, NoSuchAlgorithmException, NoSuchProviderException {
        byte[] bytes = new byte[16];
        SecureRandomUtils.SECURE_RANDOM.nextBytes(bytes);
        return WalletUtils.generateFullNewWalletFile(password, new File(destinationDirectory));
    }

    /**
     * sign message by private key.
     * @param message the string you need to sign with secp256r1
     * @param privateKey private key string with 0x.
     * @return
     */
    public static String signSecp256r1(String message, String privateKey) {
        Sign.SignatureData sig = Sign.signMessage(message.getBytes(), ECKeyPair.create(Numeric.toBigInt(privateKey)));
        String r = Numeric.toHexString(sig.getR());
        String s = Numeric.toHexStringNoPrefix(sig.getS());
        return r + s;
    }

    /**
     * get private key with prefix.
     * @param keystorePath
     * @param password
     * @return private key string.
     * @throws IOException
     * @throws CipherException
     */
    public static String getPrivateKey(String keystorePath, String password) throws IOException, CipherException {
        Credentials credentials = WalletUtils.loadCredentials(password, new File(keystorePath));
        return Numeric.toHexStringWithPrefix(credentials.getEcKeyPair().getPrivateKey());
    }

    /**
     * get public key
     * @param keystorePath
     * @param password
     * @return
     * @throws IOException
     * @throws CipherException
     */
    public static String getPublicKey(String keystorePath, String password) throws IOException, CipherException {
        Credentials credentials = WalletUtils.loadCredentials(password, new File(keystorePath));
        return Numeric.toHexStringWithPrefix(credentials.getEcKeyPair().getPublicKey());
    }

    /**
     *
     * @param r
     * @param s
     * @param message
     * @return
     */
    public static ArrayList<String> extractSecp256r1PublicKeys(String r, String s, String message) {
        ArrayList<String> publicKeys = new ArrayList<>();
        Class clazz = null;
        try {
            clazz = Class.forName("org.web3j.crypto.Sign");
            Method recover = clazz.getDeclaredMethod("recoverFromSignature", int.class, ECDSASignature.class, byte[].class);
            recover.setAccessible(true);
            for(int i = 0; i < 4; i++) {
                Object k = recover.invoke(null, i, new ECDSASignature(Numeric.toBigInt(r), Numeric.toBigInt(s)).toCanonicalised(), Hash.sha3(message.getBytes()));
                if(k != null) {
                    String pub = Numeric.toHexStringNoPrefix((BigInteger) k);
                    publicKeys.add(pub);
                }
            }
        } catch (ClassNotFoundException | InvocationTargetException | IllegalAccessException | NoSuchMethodException e) {
            e.printStackTrace();
        }
        return publicKeys;
    }

    public static boolean validateSecp256r1Signature(String r, String s, String message, ArrayList<String> validPublicKeys) {
        ArrayList<String> list = extractSecp256r1PublicKeys(r, s, message);
        for (String calculatePublicKey : list) {
            if(validPublicKeys.contains(calculatePublicKey)) {
                return true;
            }
        }
        return false;
    }

    public static String newidEncodeByPublicKey(String publicKey, int chainId) {
        String hash = Hash.sha3(publicKey);
        hash = Numeric.cleanHexPrefix(hash);
        String hexChainId = Integer.toHexString(chainId);
        if(hexChainId.length() > 8) {
            hexChainId = hexChainId.substring(hexChainId.length() - 8);
        }
        String data = hexChainId + hash;
        byte[] addressData = new BigInteger(data, 16).toByteArray();
        return "NEWID" + Base58.encodeChecked(0, addressData);
    }

    public static boolean validateNewid(String r, String s, String message, String newid, int chainId) {
        ArrayList<String> list = extractSecp256r1PublicKeys(r, s, message);
        for (String pub : list) {
            String calculateNewId = newidEncodeByPublicKey(pub, chainId);
            if (calculateNewId.equals(newid)) {
                return true;
            }
        }
        return false;
    }

    public static HashMap<String, String> splitSignature(String signature) {
        signature = Numeric.cleanHexPrefix(signature);
        String r = Numeric.prependHexPrefix(signature.substring(0, signature.length() / 2));
        String s = Numeric.prependHexPrefix(signature.substring(signature.length() / 2));
        HashMap<String, String> sigMap = new HashMap<>();
        sigMap.put("r", r);
        sigMap.put("s", s);
        return sigMap;
    }

    private static TreeMap<String, Object> sortMap(Map<String, Object> map) {
        Gson gson = json.getGson();
        TreeMap<String, Object> treeMap = new TreeMap<>(
                new Comparator<String>() {
                    @Override
                    public int compare(String o1, String o2) {
                        return o1.compareTo(o2);
                    }
                });
        Set<Map.Entry<String, Object>> entries = map.entrySet();
        for(Map.Entry<String, Object> entry: entries) {
            Object value = entry.getValue();
            if(value instanceof Map) {
                TreeMap sortMap = sortMap((Map<String, Object>) value);
                map.put(entry.getKey(), sortMap);
            } else if(value instanceof ArrayList){
                ArrayList linkedArrayList = sortList((ArrayList) value);
                map.put(entry.getKey(), linkedArrayList);
            }
        }
        return gson.fromJson(gson.toJson(map), treeMap.getClass());
    }

    private static ArrayList sortList(ArrayList value) {
        ArrayList list = new ArrayList();
        if(value.size() == 0) return null;
        for(int i = 0; i < value.size(); i++) {
            Object o = value.get(i);
            if(o instanceof Map) {
                list.add(sortMap((Map<String, Object>) o));
            }else if(o instanceof ArrayList) {
                list.add(sortList((ArrayList) o));
            }else{
                list.add(o);
            }
        }
        return list;
    }

    public static void main(String args[]) throws IOException, NoSuchAlgorithmException, NoSuchProviderException, InvalidAlgorithmParameterException, CipherException {
        String filePath = Utils.generateECKeyPair("/Users/erhu/temp", "123");
        String publicKey = Utils.getPublicKey("/Users/erhu/temp/" + filePath, "123");
        System.out.println(publicKey);
    }

}
