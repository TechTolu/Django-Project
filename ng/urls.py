from django.urls import path
from django.http import HttpResponse
from . import views

urlpatterns = [
    path('login', views.ng_login),
    path('register', views.ng_register)
]
