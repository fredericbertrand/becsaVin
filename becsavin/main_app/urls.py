from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

app_name = "main_app"

urlpatterns = [
    path("", views.index, name="index"),
    path("plan/", views.plan, name="plan"),
    path("caviste/", views.caviste, name="caviste"),
    path("baravin/", views.baravin, name="baravin"),
    path("bistrot/", views.bistrot, name="bistrot"),
    path("partenaires/", views.partenaires, name="partenaires"),
    path("commentaires/", views.commentaires, name="commentaires"),
    path("propos/", views.propos, name="propos"),
    path("suggestions/", views.suggestions, name="suggestions"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
