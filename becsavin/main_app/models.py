from django.db import models

# Create your models here.
class Image_caroussel(models.Model):
    title = models.CharField(max_length=200)
    picture = models.ImageField(upload_to="slider/")

    def __str__(self):
        return self.title


class Producteurs(models.Model):
    name = models.CharField(max_length=200)
    link = models.URLField()
    picture = models.ImageField(upload_to="partenaires/")

    def __str__(self):
        return self.name


class Vins(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    region = models.CharField(max_length=200)
    picture = models.ImageField()
    price = models.FloatField()
    date = models.DateField()