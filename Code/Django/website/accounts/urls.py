from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('logout', views.logout1, name='logout'),
    path('login', views.login1, name='login'),
]