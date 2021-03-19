from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    dict={'ins':'hello views.py se a rha hu me'}
    return render(request,'app1/index.html',dict)

def help(request):
    return render(request,'app1/help_page.html')

def about(request):
    return render(request,'about.html')