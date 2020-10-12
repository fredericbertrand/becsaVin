from django.contrib import admin

# Register your models here.
from .models import Producteurs, Image_caroussel, Vins

admin.site.register(Producteurs)
admin.site.register(Image_caroussel)
admin.site.register(Vins)