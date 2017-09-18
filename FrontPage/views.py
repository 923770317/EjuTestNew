#-*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render_to_response
from models import ReleaseVersion
import sys
sys.path.append("/util")
from util import oracleUtil as ou
from util import toolsUtil

# Create your views here.

# releaseVersion's index
def releaseIndex(request):

    modelName = request.GET.get("searchText")
    reObjects = None
    if modelName:
        reObjects = ReleaseVersion.objects.filter(mod__icontains=modelName).order_by("-lastOnLineDate")
    else:
        reObjects = ReleaseVersion.objects.all().order_by("-lastOnLineDate")


    return render_to_response('releaseIndex.html',{'reObjects':reObjects})

# log in the index
def index(request):
    return render_to_response("index.html")


#delete the password
def deletePassWord(request):
    if str(request.method) == "POST":
        member_id = request.POST.get("memberId")
        env = request.POST.get("env")
        oracle_Util = None
        resultCode = ""
        if member_id is None:
            resultCode = "member_id is required"
        if env == "test":
            oracle_Util = ou.oracleUtil("test")
        else:
            oracle_Util = ou.oracleUtil("inte")
        resultCode = oracle_Util.deletePassWord(member_id)
        return HttpResponse(resultCode)

    else:
        return render_to_response("deletePassWord.html")


#delete the cert
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


#update the account's amount
def updateAccount(request):
    if str(request.method) == 'POST':
        member_id = request.POST.get("memberId")
        env = request.POST.get("env")
        amount = request.POST.get('amount')
        oracle_Util = None
        resultCode = ""
        if member_id is None or amount is None:
            return 'pls enter the para'

        if env == "test":
            oracle_Util = ou.oracleUtil("test")
        else:
            oracle_Util = ou.oracleUtil("inte")
        resultCode = oracle_Util.updateAccountByMemberId(member_id,amount)
        toolsUtil.refreshAccountByMemberId(member_id,env)
        return HttpResponse(resultCode)
    return render_to_response("updateAccount.html")

#udpate the receipt's amount
def updateReceiptAmount(request):
    if str(request.method) == 'POST':
        receipt_id = request.POST.get('receiptId')
        env = request.POST.get('env')
        amount = request.POST.get('amount')
        oracle_Util = None
        resultCode = ""
        if receipt_id is None or amount is None:
            return 'pls enter the para'

        if env == "test":

            oracle_Util = ou.oracleUtil("test")
        else:
            oracle_Util = ou.oracleUtil("inte")

        resultCode = oracle_Util.updateReceiptById(receipt_id, amount)
        toolsUtil.refreshReceiptById(receipt_id, env)
        return HttpResponse(resultCode)
    return render_to_response('updateReceipt.html')


def interfaceGrant(request):
    if str(request.method) == 'POST':
        partner_id = request.POST.get("partner_id")
        service_code = request.POST.get('serviceCode')
        env = request.POST.get('env')
        oracle_Util = None
        resultCode = ''
        


    return render_to_response('interfaceGrant.html')