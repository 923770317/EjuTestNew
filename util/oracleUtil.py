#coding=utf-8
import cx_Oracle

class oracleUtil(object):
    conn = None
    cursor = None



    @staticmethod
    def initConandCursor(env):
        if env == "test":
            oracleUtil.conn = cx_Oracle.connect('wangbing', 'wangbing123', '10.0.35.1:1521/testdb')
        else:
            oracleUtil.conn = cx_Oracle.connect('wangbing', 'wangbing123', '10.0.35.1:1521/intedb')
        oracleUtil.cursor = oracleUtil.conn.cursor()

    @staticmethod
    def deleteCertByMemberId(member_id,env):
        oracleUtil.initConandCursor(env)
        sql = 'update mb.tb_cert c set c.logic_delete = 1 where c.member_id=%s' % member_id
        oracleUtil.cursor.execute(sql)
        oracleUtil.conn.commit()



    @staticmethod
    def deletePassWord(member_id,env):
        oracleUtil.initConandCursor(env)
        sql = '''update mb.tb_operator t set t.pay_password = null ,t.lock_time = null ,t.last_error_time = null,
t.password_error_count = null,t.encrypt_strategy = null where t.member_id =%s''' % member_id
        oracleUtil.cursor.execute(sql)
        oracleUtil.conn.commit()

    @staticmethod
    def updateAccountByMemberId(memberId,amount,env):
        oracleUtil.initConandCursor(env)
        sql = 'update account.tb_account t set t.available_balance = %s where t.member_id = %s and t.account_type_id = 1' % (amount,memberId)
        oracleUtil.cursor.execute(sql)
        oracleUtil.conn.commit()

    @staticmethod
    def updateReceiptById(receiptId,amount,env):
        oracleUtil.initConandCursor(env)
        sql = 'update account.tb_receipt t set t.available_balance = %s where t.id = %s' % (amount, receiptId)
        oracleUtil.cursor.execute(sql)
        oracleUtil.conn.commit()

    @staticmethod
    def getServiceId(service_code):
        serviceId = ''
        sql = "select service_id from gateway.tb_partner_service where code = '%s' and rownum <=1" % service_code
        oracleUtil.cursor.execute(sql)
        while (1):
            row = oracleUtil.cursor.fetchone()
            if row == None:
                break
            serviceId = row[0]
        return str(serviceId)





    @staticmethod
    def interfaceGrant(partner_id,service_code,env):
        oracleUtil.initConandCursor(env)
        serviceId = oracleUtil.getServiceId(service_code)
        if not serviceId:
            raise Exception('no serveice_id')
        sql = "insert into gateway.tb_partner_service values(%ks,%s,'%s',1)" %(partner_id,serviceId,service_code)
        oracleUtil.cursor.execute(sql)
        oracleUtil.conn.commit()



if __name__ == "__main__":
    orac = oracleUtil("test")
    orac.deleteCertByMemberId('1009442')
