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
    return render(request, 'main/qna.html')

def qna_new(request):
    return render(request, 'main/qna_new.html')

def qna_create(request):
    return render(request, 'main/qna_detail.html')

def qna_detail(request):
    return render(request, 'main/qna_detail.html')

def qna_delete(request):
    return render(request, 'main/qna.html')

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