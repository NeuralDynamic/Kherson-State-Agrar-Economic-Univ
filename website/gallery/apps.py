#region				-----External Imports-----
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _
#endregion

class GalleryConfig(AppConfig):
    verbose_name=_("Gallery App")
    name="gallery"

    def ready(self)->None:
        """
        Connects app signals
        @return None
        """
        import gallery.signals