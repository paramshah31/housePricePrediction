from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('predict_price', views.predict_house_price, name='predict_price'),
]