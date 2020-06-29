from django.db import models

# Create your models here.
class team(models.Model):
    name = models.CharField(max_length=20)
    designation=models.CharField(max_length=50)
    image=models.ImageField(upload_to='photos/%Y/%m/%d')
    facebook = models.URLField(max_length=500, blank=True)
    instagram= models.URLField(max_length=500, blank=True)
    twitter = models.URLField(max_length=500, blank=True)
    linkedin = models.URLField(max_length=500, blank=True)
    is_published = models.BooleanField(default=True)
    def __str__(self):
        return self.name

class Carousel(models.Model):
    image_name= models.CharField(max_length=30)
    image=models.ImageField(upload_to='photos/%Y/%m/%d')
    desc=models.TextField(max_length=500, blank=True)
    is_published=models.BooleanField(default=True)
    def __str__(self):
        return self.image_name
