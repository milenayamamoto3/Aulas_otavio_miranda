# Create your views here.

# from django.http import HttpResponse

# def blog(request):
#     print("blog")
#     return HttpResponse("blog do app")


# def exemplo(request):
#     print("exemplo")
#     return HttpResponse("exemplo do app 1")

from django.shortcuts import render


def blog(request):
    print("blog")
    return render(request, "blog/index.html")


def exemplo(request):
    print("exemplo")
    return render(request, "blog/example.html")
