from django.shortcuts import render_to_response
from models import *
from django.template import Context
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required

def home(request):

    query = request.GET.get('input',' ')
    if query == ' ':
    	template = "index.html"
    	aux= ''
    	num2= 0
    elif query == '':
        template = "index.html" 
        num2= 0
    else:
    	receta = Receta.objects.filter(nombre__icontains=query)
    	num = receta.count()
    	num2= receta.count()+1	
    	template = "index.html"
    	aux= query
    return  render_to_response(template,locals())

def acerca(request): 	
    template = "acerca.html"
    return  render_to_response(template,locals())