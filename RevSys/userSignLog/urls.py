from django.urls import path
from . import views

urlpatterns = [
    path("", views.SignUp, name="SignUp"),
    path("login/", views.LogIn, name="LogIn"),
]