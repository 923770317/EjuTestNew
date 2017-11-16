#-- coding: utf-8 --
import configparser
import os

class confUtil():

    conf = None

    @staticmethod
    def initConf():
        confUtil.conf = configparser.ConfigParser()
        # confUtil.conf.read(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'cong.ini'))
        confUtil.conf.read('C:/Users/zc/PycharmProjects/EjuTest/cong.ini')
    @staticmethod
    def getSections():
        sections = confUtil.conf.sections()
        return sections

    @staticmethod
    def getOptions(section_name):
        return confUtil.conf.options(section_name)

    @staticmethod
    def getValues(section_name,option_name):
        return confUtil.conf.get(section_name,option_name)

    @staticmethod
    def getParameters(section_name, option_name):
        paramers = confUtil.getValues(section_name, option_name)
        return str(paramers).split(',')


if __name__ == "__main__":
    confUtil.initConf()
    print confUtil.getValues('100001','queryAccount')

