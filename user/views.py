import json

from django.views import View
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from .models import User
from django.contrib import auth
from django.contrib.auth.hashers import check_password

from user.decorators import *
from django.utils.decorators import method_decorator


class RegisterView(View):
    def post(self, request):
        try:
            data = request.POST
            
            user = User.objects.create_user(
                        user_id=data.get('user_id', None),
                        password=data.get('user_pw', None),
                        email=data.get('email', None)
                    )
            
            auth.login(request, user)
            return JsonResponse({'msg': "success"}, status=200)
            
        except KeyError:
            return JsonResponse({'msg': "INVALID_KEYS"}, status=400)
    
    
    def get(self, request):
        
        return render(request, 'user/register.html', {})
        


def doubleCheck(request):
        try:
            data = request.POST
            
            if User.objects.filter(user_id=data.get('user_id', None)).exists():
                return JsonResponse({'msg': "fail"}, status=200)
          
            else:
                return JsonResponse({'msg': "success"}, status=200)
            
        except KeyError:
            return JsonResponse({'msg': "INVALID_KEYS"}, status=400)
    
    
class LoginView(View):
    
    def post(self, request):
        try:
            data = request.POST            
            user = auth.authenticate(request, user_id=data.get('user_id', None), password=data.get('user_pw', None))
            
            if user is not None:
                auth.login(request, user)
                return JsonResponse({'msg': "success"}, status=200)
            else:
                return JsonResponse({'msg': "fail"}, status=200)

        except KeyError:
            return JsonResponse({'msg': "INVALID_KEYS"}, status=400)
    def get(self, request):

        return render(request, 'user/login.html', {})


class LogoutView(View):
    
    def get(self, request):
        auth.logout(request)
        return redirect("/")
    
    
@method_decorator(login_message_required, name='dispatch')
class PasswordChangeView(View):
    
    def post(self, request):
        
        user = request.user
        current_password = request.POST.get("pw_origin", None)
        print(current_password)
        print(user.password)
        print(check_password(current_password,user.password))
        if check_password(current_password,user.password):
            if request.POST.get("pw_new") == request.POST.get("pw_new_re"):
                new_password = request.POST.get("pw_new")
                user.set_password(new_password)
                user.save()
                auth.login(request,user)
                
                return JsonResponse({'msg': "success"}, status=200)
            return JsonResponse({'msg': "pw-error"}, status=200)
        else:
            return JsonResponse({'msg': "pw-error"}, status=200)
        
        
    def get(self, request):
        

        return render(request, 'user/password-change.html')


    
@method_decorator(login_message_required, name='dispatch')
class UserDeleteView(View):
    
    def post(self, request):
        
        user = request.user
        current_password = request.POST.get("pw", None)
        
        if(check_password(current_password, user.password)):
            user.delete()
            auth.logout(request)
            print("--------------------회원탈퇴===============")
            return JsonResponse({'msg': "success"}, status=200)
        
        else:
            return JsonResponse({'msg': "pw-error"}, status=200)
        
    def get(self, request):
        
        return render(request, 'user/delete.html')