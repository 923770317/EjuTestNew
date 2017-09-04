#coding=utf-8
import urllib,urllib2


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

if __name__ == "__main__":
    refreshAccount()