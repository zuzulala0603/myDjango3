from django.views import View
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse

from .models import Contact


class ContactView(View):
    
    def post(self, request):
        try:
            data = request.POST
            
            contact = Contact(
                email=data.get('email', None),
                content=data.get('content', None),
            )
            
            contact.save()
            return JsonResponse({'msg': "success"}, status=200)
            
        except KeyError:
            return JsonResponse({'msg': "INVALID_KEYS"}, status=400)

    def get(self, request):
        return render(request, 'contact/index.html', {})