from django.urls import path
from mysite.views import *

urlpatterns = [
    path("", index, name="index"),
    path("main/", main, name="main"),
    path("reg/", reg, name="reg"),
]
