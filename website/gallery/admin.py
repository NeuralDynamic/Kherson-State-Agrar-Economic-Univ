#region				-----External Imports-----
from django.contrib.admin import ModelAdmin
from django.contrib import admin
#endregion

#region				-----Internal Imports-----
from .models import Gallery, Image
#endregion

#region               -----Admin Pages-----
class GalleryAdmin(ModelAdmin):
    fields=["title", "description", "_images"]
    readonly_fields=["_images"]
    list_display=["__str__"]

class ImageAdmin(ModelAdmin):
    fields=["image", "gallery", "description"]
    list_display=["_title", "_gallery"]
#endregion

#region               -----Page Record-----
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Image, ImageAdmin)
#endregion