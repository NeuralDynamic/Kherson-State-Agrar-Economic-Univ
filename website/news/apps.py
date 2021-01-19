#region				-----External Imports-----
from django.apps import AppConfig
#endregion

class NewsConfig(AppConfig):
    name = 'news'

    def ready(self)->None:
        """
        Connects app signals
        @return None
        """
        import news.signals