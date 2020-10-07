from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

app_name = "main_app"

urlpatterns = [
    path("", views.index, name="index"),
    path("caviste/", views.caviste, name="caviste"),
    path("commentaires/", views.commentaires, name="commentaires"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
