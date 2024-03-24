from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('about', views.about, name="about"),
    path('taro', views.taro, name="taro_cards_reading")
]