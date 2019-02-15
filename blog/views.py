# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse
# Create your views here.

def home (request):
    nama ="Dika Pratama"
    buah =['kalapa', 'jambu', 'kadongdong', 'salak']
    makanan =['batagor','cimol','cireng']
    return render(request, 'index.html', {'nama':nama, 'buah':buah, 'makanan':makanan})

def about (request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def blog(request):
    return render(request, 'blog.html')

