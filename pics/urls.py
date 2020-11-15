from django.contrib import admin 
from django.urls import path 
from django.conf import settings 
from django.conf.urls.static import static
from . import views

urlpatterns =[
    path('home/',views.index, name = 'home')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)