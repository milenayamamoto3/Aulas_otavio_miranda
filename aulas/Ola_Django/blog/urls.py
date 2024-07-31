from blog import views
from django.urls import path

# namespace
app_name = "blog"


# Django URLs:
# https://docs.djangoproject.com/en/4.2/topics/http/urls/

# blog/
urlpatterns = [
    path("", views.blog, name="home"),
    path("<int:id>/", views.post, name="post"),
    path("exemplo/", views.exemplo, name="exemplo"),
]
