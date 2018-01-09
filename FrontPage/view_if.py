#coding=utf-8
from django.http import JsonResponse
from util.confUtil import confUtil


#get the option of section
def getOption(scetion_name):
    return confUtil.getOptions(scetion_name)

def getSections():
    return confUtil.getSections()


def getParametres(section_name,option_name):
    return confUtil.getParameters(section_name,option_name)
