from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from . import views
from django.contrib.auth import login, logout
from django.http import HttpResponse


class QrcodeMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
    
    def __call__(self,request):
        response=self.get_response(request)
        return response
    
    def process_view(self,request,view_func,view_args,view_kwargs):
        if '/admin' in request.path:
            return None
        if request.user.is_superuser:
            return None
        
        if request.user.is_authenticated():
            if 'logout' not in request.path:
                if not request.user.username=='audiforce' and 'qrcode' in request.path:
                    logout(request)
                    return HttpResponse("invalid user")
                else:
                    return None
        else:
            return None        
