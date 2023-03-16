from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path("login",views.User_login,name="login"),
    path("registration",views.registration,name="registration"),
    path("logout",views.User_logout),
]
