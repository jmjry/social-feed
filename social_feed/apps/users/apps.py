from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = "social_feed.apps.users"

    def ready(self):
        import social_feed.apps.users.signals
