#-*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render_to_response
from models import ReleaseVersion
from models import ProdectSiste
import sys
sys.path.append("/util")
from util import oracleUtil as ou
from util import toolsUtil
from django.http import JsonResponse
from cx_Oracle import DatabaseError
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

#线上应用分布
def productSites(request):
    modelName = request.GET.get("searchText")
    reObjects = None
    if modelName:
        reObjects =  ProdectSiste.objects.filter(modeleNmae__icontains=modelName)
    else:
        reObjects = ProdectSiste.objects.all().order_by("modeleNmae")

    return render_to_response('productSites.html',{'reObjects':reObjects})


# log in the index
def index(request):
    return render_to_response("index.html")


#delete the password
def deletePassWord(request):
    if str(request.method) == "POST":
        status = '000'
        message = 'DELETE PASSWORD SUCCESS'
        member_id = request.POST.get("memberId")
        env = request.POST.get("env")
        if not member_id:
            return JsonResponse({'status': '777', 'message': 'member_id is null'})
        try:
            ou.oracleUtil.deletePassWord(member_id,env)
        except DatabaseError as e:
            status = '999'
            message = str(e)
            return JsonResponse({'status': status, 'message': message})
        except Exception as e :
            status = '999'
            message = str(e)
        ou.cursor.close()
        ou.conn.close()
        return JsonResponse({'status':status,'message':message})
    else:
        return render_to_response("deletePassWord.html")


#delete the cert
def deleteCert(request):
    if str(request.method) == "POST":
        status = '000'
        message = 'DELETE CERT SUCCESS'
        member_id = request.POST.get("memberId")
        env = request.POST.get("env")
        if not member_id:
            return JsonResponse({'status': '777', 'message': 'member_id is null'})
        try:
            ou.oracleUtil.deleteCertByMemberId(member_id,env)
        except DatabaseError as e:
            status = '999'
            message = str(e)
            return JsonResponse({'status': status, 'message': message})
        except Exception as e :
            status = '999'
            message = str(e)
        ou.cursor.close()
        ou.conn.close()
        return JsonResponse({'status':status,'message':message})
    else:
        return render_to_response("deleteCert.html")

#update the account's amount
def updateAccount(request):
    if str(request.method) == 'POST':
        status = '000'
        message = 'UPDATE ACCOUNT SUCCESS'
        member_id = request.POST.get("memberId")
        env = request.POST.get("env")
        amount = request.POST.get('amount')
        if member_id == '' or amount  == '':
            return JsonResponse({'status':'999','message':'PLS ENTER THE PARAM'})
        try:
            ou.oracleUtil.updateAccountByMemberId(member_id,amount,env)
            toolsUtil.refreshAccountByMemberId(member_id, env)
        except DatabaseError as e:
            status = '999'
            message = str(e)
            return JsonResponse({'status': status, 'message': message})
        except Exception as e :
            status = '999'
            message = str(e)
        ou.cursor.close()
        ou.conn.close()
        return JsonResponse({'status':status,'message':message})
    return render_to_response("updateAccount.html")


#udpate the receipt's amount
def updateReceiptAmount(request):
    if str(request.method) == 'POST':
        status = '000'
        message = "UPDATE RECEIPT'S AMOUNT SUCCESS"
        receipt_id = request.POST.get('receiptId')
        env = request.POST.get('env')
        amount = request.POST.get('amount')
        if receipt_id == '' or amount == '':
            return JsonResponse({'status': '999', 'message': 'PLS ENTER THE PARAM'})

        try:
            ou.oracleUtil.updateReceiptById(receipt_id, amount,env)
            toolsUtil.refreshReceiptById(receipt_id, env)
        except DatabaseError as e:
            status = '999'
            message = str(e)
            return JsonResponse({'status': status, 'message': message})

        except Exception as e:
            status = '999'
            message = str(e)

        ou.cursor.close()
        ou.conn.close()
        return JsonResponse({'status': status, 'message': message})
    return render_to_response('updateReceipt.html')


#接口授权
def interfaceGrant(request):
    if str(request.method) == 'POST':
        partner_id = request.POST.get("partner_id")
        service_code = request.POST.get('service_code')
        env = request.POST.get('env')
        if service_code == '' or partner_id == '':
            return JsonResponse({'status': '999', 'message': 'PLS ENTER THE PARAM'})
        try:
            ou.oracleUtil.interfaceGrant(partner_id,service_code,env)
        except DatabaseError as e:
            status = '999'
            message = str(e)
            return JsonResponse({'status': status, 'message': message})
        except Exception as e:
            status = '999'
            message = str(e)

        ou.cursor.close()
        ou.conn.close()
        return JsonResponse({'status': status, 'message': message})
    return render_to_response('interfaceGrant.html')
