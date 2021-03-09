from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from cms.models import (Page,PageType, StaticPlaceholder, 
                        GlobalPagePermission,GlobalPagePermissionManager)


admin.site.site_header = _("KSAU administration")
admin.site.site_title = _("KSAU administration")
admin.site.index_title = _("KSAU administration")