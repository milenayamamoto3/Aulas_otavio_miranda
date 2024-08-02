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
from django.http import HttpRequest, Http404
from typing import Any


def blog(request):
    print("blog")
    context = {"text": "Estou na blog home", "posts": posts}
    return render(request, "blog/index.html", context)


def post(request: HttpRequest, post_id: int):
    found_post: dict[str, Any] | None = None

    for post in posts:
        if post["id"] == post_id:
            found_post = post
            break

    if found_post is None:
        raise Http404("Post não existe.")

    print("post", post_id)

    context = {
        "text": "Olá posts",
        "post": found_post,
        "title": found_post["title"] + " - ",
    }
    return render(request, "blog/post.html", context)


def exemplo(request):
    print("exemplo")
    context = {"text": "Estou no exemplo", "title": "nome da página Exemplo - "}
    return render(request, "blog/example.html", context)
