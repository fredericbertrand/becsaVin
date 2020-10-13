from django.db import models

# Create your models here.
class Image_caroussel(models.Model):
    name = models.CharField(max_length=200)
    picture = models.ImageField()

    def __str__(self):
        return self.name


class Producteurs(models.Model):
    name = models.CharField(max_length=200)
    link = models.URLField()
    picture = models.ImageField()


class Vins(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    region = models.CharField(max_length=200)
    picture = models.ImageField()
    price = models.FloatField()
    date = models.DateField()