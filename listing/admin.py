from django.contrib import admin

# Register your models here.
from listing.models import Listing

class ListingAdmin(admin.ModelAdmin) : 
    list_display = ('id', 'title', 'realtor', 'state', 'city', 'pub_date', 'zipcode')
    list_display_links = ('id', 'title')
    list_filter = ('state', 'realtor')
    search_fields = ('title', 'state')

admin.site.register(Listing, ListingAdmin)