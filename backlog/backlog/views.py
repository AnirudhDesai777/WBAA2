from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def otp(request):
    return render(request, 'otp.html')


def display_information(request):
    return render(request, 'display_information.html')
