package org.newtonproject.hep.rest;

import com.google.gson.Gson;
import org.newtonproject.hep.rest.utils.Base58;
import org.spongycastle.util.io.pem.PemWriter;
import org.bouncycastle.jcajce.spec.*;
import org.web3j.crypto.ECDSASignature;
import org.web3j.crypto.ECKeyPair;
import org.web3j.crypto.Hash;
import org.web3j.crypto.Sign;
import org.web3j.utils.Numeric;
import sun.security.util.Pem;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.math.BigInteger;
import java.security.MessageDigest;
import java.util.*;

public class Utils {

    static JSON json = new JSON();
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

    public static String generateSecp256r1KeyPairs(String savePath) throws IOException {
        File file = new File(savePath);
        BufferedReader reader = new BufferedReader(new FileReader(file));
        String line = null;
        StringBuilder builder = new StringBuilder();
        while ((line = reader.readLine()) != null) {
            if(!line.contains("-----")){
                builder.append(line);
            }
        }

        byte[] decode = Pem.decode(builder.toString());
        ECKeyPair keyPair = ECKeyPair.create(decode);

        System.out.println("pub:" + keyPair.getPublicKey().toString(16));
        ECKeyPair keyPair1 = ECKeyPair.create(Numeric.toBigInt("0xab76d2984444142e58cc296b632959ec3695b1e886131eb26f387dfdfea60c1f"));
        System.out.println("pub:" + keyPair1.getPublicKey().toString(16));

        return null;
    }

    public static String signSecp256r1(String message, String privateKeyPath) {
        String priv = privateKeyPath;
        Sign.SignatureData sig = Sign.signMessage(message.getBytes(), ECKeyPair.create(Numeric.toBigInt(priv)));
        String r = Numeric.toHexString(sig.getR());
        String s = Numeric.toHexStringNoPrefix(sig.getS());
        return r + s;
    }

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

    public static void main(String args[]) throws IOException {
        Utils.generateSecp256r1KeyPairs("/Users/erhu/pony/priv");
    }

}
