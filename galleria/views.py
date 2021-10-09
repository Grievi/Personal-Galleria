from django.shortcuts import render
from .models import Img, Location

def pics(request):
    images = Img.objects.all()
    locations = Location.get_locations()
    print(locations)
    return render (request, 'gallery/pics.html' , {'images': images[::-1], 'locations': locations})
    
def image_location(request, location):
    images =Img.filter_by_location(location)
    print(images)
    return render(request, 'gallery/location.html', {'images_location': images})