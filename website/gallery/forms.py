#region				-----External Imports-----
from django.core.validators import validate_image_file_extension
from django.forms import (FileField, ClearableFileInput)
from django.utils.translation import ugettext_lazy as _
from parler.forms import TranslatableModelForm
#endregion

#region				-----Internal Imports-----
from .models import (Gallery, Image)
#endregion

class GalleryAdminForm(TranslatableModelForm):
    #region           -----Information-----
    images=FileField(label=_("Add images"), required=False,
    widget=ClearableFileInput(attrs={"multiple": True}))
    #endregion

    #region         -----Internal Methods-----
    def save_images(self, gallery: Gallery)->None:
        """
        Associates selected images with gallery\n
        :param gallery: gallery class instance\n
        @return None
        """
        [Image(gallery=gallery, image=image).save()
        for image in self.files.getlist("images")]
    def validate_image_extensions(self)->None:
        """
        Validates image file extensions and can
        raise exception if format is invalid\n
        @return None
        """
        [validate_image_file_extension(value=image)
        for image in self.files.getlist("images")]
    #endregion

    #region             -----Metadata-----
    class Meta(object):
        fields=["title", "description"]
        model=Gallery
    #endregion
