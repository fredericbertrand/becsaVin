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
    path("commentaires/", views.commentaires, name="commentaires"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
