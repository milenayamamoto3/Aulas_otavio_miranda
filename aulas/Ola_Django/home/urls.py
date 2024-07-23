from django.urls import path

from . import views

# namespace
app_name = "home"

urlpatterns = [
    path("", views.home, name="home"),
]
