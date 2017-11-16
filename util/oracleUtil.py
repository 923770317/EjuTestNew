#coding=utf-8
import cx_Oracle
import logging

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
        if not oracleUtil.isMemberExist(member_id):
            raise  Exception('there is no member like this id')
        sql = 'update mb.tb_cert c set c.logic_delete = 1 where c.member_id=%s and c.logic_delete = 0' % member_id
        oracleUtil.cursor.execute(sql)
        oracleUtil.conn.commit()



    @staticmethod
    def deletePassWord(member_id,env):
        oracleUtil.initConandCursor(env)
        if not oracleUtil.isMemberExist(member_id):
            raise  Exception('there is no member like this id')
        sql = '''update mb.tb_operator t set t.pay_password = null ,t.lock_time = null ,t.last_error_time = null,
t.password_error_count = null,t.encrypt_strategy = null where t.member_id =%s''' % member_id
        oracleUtil.cursor.execute(sql)
        oracleUtil.conn.commit()

    @staticmethod
    def updateAccountByMemberId(member_id,amount,env):
        oracleUtil.initConandCursor(env)
        if not oracleUtil.isMemberExist(member_id):
            raise  Exception('there is no member like this id ')
        sql = 'update account.tb_account t set t.available_balance = %s where t.member_id = %s and t.account_type_id = 1' % (amount,member_id)
        oracleUtil.cursor.execute(sql)
        oracleUtil.conn.commit()

    @staticmethod
    def updateReceiptById(receipt_id,amount,env):
        oracleUtil.initConandCursor(env)
        if not oracleUtil.isReceiptExist(receipt_id):
            raise  Exception('there is no receipt like this id')
        sql = 'update account.tb_receipt t set t.available_balance = %s where t.id = %s' % (amount, receipt_id)
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
    def isMemberExist(member_id):
        sql = "select id from mb.tb_member t where t.id =%s" % member_id
        oracleUtil.cursor.execute(sql)
        result = oracleUtil.cursor.fetchall()
        if not result :
            return False
        else:
            return True

    @staticmethod
    def isReceiptExist(receipt_id):
        sql = "select id from account.tb_receipt t where t.id =%s" % receipt_id
        oracleUtil.cursor.execute(sql)
        result = oracleUtil.cursor.fetchall()
        if not result:
            return False
        else:
            return True




    @staticmethod
    def interfaceGrant(partner_id,service_code,env):
        oracleUtil.initConandCursor(env)
        serviceId = oracleUtil.getServiceId(service_code)
        if not serviceId:
            raise Exception('no serveice_id')
        sql = "insert into gateway.tb_partner_service values(%s,%s,'%s',1)" %(partner_id,serviceId,service_code)
        oracleUtil.cursor.execute(sql)
        oracleUtil.conn.commit()



if __name__ == "__main__":
    # oracleUtil.updateAccountByMemberId('1003579','2000','test')
    oracleUtil.initConandCursor('test')
    oracleUtil.isMemberExist('1003579')


