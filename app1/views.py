from django.shortcuts import render
from django.http import HttpResponse
from . import forms
# Create your views here.

def index(request):
    dict={'ins':'hello views.py se a rha hu me'}
    return render(request,'app1/index.html',dict)

def help(request):
    return render(request, 'help_page.html')

def about(request):
    return render(request,'about.html')

def other(request):
    return render(request,'app1/other.html')

def relative(request):
    return render(request,'app1/relative.html')


def forms_page(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            print('validation success')
            print("NAME: "+form.cleaned_data['name'])
            print("EMAIL: "+form.cleaned_data['email'])

            print("EMAIL1: "+form.cleaned_data['email1'])
            print("TEXT: "+form.cleaned_data['text'])
    return render(request, 'f_page.html', {'form': form})
