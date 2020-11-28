import json

from django.views import View
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.mixins import PermissionRequiredMixin

from django.contrib.auth.decorators import login_required
# Create your views here.

class IndexView(View):

    def get(self, request): 
        return render(request, 'common/index.html')

class HeaderView(View):

    def get(self, request): 
        return render(request, 'common/header.html')

