from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import auth_login, LoginView
from . import views

app_name = 'users'

urlpatterns = [
    # path('login/', LoginView.as_view(template_name='login.html'), name="login"),
]
