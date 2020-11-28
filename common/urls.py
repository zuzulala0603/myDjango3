
from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('header', views.HeaderView.as_view(), name="header"),
]
