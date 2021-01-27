#region				-----External Imports-----
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _
#endregion

class NewsConfig(AppConfig):
    verbose_name=_("News App")
    name="news"

    def ready(self)->None:
        """
        Connects app signals
        @return None
        """
        import news.signals