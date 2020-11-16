from django.shortcuts import render
from pics.models import *

# Create your views here.
def index(request):
    Images = Image.objects.all()
    return render (request, 'base.html',{'Image':resultsdisplay })