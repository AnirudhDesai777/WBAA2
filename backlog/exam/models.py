from django.db import models

# Create your models here.


class student_details(models.Model):
    USN = models.CharField(max_length=11,null=True,blank=True)
    MOBILE = models.IntegerField(null=True,blank=True)
    EMAIL = models.EmailField(max_length=32,null=True,blank=True)
