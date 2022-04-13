from django.urls import path
from django.http import HttpResponse
from . import views

urlpatterns = [
    path('login', views.eu_login),
    path('register', views.eu_register),
]
