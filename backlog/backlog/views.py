from django.http import HttpResponse
from django.shortcuts import render


def index1(request):
    return render(request, 'index1.html')


def otp(request):
    return render(request, 'otp.html')


def display_information(request):
    return render(request, 'display_information.html')
