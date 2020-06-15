from django.http import Http404, HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from datetime import datetime
from django.core.paginator import Paginator

from listing.models import Listing 

def indexView(request) : 
    listings = Listing.objects.all().order_by('-pub_date')

    #   implementing the paginator
    paginator = Paginator(listings, 2)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        "listings" : paged_listings
    }
    #   returning render 

    return render(request, 'listings/listings.html', context)    

def listing(request, listing_id) : 
    return HttpResponse(listing_id)

