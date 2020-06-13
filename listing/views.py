from django.http import Http404, HttpResponse, JsonResponse
from django.shortcuts import render, redirect

def indexView(request) : 
    return HttpResponse("All Listing page")