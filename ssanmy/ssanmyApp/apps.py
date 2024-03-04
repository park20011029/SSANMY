from django.apps import AppConfig


class SsanmyappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ssanmyApp'
    def ready(self):
        import deal_crawler



