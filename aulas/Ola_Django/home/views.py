# Create your views here.

# # from django.http import HttpResponse
# def home(request):
#     print("home")
# return HttpResponse("home <b>do</b> app")

from django.shortcuts import render


def home(request):
    print("home")

    return render(request, "home/index.html")
