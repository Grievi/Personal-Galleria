from django.db import models

# Create your models here.
class Img(models.Model):
    img = models.ImageField(upload_to ='static/')
    name = models.CharField(max_length=60)
    description = models.TextField()
    author = models.CharField(max_length=40, default='admin')
    date = models.DateTimeField(auto_now_add=True)
    # category = models.ForeignKey(Category)
    # location = models.ForeignKey(Location)

class Category(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

class Location(models.Model):
    name = models.CharField(max_length=60)

    @classmethod
    def get_locations(cls):
        locations = Location.objects.all()
        return locations

    def __str__(self):
        return self.name

    @classmethod
    def save_location(self):
        self.save()

    def update_location(cls, id, value):
        cls.objects.filter(id=id).update(image=value)

    def delete_locations(self):
        self.delete()



















