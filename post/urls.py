from django.urls import path
from . import views
from post import views as posts_views
from django.views.generic import RedirectView
app_name = 'post'

urlpatterns = [
    path('post/', posts_views.post_list, name='post-list'),
    path('post/create/', posts_views.create_post, name='create-post'),
    path('', RedirectView.as_view(url='post/')),
] 