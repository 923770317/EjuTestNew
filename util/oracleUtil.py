import cx_Oracle

class oracleUtil():

    def __init__(self,env):
        self.conn = None
        if env == "test":
            conn = cx_Oracle.connect('cs_test_44/cs_test_444/testdb')
        else:
            conn = cx_Oracle.connect('jc_test_46/jc_test_46/intedb')

        self.cursor = conn.cursor()

    def select(self):
        self.cursor.execute ("SELECT * FROM TEST")


if __name__ == "__main__":
    orac = oracleUtil("test")
    orac.select()
