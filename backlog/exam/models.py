from django.db import models

# Create your models here.


class student_details(models.Model):
    USN = models.CharField(max_length=11, primary_key=True, editable=False)
    MOBILE = models.IntegerField(null=False, editable=False)
    EMAIL = models.EmailField(max_length=32, default="", editable=False)


class details(models.Model):
    s_usn = models.CharField(max_length=11, primary_key=True, editable=False)
    s_mobile = models.IntegerField(editable=False)
    s_email = models.EmailField(max_length=32, default="", editable=False)
