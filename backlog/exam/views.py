# from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
import requests
import json


def index1(request):

    print(request.POST.get('USN'))
    print(request.POST.get('MOBILE'))
    print(request.POST.get('EMAIL'))

    return render(request, 'index1.html')


def otp(request):
    return render(request, 'otp.html')


def display_information(request):
    return render(request, 'display_information.html')
