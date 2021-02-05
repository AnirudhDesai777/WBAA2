# from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
import requests
import json
from .models import student_details, details


def index1(request):

    if request.method == "POST":
        student_usn = request.POST.get('USN')
        student_mobile = request.POST.get('MOBILE')
        student_email = request.POST.get('EMAIL')

        post = student_details()
        # if student_usn.exists() == False:

        post.USN = student_usn
        post.MOBILE = student_mobile
        post.EMAIL = student_email
        post.save()

        print(request.POST.get('USN'))
        print(request.POST.get('MOBILE'))
        print(request.POST.get('EMAIL'))

    return render(request, 'index1.html')
    # else:
    #     return render(request, 'index.html', {"message": "The Student details already exists..."})


def otp(request):
    return render(request, 'otp.html')


def display_information(request):
    return render(request, 'display_information.html')
