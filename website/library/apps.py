#region				-----External Imports-----
from django.utils.translation import ugettext_lazy as _
from django.apps import AppConfig
#endregion

class LibraryConfig(AppConfig):
    verbose_name=_("Library App")
    name = "library"

    def ready(self)->None:
        """
        Connects app signals
        @return None
        """
        import library.signals