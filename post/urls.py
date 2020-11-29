from django.urls import path
from . import views
from post import views as posts_views
from django.views.generic import RedirectView
app_name = 'post'

urlpatterns = [
    path('post/scroll', posts_views.post_list_scroll, name='post-list-scroll'),
    path('post/scroll/create/', posts_views.create_post_scroll, name='create-post-scroll'),
    path('post/board', views.BoardView.as_view(), name='post-list-board'),
    path('post/board/<int:pk>', views.Board_Detail_View.as_view(), name='post-list-board-detail'),
    path('post/board/<int:pk>/comment/write', views.Comment_View.as_view(), name='board-comment-write'),
] 

 