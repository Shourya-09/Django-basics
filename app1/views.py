from django.shortcuts import render
from app1.forms import *

from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    return render(request,'index.html')

def base(request):
    return render(request,'app1/base.html')

def register(request):
    registered=False

    if request.method=='POST':
        user_form=UserForm(data=request.POST)
        profile_form=UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user=user_form.save()
            user.set_password(user.password)
            user.save()

            profile=profile_form.save(commit=False)
            profile.user=user

            profile_form.save() 
            registered=True
            if 'profile_pic' in request.FILES:
                profile.profile_pic=request.FILES['profile_pic']
        else:
            print(user_form.errors,profile_form.errors)
    
    else:
        user_form=UserForm()
        profile_form=UserProfileForm()
    return render(request,'app1/register.html',{'user_form':user_form,'profile_form':profile_form,'registered':registered})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def user_login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('Account not active')
        else:
            print('Someone tried to login ')
            print("username {} and password {}".format(username,password))
            return HttpResponse('invalid creds')
    else:
        return render(request,'app1/login.html',{})


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
