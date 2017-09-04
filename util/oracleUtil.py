#coding=utf-8
import cx_Oracle

class oracleUtil():

    def __init__(self,env):
        try:
            self.conn = None
            if env == "test":
                self.conn = cx_Oracle.connect('wangbing','wangbing123','10.0.35.1:1521/testdb')
            else:
                self.conn = cx_Oracle.connect('wangbing','wangbing123','10.0.35.1:1521/intedb')
            self.cursor = self.conn.cursor()
        except Exception, e:
            self.cursor.close()
            self.conn.close()
            print 'connect the oracle error'




    def deleteCertByMemberId(self,member_id):
        resultCode = '000'
        try:
            sql = 'update mb.tb_cert c set c.logic_delete = 1 where c.member_id=%s' % member_id
            self.cursor.execute(sql)
            self.conn.commit()
        except Exception,e:
            print "delete memberis cert err",str(e)
            resultCode = '999'
        finally:
            self.cursor.close()
            self.conn.close()
            return resultCode


    def deletePassWord(self,member_id):
        resultCode = '000'
        try:
            sql = '''update mb.tb_operator t set t.pay_password = null ,t.lock_time = null ,t.last_error_time = null,
t.password_error_count = null,t.encrypt_strategy = null where t.member_id =%s''' % member_id
            self.cursor.execute(sql)
            self.conn.commit()
        except Exception, e:
            print "delete password err", str(e)
            resultCode = '999'
        finally:
            self.cursor.close()
            self.conn.close()
            return resultCode

    def updateAccountByMemberId(self,memberId,amount):
        resultCode = '000'
        try:
            sql = 'update account.tb_account t set t.available_balance = %s where t.member_id = %s and t.account_type_id = 1' % (amount,memberId)
            self.cursor.execute(sql)
            self.conn.commit()

        except Exception, e:
            print "delete password err", str(e)
            resultCode = '999'

        finally:
            self.cursor.close()
            self.conn.close()
            return resultCode



if __name__ == "__main__":
    orac = oracleUtil("test")
    orac.deleteCertByMemberId('1009442')
