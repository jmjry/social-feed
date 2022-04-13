from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = "project.users"

    def ready(self):
        import project.users.signals
