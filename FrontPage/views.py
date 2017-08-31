#-*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render_to_response
from models import ReleaseVersion
import sys
sys.path.append("/util")
from util import oracleUtil as ou

# Create your views here.

# releaseVersion 模块首页
def releaseIndex(request):

    modelName = request.GET.get("searchText")
    reObjects = None
    if modelName:
        reObjects = ReleaseVersion.objects.filter(mod__icontains=modelName).order_by("-lastOnLineDate")
    else:
        reObjects = ReleaseVersion.objects.all().order_by("-lastOnLineDate")


    return render_to_response('releaseIndex.html',{'reObjects':reObjects})

# 登录后首页
def index(request):
    return render_to_response("index.html")


#删除支付密码
def deletePassWord(request):
    if str(request.method) == "POST":
        member_id = request.POST.get("memberId")
        env = request.POST.get("optionsRadios")
        oracle_Util = None
        resultCode = ""
        if member_id is None:
            resultCode = "member_id is required"
        if env == "test":
            oracle_Util = ou.oracleUtil("test")
        else:
            oracle_Util = ou.oracleUtil("inte")

    else:
        return render_to_response("deletePassWord.html")


#删除实名认证
def deleteCert(request):
    if str(request.method) == "POST":
        member_id = request.POST.get("memberId")
        env = request.POST.get("env")
        oracle_Util = None
        resultCode = ""
        if member_id is None:
            resultCode =  "member_id is required"

        if env == "test":
            oracle_Util = ou.oracleUtil("test")
        else:
            oracle_Util = ou.oracleUtil("inte")

        resultCode = oracle_Util.deleteCertByMemberId(member_id)

        return HttpResponse(resultCode)
    else:
        return render_to_response("deleteCert.html")