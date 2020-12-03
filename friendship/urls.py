from django.urls import path
from . import views

app_name = 'friendship'

urlpatterns = [
    path('friendship/',  views.FriendshipView.as_view(), name='friendship'),
    path('friend-add/', views.friend_add, name="friend-add"),
    path('friend-cancel/', views.friend_cancel, name="friend-cancel"),
    path('friend-accept/', views.friend_accept, name="friend-accept"),
    path('friend-reject/', views.friend_reject, name="friend-reject"),
    path('friend-remove/', views.friend_remove, name="friend-remove"),
]