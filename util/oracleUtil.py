#coding=utf-8
import cx_Oracle

class oracleUtil():

    def __init__(self,env):
        try:
            self.conn = None
            if env == "test":
                conn = cx_Oracle.connect('cs_test_44','cs_test_44','10.0.35.1:1521/testdb')
            else:
                conn = cx_Oracle.connect('jc_test_46','jc_test_46','10.0.35.1:1521/intedb')
            self.cursor = conn.cursor()
        except Exception, e:
            self.cursor.close()
            self.conn.close()
            print '创建数据库链接异常'

    def select(self):
        self.cursor.execute ("SELECT * FROM mb.tb_area")

    def deleteCertByMemberId(self,member_id):
        try:
            sql = 'delete from mb.tb_cert t where t.member_id = %;' % member_id,
            self.cursor.execute(sql)
            self.conn.commit()
        except Exception,e:
            print "delete member's cert error"
        finally:
            self.cursor.close()
            self.conn.close()


if __name__ == "__main__":
    orac = oracleUtil("test")
    orac.select()
