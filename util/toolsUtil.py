import urllib,urllib2


def refreshAccount():
    url = 'https://test2.ejupay.cn/account-inrpc/balanceAuth/account?memberId=124487'
    req = urllib2.Request(url)
    print req
    res_data = urllib2.urlopen(req)
    res = res_data.read()
    print res



if __name__ == "__main__":
    refreshAccount()