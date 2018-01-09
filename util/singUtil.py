#coding:utf-8

import cgi, base64
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA
import requests
import json
import hashlib
from util.Constants import Constants as const


# rsa sign
def rsa_sign(data):
    key = RSA.importKey(const.private_key)
    h = SHA.new(data)
    signer = PKCS1_v1_5.new(key)
    signature = signer.sign(h)
    return base64.b64encode(signature)

#md5 sign
def md5_sign(data):
    md5 = hashlib.md5()
    sing_bytes_utf8 = data.encode(encoding='utf-8')
    md5.update(sing_bytes_utf8)
    return md5.hexdigest()