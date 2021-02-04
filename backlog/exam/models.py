from django.db import models

# Create your models here.


class student_details(models.Model):
    USN = models.CharField(max_length=11)
    MOBILE = models.IntegerField()
    EMAIL = models.EmailField(max_length=34)
