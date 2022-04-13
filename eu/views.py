# from django.shortcuts import render
# from django.http import HttpResponse

# def eu_login(request):
#     return HttpResponse("You successfully logged in, in Europe")

# def eu_register(request):
#     return HttpResponse("Fill in your details, for European nations")

from django.shortcuts import render

def eu_login(request):
    return render(request, "register.html")

def eu_register(request):
    return render(request, "register.html")