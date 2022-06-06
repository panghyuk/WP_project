from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import HttpResponse
import json

# Create your views here.
def showmain(request):
    return render(request,'main/mainpage.html')

def big(request):
    return render(request, 'main/big.html')

def public(request):
    return render(request, 'main/public.html')

def qna(request):
    posts = Post.objects.all()
    return render(request, 'main/qna.html', {'posts': posts})

def qna_new(request):
    return render(request, 'main/qna_new.html')

def qna_create(request):
    new_qna = Post()
    new_qna.title = request.POST['title']
    new_qna.writer = request.user
    new_qna.pub_date = timezone.now() 
    new_qna.body = request.POST['body']
    new_qna.image = request.FILES.get('image')
    new_qna.save()
    return redirect('main:qna_detail', new_qna.id)

def qna_edit(request, id):
    qna_edit = Post.objects.get(id = id)
    return render(request, 'main/post_edit.html', {'post': qna_edit})

def qna_update(request, id):
    qna_update = Post.objects.get(id = id)
    qna_update.title = request.POST['title']
    qna_update.writer = request.user
    qna_update.pub_date = timezone.now() 
    qna_update.body = request.POST['body']
    qna_update.image = request.FILES.get('image')
    qna_update.save()
    return redirect('main:qna_detail', qna_update.id)

def qna_detail(request, id):
    qna = get_object_or_404(Post, pk = id)
    return render(request, 'main/board_detail.html', {'post': qna})

def qna_delete(request, id):
    board_delete = Post.objects.get(id = id)
    board_delete.delete()
    return redirect ('main:qna')

def showLG(request):
    return render(request, 'main/LG.html')

def showLGES(request):
    return render(request, 'main/LGES.html')

def showSamsung(request):
    return render(request,'main/samsung.html')

def showSamsungElec(request):
    return render(request,'main/samsungelec.html')

def showIBK(request):
    return render(request,'main/IBK.html')