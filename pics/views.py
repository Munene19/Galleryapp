import os
from django.conf import settings
from django.shortcuts import render
from django.templatetags.static import static
from .models import Image, Category, Location


# Create your views here.
def gallery(request):
    images = Image.objects.all()
    locations = Location.objects.all()
    ctx = {"images":images,"locations":locations}
    return render(request, 'index.html', ctx)

def location(request,location):
    locations = Location.objects.all()
    selected_location = Location.objects.get(id = location)
    images = Image.objects.filter(location = selected_location.id)
    ctx_2 = {"location":selected_location,"locations":locations,"images":images}
    return render(request, 'location.html', ctx_2)

def search(request):
    if 'imagesearch' in request.GET and request.GET["imagesearch"]:
        search_term = request.GET.get("category")
        category = request.GET.get("imagesearch")
        searched_images = Image.search_by_category(category)
        message = f"{category}"
        ctx_3 = {"images":searched_images,"category":search_term}
        print(searched_images)
        return render(request,'search.html', ctx_3)
    else:
        message = "Try entering a valid category"
        return render(request, 'search.html', {"message": message})