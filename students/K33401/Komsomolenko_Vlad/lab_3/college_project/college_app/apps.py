from django.apps import AppConfig


class CollegeAppConfig(AppConfig):
    name = 'college_app'

    def ready(self):
        import college_app.signals