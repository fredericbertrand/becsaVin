# from . import views
# from django.urls import path
# from django.conf import settings
# from django.conf.urls.static import static
# from django.conf.urls import url

# app_name = "account"

# urlpatterns = [
#     # path("", views.index, name="index"),
#     path("", views.my_account, name="my_account"),
#     # path("base_account/", views.base_account, name="base_account"),
#     path("signin/", views.signin, name="signin"),
#     path("signup/", views.signup, name="signup"),
#     path("toto/", views.toto, name="toto"),
# ]

"""Contains the applicationâ€™s url."""
from django.urls import path
from . import views

app_name = "account"
urlpatterns = [
    path("my_account", views.my_account, name="my_account"),
    path(
        "inscription_producteur",
        views.inscription_producteur,
        name="inscription_producteur",
    ),
    path("connexion", views.connexion, name="connexion"),
    path("deconnexion", views.deconnexion, name="deconnexion"),
]
