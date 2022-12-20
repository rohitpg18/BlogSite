from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
import random
from .mixins import MessageHandler
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.views.generic import View
from Blogs.models import *
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


# Create your views here.
def login_view(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        if not Profile.objects.filter(phone_number=phone_number).exists():
            return redirect ('register/')
        else:
            profile = Profile.objects.get(phone_number=phone_number)
        
        profile.otp = random.randint (1000 , 9999)
        profile.save()

        message_handler = MessageHandler(phone_number , profile.otp).send_otp_on_phone()

        return redirect(f'/otp/{profile.uid}')

    return render (request , 'login.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        phone_number = request.POST.get('phone_number')
        user = User.objects.create(username = username)
        profile = Profile.objects.create(user=user, phone_number=phone_number)

        return redirect ("login")

    return render (request, 'signup.html')

def dashboard_view(request):
    return redirect("blog_list")

def otp (request , uid):
    if request.method == 'POST':
        otp = request.POST.get('otp')
        profile = Profile.objects.get(uid = uid)
        if otp==profile.otp:
            login(request, profile.user)
            messages.success(request, "Logged In Successfully")
            return redirect ("blog_list")

        return redirect(f'/otp/{uid}')
    return render (request, 'otp.html')

def logoutUser(request):
    logout(request)
    messages.info(request, "Logged out of BlogSite")
    return redirect('login')

class ProfileView(View):
    @method_decorator(login_required(login_url=''))

    def get(self, request):
        pk= request.user.id

            
        blogs = Blog.objects.filter(author_id=pk)
            
        context= {
            "blogs":blogs,
        }
        
        return render(request, "profile.html",context)


