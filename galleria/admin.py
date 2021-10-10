from django.contrib import admin
from . models import Img, Location, Category
# Register your models here.
admin.site.register(Img)
admin.site.register(Location)
admin.site.register(Category)