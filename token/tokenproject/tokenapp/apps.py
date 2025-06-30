from django.apps import AppConfig

class TokenappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tokenapp'

    def ready(self):
        import tokenapp.signals
