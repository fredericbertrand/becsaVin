from django.shortcuts import render, get_object_or_404
from .models import Image_caroussel


# from django.http import HttpResponse

# Create your views here.


# def index(request):
#   return HttpResponse("Hello! c'est la page d'index de cette main_app.")


def index(request):
    return render(request, "main_app/index.html")


def carousel(request, id):
    photos_carousel = get_object_or_404(Image_caroussel, id=id)
    data = {"photos_list": photos_carousel}
    return render(request, "main_app/carousel.html", data)


def plan(request):
    return render(request, "main_app/plan.html")


def caviste(request):
    return render(request, "main_app/caviste.html")


def commentaires(request):
    return render(request, "main_app/commentaires.html")


def bistrot(request):
    return render(request, "main_app/bistrot.html")


def baravin(request):
    return render(request, "main_app/baravin.html")


def partenaires(request):
    return render(request, "main_app/partenaires.html")


def propos(request):
    return render(request, "main_app/propos.html")


def photo(request, id):
    pict = get_object_or_404(Image_caroussel, id=id)
    pict_data = {"picture": pict.picture, "title": pict.title}
    return render(request, "main_app/photo.html", pict_data)