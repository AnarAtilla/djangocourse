from django.apps import AppConfig

class LagerhouseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'lagerhouse'

    def ready(self):
        import lagerhouse.signals