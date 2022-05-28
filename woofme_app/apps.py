""" Imports """
from django.apps import AppConfig


class WoofmeAppConfig(AppConfig):
    """ app's initial configurations"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'woofme_app'
