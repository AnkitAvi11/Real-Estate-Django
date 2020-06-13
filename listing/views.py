from django.http import Http404, HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from datetime import datetime

from listing.models import Listing 

def indexView(request) : 
    listings = Listing.objects.all().order_by('-pub_date')
    context = {
        "listings" : listings
    }
    return render(
        request, 
        "listings/listings.html",
        context
    )

def listing(request, listing_id) : 
    return HttpResponse(listing_id)
