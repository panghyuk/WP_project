from django.shortcuts import render, get_object_or_404, redirect
from main.models import *
from .models import User

def mypage(request):
    user = request.user
    posts = Post.objects.filter(writer = user)
    return render(request,'users/mypage.html',{'posts':posts})
    