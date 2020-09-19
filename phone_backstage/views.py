from django.shortcuts import render
import urllib
from bs4 import BeautifulSoup
from .models import *
import json
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.db import connection

import logging
logger = logging.getLogger("console")#配置日志


def china(request):
    json_list = []
    goods = phone_test.objects.all()
    for good in goods:
        json_dict = {}
        aa = good.country
        if aa.rstrip() == "+86":
            json_dict["country"] = good.country
            json_dict["phone"] = good.phone
            json_dict["information_url"] = good.information_url
            json_list.append(json_dict)
        else:
            pass
    return JsonResponse({"json_list": json_list})


def overseas(request):
    json_list = []
    goods = phone_test.objects.all()
    for good in goods:
        json_dict = {}
        aa = good.country
        if aa.rstrip() == "+86":
            pass
        else:
            json_dict["country"] = good.country
            json_dict["phone"] = good.phone
            json_dict["information_url"] = good.information_url
            json_list.append(json_dict)
    return JsonResponse({"json_list": json_list})

def information(request,):
    phone="17190077130"
    phone_dat = phone_test.objects.values().get(phone=phone)
    #print(goods["information_url"])
    url=phone_dat["information_url"]+phone
    page = urllib.request.urlopen(url)
    html = page.read().decode('utf-8')
    # print(html)
    bs = BeautifulSoup(html, "html.parser")
    nr = bs.find(class_="container")
    #print(nr)
    return HttpResponse(html)
