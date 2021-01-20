#region				-----External Imports-----
from django.apps import AppConfig
#endregion

#region				-----Internal Imports-----
#endregion

#region				   -----Type Hints-----
#endregion

class LibraryConfig(AppConfig):
    name = 'library'

    def ready(self)->None:
        """
        Connects app signals
        @return None
        """
        import library.signals