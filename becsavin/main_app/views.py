from django.shortcuts import render, get_object_or_404
from .models import Image_caroussel


# from django.http import HttpResponse

# Create your views here.


# def index(request):
#   return HttpResponse("Hello! c'est la page d'index de cette main_app.")


def carousel():
    list_photos_carousel = Image_caroussel.objects.all()
    context = {"list_pictures": list_photos_carousel}
    return context


def index(request):
    context = carousel()
    return render(request, "main_app/index.html", context)


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

def suggestions(request):
    return render(request, "main_app/suggestions.html")

