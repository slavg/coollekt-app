from django.apps import AppConfig
from rest_framework.authentication import TokenAuthentication


class CoollektConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'coollekt'
