# apps/events/apps.py
from django.apps import AppConfig


class EventsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.events'

    # activamos los signals
    def ready(self):
        import apps.events.signals