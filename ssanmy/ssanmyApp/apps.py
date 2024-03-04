from django.apps import AppConfig


class SsanmyappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ssanmyApp'
    def ready(self):
        from .models import testPost
        from .deal_crawler import start_crawl
        start_crawl()