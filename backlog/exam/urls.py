from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.index1, name="index1"),
    path('otp', views.otp, name="otp"),

    path('display', views.display_information, name="display")
]
