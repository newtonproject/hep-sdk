<?php

namespace HepRestApi;

use Elliptic\EC;
use kornrunner\Keccak;

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
            $prefix = "";
            for ($i = 0; $i < (64 - strlen($x)); $i++) {
                $prefix = $prefix . "0";
            }
            $x = $prefix . $x;
        }

        if (strlen($y) < 64) {
            $prefix = "";
            for ($i = 0; $i < (64 - strlen($x)); $i++) {
                $prefix = $prefix . "0";
            }
            $y = $prefix . $y;
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
            $pubkeyobj             = $ec->recoverPubKey($msg, $sign, $l, false);
            $x                     = $pubkeyobj->getX()->jsonSerialize();
            $y                     = $pubkeyobj->getY()->jsonSerialize();
            if (strlen($x) < 64) {
                $prefix = "";
                for ($i = 0; $i < (64 - strlen($x)); $i++) {
                    $prefix = $prefix . "0";
                }
                $x = $prefix . $x;
            }
            if (strlen($y) < 64) {
                $prefix = "";
                for ($i = 0; $i < (64 - strlen($x)); $i++) {
                    $prefix = $prefix . "0";
                }
                $y = $prefix . $y;
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
}