from django.db import models
from django.db.models import Model

# Create your models here.

class Location(models.Model):
    Image_location = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.Image_location


class Category(models.Model):
    Image_category = models.CharField(max_length=30, null=True)

    def save_category(self):
        self.save()

    def __str__(self):
        return self.Image_category


class Image(models.Model):
    Image = models.ImageField(upload_to='static/media/' , height_field=None, width_field=None, max_length=100, null=True)  
    Image_name = models.CharField(max_length=30)
    Image_description = models.CharField(max_length=100)
    location = models.ForeignKey(Location, null=True, on_delete=models.SET_NULL)
    Category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.Image_name




