from django.shortcuts import render
from django.http import HttpResponse


def ng_login(request):
    return HttpResponse("You successfully logged in, in Nigeria")  

def ng_register(request):
    return HttpResponse("Fill in your details, for Nigerians")

