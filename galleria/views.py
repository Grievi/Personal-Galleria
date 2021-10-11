from django.shortcuts import render
from .models import Img, Location

def pics(request):
    images = Img.objects.all()
    locations = Location.get_locations()
    
    return render (request, 'gallery/pics.html' , {'images': images[::-1], 'locations': locations})
    
def image_location(request, location):
    images =Img.filter_by_location(location)
    
    return render(request, 'gallery/location.html', {'images': images})

def search_results(request):
    
    if 'imagesearch' in request.GET and request.GET["imagesearch"]:
        category = request.GET.get("imagesearch")
        searched_images = Img.search_by_category(category)
        message = f"{category}"
        
        return render(request, 'gallery/search_res.html', {"message": message, "images": searched_images})
    else:
        message = "Enter a category to search images from"
        return render (request, 'gallery/search_res.html', {"message": message})