#region				-----External Imports-----
from django.apps import AppConfig
#endregion

class UniversityConfig(AppConfig):
    name = 'university'

    def ready(self)->None:
        """
        Connects app signals
        @return None
        """
        import university.signals