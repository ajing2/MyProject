import json

from django.core import serializers
from django.forms import model_to_dict
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.http import require_http_methods
from rest_framework import generics, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from saltstack.forms import AddAppForm, CheckAppForm
from saltstack.models import App, IPAddr
from saltstack.serializers import AppSerializer
from utils import resultJson
from utils.resultJson import ResultBean


def index(request):
    return HttpResponse({"hello": "salt"})

#分页
class StandardResultsSetPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 5


class AppInstall(generics.ListAPIView):
    def get(self, request):
        return render(request, 'appinstall.html')

    def post(self, request):
        resultBean = dict()
        print(request.data)
        data = request.data
        if data:
            apps = data['app']
            ips = data['ip']
            try:
                installApp = App(name=apps, ip=ips, type=1, isDelete=0)
                installApp.save()
                resultBean["code"] = 0
                resultBean["message"] = "success"
                resultBean["data"] = 1
            except Exception as e:
                resultBean["message"] = "save install app error."
                resultBean["code"] = -1
                resultBean["data"] = None
            finally:
                return JsonResponse(resultBean)
        else:
            resultBean["message"] = "form data error."
            resultBean["code"] = 400
            resultBean["data"] = None
            return JsonResponse(resultBean)


def ipList(request):
    resultBean = dict()
    if request.method == "GET":
        ipaddr = IPAddr.objects.all()
        data = serializers.serialize("json", ipaddr)
        resultBean['code']  = 0
        resultBean["message"] = "success"
        resultBean["data"] = json.loads(data)
        return JsonResponse(resultBean, safe=False)



@require_http_methods(['GET','POST'])
def login(request):
    if request.method == "GET":
        return render(request, 'login.html')



@require_http_methods(['GET','POST'])
def check(request):
    if request.method == "GET":
        return render(request, 'appcheck.html')
    else:
        resultBean = dict()
        data = CheckAppForm(request.POST)
        if data.is_valid():
            app = data.cleaned_data.get("app")
            ip = data.cleaned_data.get("ip")
            tool = data.cleaned_data.get("tool")
            print(app, ip, tool)
            print(type(app), type(ip), type(tool))
            resultBean['code'] = 0
            resultBean['message'] = "success"
            resultBean['data'] = len(app)
            return JsonResponse(resultBean)
        else:
            resultBean["code"] = 400
            resultBean["message"] = "param error"
            resultBean["data"] = None
            return JsonResponse(resultBean)