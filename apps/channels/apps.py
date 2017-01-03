from django.apps import AppConfig


class ChannelsConfig(AppConfig):
    name = 'channels'
    verbose_name = 'Channels'

    def ready(self):
        from .signals import *
