from django.views import View
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse

from .models import *
from user.models import User

from user.decorators import *
from django.utils.decorators import method_decorator

# Create your views here.

@method_decorator(login_message_required, name='dispatch')
class FriendshipView(View):
    
    def get(self, request):
        data = {
            "friendship_request_from" : FriendshipRequest.objects.filter(to_user=request.user).only("to_user"),
            "friendship_request_to" : FriendshipRequest.objects.filter(from_user=request.user),
            "users" : User.objects.only("user_id"),
            "friend_list": Friendship.objects.filter(to_user=request.user)
        }
        tmp = User.objects.only("user_id")
        print(FriendshipRequest.objects.filter(to_user=request.user).only("to_user"))
        print(FriendshipRequest.objects.filter(to_user=request.user).only("from_user"))
        return render(request, 'friendship/index.html', {"data" : data})
    
    
@login_message_required
def friend_add(request):
    if request.method == "POST":
        from_user = request.user
        to_user = User.objects.get(user_id=request.POST.get('to_user', None))
        
        print(to_user)
        
        if from_user == to_user:
            return JsonResponse({'msg': "fail_same_user"}, status=200)
        
        if FriendshipRequest.objects.filter(from_user=from_user, to_user=to_user).exists():
            return JsonResponse({'msg': "fail_already_request"}, status=200)
        
        if Friendship.objects.filter(from_user=from_user, to_user=to_user).exists():
            return JsonResponse({'msg': "fail_already_friend"}, status=200)
        
        FriendshipRequest.objects.friend_add(from_user, to_user)
        return JsonResponse({'msg': "success"}, status=200)
    
    
@login_message_required 
def friend_cancel(request):
    if request.method == "POST":
        from_user = request.user
        to_user = User.objects.get(user_id=request.POST.get('to_user', None))

        print(to_user)
        FriendshipRequest.objects.friend_cancel(from_user, to_user)
        return JsonResponse({'msg': "success"}, status=200)
    
    
@login_message_required
def friend_accept(request):
    if request.method == "POST":
        from_user = User.objects.get(user_id=request.POST.get('from_user', None))
        to_user = request.user

        print(from_user)
        FriendshipRequest.objects.friend_accept(from_user, to_user)
        return JsonResponse({'msg': "success"}, status=200)
    
@login_message_required
def friend_reject(request):
    if request.method == "POST":
        from_user = User.objects.get(user_id=request.POST.get('from_user', None))
        to_user = request.user

        print(from_user)
        FriendshipRequest.objects.friend_reject(from_user, to_user)
        return JsonResponse({'msg': "success"}, status=200)
    
@login_message_required
def friend_remove(request):
    if request.method == "POST":
        from_user = User.objects.get(user_id=request.POST.get('from_user', None))
        to_user = request.user

        print(from_user)
        Friendship.objects.friend_remove(from_user, to_user)
        return JsonResponse({'msg': "success"}, status=200)