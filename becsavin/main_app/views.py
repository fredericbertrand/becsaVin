from django.shortcuts import render

# from django.http import HttpResponse

# Create your views here.


# def index(request):
#   return HttpResponse("Hello! c'est la page d'index de cette main_app.")


def index(request):
    return render(request, "main_app/index.html")


def carousel(request):
    return render(request, "main_app/carousel.html")
