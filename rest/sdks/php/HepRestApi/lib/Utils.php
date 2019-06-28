<?php

namespace HepRestApi;

use Elliptic\EC;
use kornrunner\Keccak;
use Sop\CryptoEncoding\PEM;
use Sop\CryptoTypes\Asymmetric\EC\ECPrivateKey;
use StephenHill\Base58;

class Utils
{
    static $SUPPORT_SIGNATURE_METHODS = array('HMAC-MD5');
    /**
     * 签名前的相关数据的预处理
     * @param $data
     * @return string
     */
    static function generate_md5($data)
    {
        return md5($data);
    }

    static function generate_signature_base_string($data, $joint)
    {
        $sign_string = '';
        $sign_fields = array('dapp_signature_method', 'dapp_signature', 'signature', 'sign_type');
        $n           = 0;

        $data = self::sort_array_by_key($data);
        foreach ($data as $key => $val) {
            if (in_array($key, $sign_fields)) {
                continue;
            }
            if ($n != 0) {
                $sign_string = $sign_string . $joint;
            }
            $n = $n + 1;
            if (is_array($val)) {
                $sign_string = $sign_string . $key . "=" . json_encode($val);
            } else {
                $sign_string = $sign_string . $key . "=" . $val;
            }
        }
        return $sign_string;
    }

    /**
     * 加密式处理预备签名的字符串
     * @param array $data 加签的有规则的数组
     * @param string $secret 哈希的密钥
     * @param string $prefix 前缀
     * @param bool $use_urlencode url处理的逻辑值
     * @param string $joint 连接符
     * @param string $signature_method 哈希方法
     * @return string
     */
    static function sign_hmac($data, $secret, $prefix = '', $use_urlencode = False, $joint = '&', $signature_method = 'HMAC-MD5')
    {
        if (!in_array($signature_method, self::$SUPPORT_SIGNATURE_METHODS)) {
            echo "Unsupported signature method";
            exit();
        }
        $sign_string = $prefix;
        $sign_string = $sign_string . self::generate_signature_base_string($data, $joint);
        $sign_string = $sign_string . $secret;
        if ($use_urlencode) {
            $sign_string = urlencode($sign_string);
        }
        $signed_string = self::generate_md5($sign_string);
        return $signed_string;
    }

    //生成密钥对
    static function getkeys()
    {
        $ec      = new EC('p256');
        $key     = $ec->genKeyPair();
        $privkey = $key->getPrivate();
        $pubkey  = $key->getPublic();
        $arr[]   = $privkey->jsonSerialize();
        $x       = $pubkey->getX()->jsonSerialize();
        $y       = $pubkey->getY()->jsonSerialize();

        if (strlen($x) < 64) {
            $x = str_pad($x, 64, "0", STR_PAD_LEFT);
        }

        if (strlen($y) < 64) {
            $y = str_pad($y, 64, "0", STR_PAD_LEFT);
        }

        $public_key = "0x" . $x . $y;
        $arr[]      = $public_key;
        return $arr;
    }

    //加签名
    static function sign($msg, $privkey)
    {
        $ec = new EC('p256');
        if (is_string($msg)) {
            $msg = Keccak::hash($msg, 256);
        }
        $signature = $ec->sign($msg, $privkey);
        $derSign   = $signature->toDER('hex');
        $darr[]    = $signature->r->jsonSerialize();
        $darr[]    = $signature->s->jsonSerialize();
        $darr[]    = $derSign;
        $darr[]    = "0x" . $signature->r->jsonSerialize() . $signature->s->jsonSerialize();
        return $darr;
    }

    //获取公钥
    static function getpubkeyformsign($msg, $r, $s)
    {
        $sign      = array();
        $sign['r'] = $r;
        $sign['s'] = $s;
        $ec        = new EC('p256');

        for ($l = 0; $l < 2; $l++) {
            $sign['recoveryParam'] = $l;

            $pubkeyobj = $ec->recoverPubKey($msg, $sign, $l, false);
            $x         = $pubkeyobj->getX()->jsonSerialize();
            $y         = $pubkeyobj->getY()->jsonSerialize();

            if (strlen($x) < 64) {
                $x = str_pad($x, 64, "0", STR_PAD_LEFT);
            }
            if (strlen($y) < 64) {
                $y = str_pad($y, 64, "0", STR_PAD_LEFT);
            }

            $arrs[] = "0x" . $x . $y;
        }

        return $arrs;
    }

    //验证签名
    static function verify($msg, $r, $s, $public_key)
    {
        if (is_string($msg)) {
            $msg = Keccak::hash($msg, 256);
        }

        $pukarr = self::getpubkeyformsign($msg, $r, $s);

        if (in_array($public_key, $pukarr)) {
            return true;
        } else {
            return false;
        }
    }

    /**
     * Validate the newid signature
     * @param string $r The r part hex string for signature
     * @param string $s The s part hex string for signature
     * @param string $message The message which signed
     * @param string $newid The user's newid
     * @param int $chain_id The NewChain id. The dev environment is 1002, test is 1007, main is 1012
     * @return bool
     */
    static function validate_newid($r, $s, $message, $newid, $chain_id)
    {
        if (is_string($message)) {
            $message = Keccak::hash($message, 256);
        }

        $public_keys = self::getpubkeyformsign($message, $r, $s);

        foreach ($public_keys as $pub_key) {
            $temp = self::newid_encode_by_public_key($pub_key, $chain_id);
            if ($temp == $newid) {
                return true;
            }
        }
        return false;
    }

    /**
     * generate newid by public key
     * @param string $public_key The public key of newid
     * @param string $chain_id The blockchain ID
     * @return string The encoded newid
     */
    static function newid_encode_by_public_key($public_key, $chain_id)
    {
        if (strpos($public_key, '0x') === 0) {
            $public_key = substr($public_key, 2);
        }
        if (strlen($public_key) < 64) {
            $public_key = str_pad($public_key, 64, "0", STR_PAD_LEFT);
        }

        $data = Keccak::hash(hex2bin($public_key), 256);

        $hex_chainID = substr(dechex($chain_id), -8);

        if ((strlen($hex_chainID) % 2) == 1) {
            $hex_chainID = '0' . $hex_chainID;
        }
        $num_sum = $hex_chainID . $data;

        $version_byte = hex2bin("00");
        $num_byte = hex2bin($num_sum);
        $hash_data = $version_byte.$num_byte;
        $first_hash_data = hash("sha256", $hash_data, true);
        $second_hash_data = hash("sha256", $first_hash_data, true);
        $check_sum = substr($second_hash_data, 0, 4);
        $final_data = $hash_data.$check_sum;

        $base58 = new Base58();
        $encode = $base58->encode($final_data);
        $newid = 'NEWID' . $encode;
        return $newid;
    }

    static function getBytes($string)
    {
        $bytes = array();
        for ($i = 0; $i < strlen($string); $i++) {
            $bytes[] = ord($string[$i]);
        }
        return $bytes;
    }

    static function asc2bin($string)
    {
        $len = strlen($string);
        $data = '';
        for ($i = 0; $i < $len; $i++) {
            $data .= sprintf('%08b', ord(substr($string, $i, 1)));
        }
        return $data;
    }

    /**
     * 多维数组按键排序
     * @param $data
     * @param string $sort_type
     * @return mixed
     */
    static function sort_array_by_key($data, $sort_type = 'ASC')
    {
        $sort_methon = $sort_type == 'ASC' ? 'ksort' : 'krsort';
        $sort_methon($data);
        foreach ($data as &$value) {
            if (is_array($value)) {
                $value = self::sort_array_by_key($value, $sort_type);
            }
        }
        return $data;
    }

    /**
     * 从私钥文件中获取
     * @param $file_path
     * @return string
     */
    static function get_private_key_from_file($file_path)
    {
        try {
            $priv_pem = PEM::fromFile($file_path);
            $ec_priv_key = ECPrivateKey::fromPEM($priv_pem);
            $ec_priv_seq = $ec_priv_key->toASN1();
            $priv_key_hex = bin2hex($ec_priv_seq->at(1)->asOctetString()->string());
            return $priv_key_hex;
        } catch (\Exception $e) {
            return '';
        }
    }
}