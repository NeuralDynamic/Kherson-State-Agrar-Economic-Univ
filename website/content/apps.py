#region				-----External Imports-----
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _
#endregion


class ContentConfig(AppConfig):
    verbose_name=_("Content App")
    name = 'content'
