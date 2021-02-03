from django.contrib import admin
from cms.models import (Page,PageType, StaticPlaceholder, 
                        GlobalPagePermission,GlobalPagePermissionManager)


admin.site.site_header = "KSAU administration"
admin.site.site_title = "KSAU administration"
admin.site.index_title = "KSAU administration"