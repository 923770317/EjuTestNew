#-*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render_to_response
from models import ReleaseVersion

# Create your views here.

# releaseVersion 模块首页
def releaseIndex(request):

    reObjects = ReleaseVersion.objects.all()

    return render_to_response('releaseIndex.html',{'reObjects':reObjects})

# 登录后首页
def index(request):
    return render_to_response("index.html")


#删除支付密码
def deletePassWord(request):
    memberId = request.REQUEST.get("memberId")
    env = request.REQUEST.get("env")
