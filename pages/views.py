from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

def indexPage(request) : 
    return render(request, 'pages/index.html')

def aboutPage(request) :
    return render(request, 'pages/about.html')


