from django.http import HttpResponse
from django.shortcuts import render
import requests
import json


def index1(request):
    # if request.method == 'POST':
    # regx1 = request.POST.get['regx1']
    print(request.POST.get('USN'))
    print(request.POST.get('MOBILE'))
    print(request.POST.get('EMAIL'))
    # usn = request.POST['usn']
    # mobile = request.POST['mobile']
    # print(mobile)
    return render(request, 'index1.html')
    # return render(request, 'index1.html', {'usn': regx1})


def otp(request):
    return render(request, 'otp.html')


def display_information(request):
    return render(request, 'display_information.html')


# def get_data(request):
