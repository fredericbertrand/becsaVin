from django.db import models

from django.contrib.auth.models import AbstractUser


class My_user(AbstractUser):
    """Contain user information."""

    administrateur = models.BooleanField(default=False)
    # username = models.CharField(max_length=255, unique=True, verbose_name=("Username"))
    # email = models.EmailField(unique=True, verbose_name=("Email Address"))


# creer une commande personnalisée pour un utilisateur admin
