from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index1(request):
    my_dict = {'insert_me':"hellom im from views.py"}
    return render(request,'index.html',context=my_dict)