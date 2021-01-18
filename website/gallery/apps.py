#region				-----External Imports-----
from django.apps import AppConfig
#endregion

class GalleryConfig(AppConfig):
    name = 'gallery'

    def ready(self)->None:
        """
        Connects app signals
        @return None
        """
        import gallery.signals