from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.indexPage, name='home'),
    re_path(r'^about/$', views.aboutPage, name='about'),
]
