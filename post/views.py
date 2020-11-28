from django.shortcuts import render, redirect
from django.views.decorators.http import require_GET, require_POST
from django.core.paginator import Paginator
from django.http import Http404
from .models import Post
from user.decorators import *
from user.models import User


def is_ajax(request):
    """
    This utility function is used, as `request.is_ajax()` is deprecated.
    This implements the previous functionality. Note that you need to
    attach this header manually if using fetch.
    """
    return request.META.get("HTTP_X_REQUESTED_WITH") == "XMLHttpRequest"



@require_GET
def post_list(request):
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
        return render(request, 'post/_posts.html', {'posts': posts})
    return render(request, 'post/post_list.html', {'posts': posts})


@login_message_required
@require_POST
def create_post(request):
    text = request.POST.get("text")
    if text:
        post = Post.objects.create(writer=User.objects.get(user_id=request.user.user_id),title=text,content=text)
    return redirect('/post')