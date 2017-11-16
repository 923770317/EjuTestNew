#coding=utf-8
import urllib,urllib2
from confUtil import confUtil
import requests
import json

def refreshAccount():
    url = 'https://test2.ejupay.cn/account-inrpc/balanceAuth/account?memberId=124487'
    req = urllib2.Request(url)
    print req
    res_data = urllib2.urlopen(req)
    res = res_data.read()
    print res



def refreshAccountByMemberId(memberId,env):
    url = ''
    if env == 'test':
        url = 'https://test2.ejupay.cn/account-inrpc/balanceAuth/account?memberId=%s' % memberId
    else:
        url = 'https://inte.ejupay.cn/account-inrpc/balanceAuth/account?memberId=%s' % memberId
    try:
        req = urllib2.Request(url)
        res_data = urllib2.urlopen(req)
    except Exception as e:
        print str(e)

def refreshReceiptById(receiptId,env):
    url = ''
    if env == 'test':
        url = 'https://test2.ejupay.cn/account-inrpc/balanceAuth/receipt?id=%s' % receiptId
    else:
        url = 'https://inte.ejupay.cn/account-inrpc/balanceAuth/receipt?id=%s' % receiptId
    try:
        req = urllib2.Request(url)
        res_data = urllib2.urlopen(req)
    except Exception as e:
        print str(e)


#组装 发送的JSON
def get_post_json(request_body):
    json = {"partner": 100001, "version": "v1.1", "requestBody": request_body ,"publicKey": "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDxAbF5OMdlj/NvI5tiohgj59N1R8MgJKJjddSCizDFJQmXU7L92iXDd+kflZpl8r7/GVswYKQGLhnm8kyrX+/daw+Ur5ianEjuXaMlJFnFZkaJGNWLx+odknLWYWnfUMEfvUy5kS2xNBXiPz9GjwNmgIj2HeeBnrIMsSmgE408mwIDAQAB", "privateKey": "MIICeQIBADANBgkqhkiG9w0BAQEFAASCAmMwggJfAgEAAoGBAPEBsXk4x2WP828jm2KiGCPn03VHwyAkomN11IKLMMUlCZdTsv3aJcN36R+VmmXyvv8ZWzBgpAYuGebyTKtf791rD5SvmJqcSO5doyUkWcVmRokY1YvH6h2SctZhad9QwR+9TLmRLbE0FeI/P0aPA2aAiPYd54GesgyxKaATjTybAgMBAAECgYEAplzL3GjUQ4hNux8yKLDJxydE8YU67Vo8ejmhGwfn/35kk4AkY1UNklOYqcPEU7FwJHmlV8yuDNIP8Tq6r+XGlZNN8fc2BQ8RuCdASpJ21wrDVJdpy/gAs5hylAXkod0Fa5Pf6Yegu2YtKwKaVI/DzNaIIG/Zebnye13KAQuNPOkCQQD9gc09SkHQPcymhKtzcE9hPbWAo656Xo2/WaNaMQyueeA/Qe7gJ0jDxwZMOXWee84Km/8ndNudtXCgS/GdS7L1AkEA82BsCGaqwOE+Zm1dvODIfPRSlIgEnyLXedXCpZHFDItAo7F54VsMB8wn8W4/wBUUeNzfA78hR3djOKsHu4kXTwJBAOagff1yXul6L4KWU/xTgoPuxf7f6k29U6tveyMEWIsqqY4jB5S5aINjvyD9bTnfXBVe0gQtVdbmSC4sqQT25zkCQQC0KgXvdikjndq2snF4+CIStj9HqyVYtM80ZvSv4qgvcAqK4z/pfp/6Sbyr8kSJKlG8Yy1Itb2qDQxLj/iqcILrAkEAqvOfjxgWL4mx3MVvyAKHXTry4Wa1gZV3bZJqtSMnm9JDg3Nv8cn90CcUS2/saLZMefziJ7EVb//0WNqBu+QmWg==", "algorithm": 2, "signature": "", "sign": ""}
    return json


#发送POST 请求
def post_request(env,json):
    url = ''
    if env == 'test':
        url = 'https://test2.ejupay.cn/gateway-mock/mock/doMock'
    else:
        url = 'https://inte2.ejupay.cn/gateway-mock/mock/doMock'
    r = requests.post(url,json)

    return r.text


if __name__ == "__main__":
    # refreshAccount()
    # getParamesrs

    print post_request(json)