from django.shortcuts import render, redirect
from django.views.decorators.http import require_GET, require_POST
from django.shortcuts import get_object_or_404
from django.views import View
from django.views.generic import ListView
from django.core.paginator import Paginator
from django.http import JsonResponse, HttpResponse
from django.http import Http404
from .models import Post, Comment
from user.decorators import *
from user.models import User
from django.core import serializers
import json


def is_ajax(request):
    """
    This utility function is used, as `request.is_ajax()` is deprecated.
    This implements the previous functionality. Note that you need to
    attach this header manually if using fetch.
    """
    return request.META.get("HTTP_X_REQUESTED_WITH") == "XMLHttpRequest"




##SCROLL
@require_GET
def post_list_scroll(request):
    """
    List view for posts. 
    """
    all_posts = Post.objects.order_by('-pk').all()
    paginator = Paginator(all_posts, per_page=10)
    page_num = int(request.GET.get("page", 1))
    if page_num > paginator.num_pages:
        raise Http404
    posts = paginator.page(page_num)
    if is_ajax(request):
        return render(request, 'post/scroll/_posts.html', {'posts': posts})
    return render(request, 'post/scroll/post_list.html', {'posts': posts})


@login_message_required
@require_POST
def create_post_scroll(request):
    text = request.POST.get("text")
    if text:
        post = Post.objects.create(writer=User.objects.get(user_id=request.user.user_id),title=text,content=text)
    return redirect('/post/scroll')







## BOARD
class BoardView(ListView):
    model = Post
    paginate_by = 10
    template_name = 'post/board/post_list.html'
    context_object_name = 'post_list'
    
    def get_queryset(self):
        post_list = Post.objects.order_by('-id')
        return post_list
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = context['paginator']
        page_numbers_range = 5
        max_index = len(paginator.page_range)

        page = self.request.GET.get('page')
        current_page = int(page) if page else 1

        start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range
        end_index = start_index + page_numbers_range
        if end_index >= max_index:
            end_index = max_index

        page_range = paginator.page_range[start_index:end_index]
        context['page_range'] = page_range

        return context

class Board_Detail_View(View):
    def get(self, request,pk):
        post = get_object_or_404(Post, pk=pk)
        comment = Comment.objects.filter(post=pk).order_by('-pub_date')
        context = {
            'post' : post,
            'comments' : comment,
        }
        
        return render(request, 'post/board/post_detail.html', context)
    
    

## COMMENT

class Comment_View(View):
    
    def post(self, request, pk):
        post = get_object_or_404(Post, id = pk)
        content = request.POST.get('content')

        if content:
            comment = Comment.objects.create(post=post,writer=request.user,content=content)
            test = request.user.user_id
            data= {
                'writer' : request.user.user_id,
                'content' : content,
                'pub_date' : '방금 전',
                'comment_id' : comment.id
            }
            return JsonResponse({'msg': "success",'data' : data}, status=200)
