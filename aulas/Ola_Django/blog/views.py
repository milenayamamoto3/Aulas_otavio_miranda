# Create your views here.

# from django.http import HttpResponse

# def blog(request):
#     print("blog")
#     return HttpResponse("blog do app")


# def exemplo(request):
#     print("exemplo")
#     return HttpResponse("exemplo do app 1")

from django.shortcuts import render
from blog.data import posts


def blog(request):
    print("blog")
    context = {"text": "Estou na blog home", "posts": posts}
    return render(request, "blog/index.html", context)


def post(request, id):
    print("post", id)
    context = {"text": "Olá posts", "posts": posts}
    return render(request, "blog/index.html", context)


def exemplo(request):
    print("exemplo")
    context = {"text": "Estou no exemplo", "title": "nome da página Exemplo - "}
    return render(request, "blog/example.html", context)
