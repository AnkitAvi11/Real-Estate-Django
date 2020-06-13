from django.contrib import admin
from .models import Realtor

#   Realtor admin Display settings
class RealtorAdminDisplay(admin.ModelAdmin) : 
    list_display = ('id', 'realtor_name', 'phone', 'email', 'is_mvp',)
    list_display_links = ('id', 'realtor_name',)
    list_editable = ('is_mvp',)

admin.site.register(Realtor, RealtorAdminDisplay)

