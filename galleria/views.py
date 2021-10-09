from django.shortcuts import render
from .models import Img, Location

def pics(request):
    images = Img.objects.all()
    locations = Location.get_locations()
    print(locations)
    return render (request, 'gallery/pics.html' , {'images': images[::-1], 'locations': locations})
    