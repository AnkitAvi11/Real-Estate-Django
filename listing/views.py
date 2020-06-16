from django.http import Http404, HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from datetime import datetime
from django.core.paginator import Paginator

from listing.models import Listing 

def indexView(request) : 
    listings = Listing.objects.all().order_by('-pub_date')

    #   implementing the paginator
    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        "listings" : paged_listings
    }
    #   returning render 

    return render(request, 'listings/listings.html', context)    

def listing(request, listing_id) : 
    listing = Listing.objects.get(id=listing_id)
    context = {
        "title" : listing,
        "listing" : listing
    }
    return render(request, 'listings/listing.html', context)

