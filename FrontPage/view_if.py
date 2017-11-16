from django.http import JsonResponse
from util import confUtil


#get the option of section
def getOption(scetion_name):
    return confUtil.confUtil.getOptions(scetion_name)


