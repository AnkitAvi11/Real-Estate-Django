from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.indexView, name='listings'),
    path('view/<int:listing_id>/', views.listing, name="listing"),
]