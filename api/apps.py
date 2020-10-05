from django.apps import AppConfig


class ApiConfig(AppConfig):
    name = 'api'

    def ready(self):
        # Makes sure all signal handlers are connected
        from api import handlers  # noqa
