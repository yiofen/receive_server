# -*-coding:utf-8-*-
import os

from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def index(request):
    return render(request, 'myApp/index.html')


def index1(request):
    return HttpResponseRedirect('/')
    

def upload(request):
    return render(request, 'myApp/upload.html')


@csrf_exempt
def save_file(request):
    if request.method == "POST":
        f = request.FILES['file']
        # 合成文件在服务器的保存位置
        file_path = os.path.join(settings.MEDIA_ROOT, f.name)
        with open(file_path, 'wb') as fp:
            # 文件分段保存
            for info in f.chunks():
                fp.write(info)

        return render(request, 'myApp/success.html')
    else:
        return render(request, 'myApp/defeat.html')


def anal_data():
    pass


def ret_data(request):
    pass

