from django.urls import path 


from . import views

urlpatterns =[
    path('home/',views.index, name = 'home'),
    path('location/',views.location,name = 'location'),
    path('search/',views.search,name='search')
]

