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
    list_display=["_title"]

class ImageAdmin(ModelAdmin):
    list_display=["_title", "_url", "_gallery"]
    fields=["image", "gallery", "description"]
#endregion

#region               -----Page Record-----
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Image, ImageAdmin)
#endregion