from django.db import models

# Create your models here.
class Img(models.Model):
    img = models.ImageField(upload_to ='static/')
    name = models.CharField(max_length=60)
    description = models.TextField()
    author = models.CharField(max_length=40, default='admin')
    date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category)
    location = models.ForeignKey(Location)

class Category(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()