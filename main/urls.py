from django.urls import path
from .views import *

app_name = 'main'
urlpatterns = [
    path('', showmain, name = 'showmain'),
    path('big/', big, name = 'big'),
    path('public', public, name = 'public'),
    path('qna/', qna, name = 'qna'),
    path('qna_new/', qna_new, name="qna_new"),
    path('qna_detail', qna_detail, name="qna_detail"),
    path('qna_create/', qna_create, name="qna_create"),
    path('qna_delete/', qna_delete, name="qna_delete"),
    path('LG/', showLG, name = 'showLG'),
    path('LGES/', showLGES, name = 'showLGES'),
    path('SAMSUNG/', showSamsung, name = 'showSamsung'),
    path('SAMSUNGELEC/', showSamsungElec, name = "showSamsungElec"),
    path('IBK/', showIBK, name = "showIBK"),
]