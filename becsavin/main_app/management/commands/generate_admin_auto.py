from django.core.management.base import BaseCommand
from application.models import Myuser # À modifier par votre utilisateur personnalisé
import os


class Command(BaseCommand):
    def handle(self, *args, **options):
        if Myuser.objects.count() == 0:
            # -----cette partie n'est pas à modifier
            username = os.environ.get("USERNAME_ADMIN")
            email = os.environ.get("EMAIL_ADMIN")
            password = os.environ.get("PASSWORD_ADMIN")
            print('Création du compte admin {} / {}'.format(username, email))
            admin = Myuser.objects.create_user(email=email, username=username, password=password)
            # fin de la partie à ne pas modifier ci-dessous configurer vos champs personnalisés
            # exemple:
            # admin.useradmin = True
            admin.save()
        else:
            print("Les comptes administrateurs ne peuvent être initialisés que si aucun compte administrateur n'existe")