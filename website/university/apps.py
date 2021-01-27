#region				-----External Imports-----
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _
#endregion

class UniversityConfig(AppConfig):
    verbose_name=_("University App")
    name="university"

    def ready(self)->None:
        """
        Connects app signals
        @return None
        """
        import university.signals