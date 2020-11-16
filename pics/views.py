import os
from django.conf import settings
from django.shortcuts import render
from django.templatetags.static import static

# Create your views here.
def index(request):
    images = Image.all_images()
    locations = Location.objects.all()
    return render(request, 'index.html', {"images":images,"locations":locations})