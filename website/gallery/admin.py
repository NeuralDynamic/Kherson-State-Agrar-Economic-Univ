#region				-----External Imports-----
from django.contrib.admin import (ModelAdmin, register)
from django.contrib import admin
from typing import (TypeVar, Dict, List)
#endregion

#region				-----Internal Imports-----
from .forms import GalleryAdminForm
from .models import (Gallery, Image)
#endregion

#region				   -----Type Hints-----
Http=TypeVar("Http", Dict, List)
#endregion

@register(Gallery)
class GalleryAdmin(ModelAdmin):
    #region           ----Configuration-----
    readonly_fields=["_images"]
    list_display=["__str__"]
    form=GalleryAdminForm
    #endregion

    #region         -----Internal Methods-----
    def save_related(self, request: Http, form: GalleryAdminForm,
    formsets: Dict, change: GalleryAdminForm)->None:
        """
        Overrides method to trigger save_related method\n
        :param change: form that is gonna be changed\n
        :param request: Http|Https request as dict\n
        :param formset: dictionary of aprameters\n
        :param form: GalleryAdminForm instance\n
        @return None
        """
        #*Traverses method through parent classes
        super().save_related(request=request, form=form,
        formsets=formsets, change=change)

        #*Validates extensions and create gallery
        try: form.validate_image_extensions()
        except: return "Invalid image format"
        else: form.save_images(form.instance)
    #endregion

@register(Image)
class ImageAdmin(ModelAdmin):
    #region           ----Configuration-----
    fields=["image", "gallery", "description"]
    list_display=["_title", "_gallery"]
    #endregion