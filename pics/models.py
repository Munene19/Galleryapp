from django.db import models
from django.db.models import Model
from cloudinary.models import CloudinaryField

# Create your models here.

class Location(models.Model):
    Image_location = models.CharField(max_length=100)

    def __str__(self):
        return self.Image_location


class Category(models.Model):
    Image_category = models.CharField(max_length=100)

    def save_category(self):
        self.save()

    def __str__(self):
        return self.Image_category


class Image(models.Model):
    Image_name = models.CharField(max_length=100)
    Image_description = models.CharField(max_length=100)
    location = models.ForeignKey(Location, null=True, on_delete=models.SET_NULL)
    Category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    Image = CloudinaryField('image')  


    def __str__(self):
        return self.Image_name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def all_images(cls):
        images = cls.objects.all()
        return images

    @classmethod
    def search_by_category(cls,search_term):
        images = cls.objects.filter(categories__name__contains = search_term)
        if len(images) < 1:
            case_images = cls.objects.filter(categories__name__contains = search_term.capitalize())
            return case_images
        else:
            return images

    @classmethod
    def filter_by_location(cls,search_term):
        location = Location.objects.get(name = search_term)
        images = cls.objects.filter(location = location)
        return images





