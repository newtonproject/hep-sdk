<?php
ini_set("display_errors", "On");
error_reporting(E_ALL | E_STRICT);
$SUPPORT_SIGNATURE_METHODS = array('HMAC-MD5');
require_once "vendor/autoload.php";
use Elliptic\EC;
use kornrunner\Keccak;
/**
	签名前的相关数据的预处理
**/
function generate_md5($data){
	return bin2hex(md5($data));
}
//数组按照一定规则进行处理为字符串
//$data $joint :$data是数组  $joint是连接符
function generate_signature_base_string($data, $joint){
    $sign_string = '';
    $sign_fields = array('dapp_signature_method', 'dapp_signature', 'signature', 'sign_type');
	$n = 0;
	foreach($data as $key=>$val){
		if(in_array($key,$sign_fields)){
			continue;
		}
		if($n!=0){
			$sign_string = $sign_string.$joint;
		}
		$n = $n+1;
		if(is_array($val)){
			$sign_string = $sign_string.$key."=".json_encode($val);
		}else{
			$sign_string = $sign_string.$key."=".$val;
		}
	}
	return $sign_string;
}
//加密式处理预备签名的字符串
//参数:
// $data 加签的有规则的数组
// $secret 哈希的密钥
// $prefix 前缀
// $user_urlencode url处理的逻辑值
// $joint 连接符
// $signature_method  哈希方法
function  sign_hmac($data, $secret, $prefix='', $use_urlencode=False, $joint='&', $signature_method='HMAC-MD5'){
	if(!in_array($SUPPORT_SIGNATURE_METHODS)){
		echo "Unsupported signature method";
		exit();
	}
    $sign_string = $prefix;
    $sign_string = $sign_string.generate_signature_base_string($data, $joint);
    $sign_string = $sign_string.$secret;
    if($use_urlencode){
        $sign_string = urlencode($sign_string);
	}
    $signed_string = generate_md5($sign_string);
    return $signed_string;
}
//生成密钥对
function getkeys(){	
	$ec = new EC('p256');
	$key = $ec->genKeyPair();
	$privkey = $key->getPrivate();
	$pubkey = $key->getPublic();
	$arr[] = $privkey->jsonSerialize();
	$x = $pubkey->getX()->jsonSerialize();
	$y = $pubkey->getY()->jsonSerialize();
	if(strlen($x)<64){
		$prefix = "";
		for($i=0;$i<(64-strlen($x));$i++){
			$prefix = $prefix."0";
		}
		$x = $prefix.$x;
	}
	if(strlen($y)<64){
		$prefix = "";
		for($i=0;$i<(64-strlen($x));$i++){
			$prefix = $prefix."0";
		}
		$y = $prefix.$y;
	}
	$public_key = "0x".$x.$y;
	$arr[] = $public_key;
	return $arr;
}
//加签名
function sign($msg,$privkey){
	$ec = new EC('p256');
	if(is_string($msg)){
		$msg = Keccak::hash($msg, 256);
	}
	$signature = $ec->sign($msg,$privkey);
	$derSign = $signature->toDER('hex');
	$darr[] = $signature->r->jsonSerialize();
	$darr[] = $signature->s->jsonSerialize();
	$darr[] = $derSign;
	$darr[] = "0x".$signature->r->jsonSerialize().$signature->s->jsonSerialize();
	return $darr;
}
//获取公钥
function getpubkeyformsign($msg,$r,$s){
	$sign = array();
	$sign['r'] = $r;
	$sign['s'] = $s;
	$ec = new EC('p256');
	 for($l=0;$l<2;$l++){
		$sign['recoveryParam'] = $l;
		$pubkeyobj = $ec->recoverPubKey($msg,$sign,$l,false);
		$x = $pubkeyobj->getX()->jsonSerialize();
		$y = $pubkeyobj->getY()->jsonSerialize();
			if(strlen($x)<64){
			$prefix = "";
			for($i=0;$i<(64-strlen($x));$i++){
				$prefix = $prefix."0";
			}
			$x = $prefix.$x;
		}
		if(strlen($y)<64){
			$prefix = "";
			for($i=0;$i<(64-strlen($x));$i++){
				$prefix = $prefix."0";
			}
			$y = $prefix.$y;
		}
		$arrs[]= "0x".$x.$y;
	}
	return $arrs;
}
//验证签名
function verify($msg,$r,$s,$public_key){
	if(is_string($msg)){
		$msg = Keccak::hash($msg, 256);
	}
	$pukarr = getpubkeyformsign($msg,$r,$s);
	if(in_array($public_key,$pukarr)){
		return true;
	}else{
		return false;
	}
}
	$arr = getkeys();
	$privkey = $arr[0];
	$pubkey = $arr[1];
	echo "私钥：".$privkey."<br>";
	echo "公钥：".$pubkey."<br>";
	$msg = "message";
	$signrs = sign($msg,$privkey);
	echo "R：".$signrs[0]."<br>";
	echo "S：".$signrs[1]."<br>";
	echo "处理签名：".$signrs[2]."<br>";
	echo "自定义处理签名：".$signrs[3]."<br>";
	$rs = verify($msg,$signrs[0],$signrs[1],$pubkey);
	echo "验签:".$rs;
?>