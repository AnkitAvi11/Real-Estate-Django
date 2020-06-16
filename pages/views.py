from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from realtor.models import Realtor
from listing.models import Listing

def indexPage(request) : 
    listings = Listing.objects.all().order_by('-pub_date')[:3]
    context = {
        "listings" : listings
    }
    return render(request, 'pages/index.html', context)

def aboutPage(request) :
    mvp = Realtor.objects.filter(is_mvp=True)[0]
    context = {
        "realtor" : mvp
    }
    return render(request, 'pages/about.html', context)


