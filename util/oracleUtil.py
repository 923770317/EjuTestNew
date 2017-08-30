#coding=utf-8
import cx_Oracle

class oracleUtil():

    def __init__(self,env):
        try:
            self.conn = None
            if env == "test":
                self.conn = cx_Oracle.connect('wangbing','wangbing123','10.0.35.1:1521/testdb')
            else:
                self.conn = cx_Oracle.connect('jc_test_46','jc_test_46','10.0.35.1:1521/intedb')
            self.cursor = self.conn.cursor()
        except Exception, e:
            self.cursor.close()
            self.conn.close()
            print 'connect the oracle error'

    def select(self):
        self.cursor.execute ("SELECT * FROM mb.tb_area")

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



if __name__ == "__main__":
    orac = oracleUtil("test")
    orac.deleteCertByMemberId('1009442')
