from django.urls import path
from authuser import views

urlpatterns = [
    path("login/",views.login_user, name="login"),
    path("register/",views.register_user, name="register"),
]