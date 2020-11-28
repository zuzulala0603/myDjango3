import json

from django.views import View
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse


from .models import User
from django.contrib import auth



class RegisterView(View):
    def post(self, request):
        try:
            data = request.POST
            
            user = User.objects.create_user(
                        user_id=data.get('user_id', None),
                        password=data.get('user_pw', None),
                        email='test'
                    )
            
            auth.login(request, user)
            return JsonResponse({'msg': "success"}, status=200)
            
        except KeyError:
            return JsonResponse({'msg': "INVALID_KEYS"}, status=400)
    
    
    def get(self, request):
        
        return render(request, 'user/register.html', {})
        


class RegisterFormView(View):

    def post(self, request):
        try:
            data = request.POST
            
            user = User.objects.create_user(
                        user_id=data.get('user_id', None),
                        password=data.get('user_pw', None),
                    )
            
            auth.login(request, user)
            return JsonResponse({'msg': "success"}, status=200)
            
        except KeyError:
            return JsonResponse({'msg': "INVALID_KEYS"}, status=400)


    def get(self, request):

        return render(request, 'user/register-form.html', {})


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