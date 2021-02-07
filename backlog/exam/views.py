# from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
import requests
import json
from .models import student_details, details
from .forms import s_form


def index(request):

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

    return render(request, 'index.html')


def otp(request):
    return render(request, 'otp.html')


def display_information(request):

    context = {}
    form = s_form()
    context['form'] = form
    if request.GET:
        temp = request.GET['dept']
        temp1 = request.GET['exam_type']
        temp2 = request.GET['sem']
        temp3 = request.GET['subject']
        temp4 = request.GET['subject_code']
        print(temp)
        print(temp1)
        print(temp2)
        print(temp3)
        print(temp4)
    return render(request, "display_information.html", context)
