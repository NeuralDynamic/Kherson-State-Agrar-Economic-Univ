#region				-----External Imports-----
from django.db.models import (CharField, TextField,
ImageField, ForeignKey, CASCADE)
from django.utils.translation import ugettext_lazy as _
from parler.models import (TranslatableModel, TranslatedFields)
from typing import TypeVar
#endregion

#region				-----Internal Imports-----
from .utils import (render_related_images, 
reverse_related_url)
#endregion

#region				   -----Type Hints-----
Html=TypeVar("Html", str, bytes)
#endregion

class Gallery(TranslatableModel):
    #region           -----Translation-----
    translations=TranslatedFields(
    description=TextField(verbose_name=_("Description"),
    max_length=1500, blank=True, null=True),
    title=CharField(verbose_name=_("Title"),
    max_length=100, blank=False))
    #endregion

    #region            -----Metadata-----
    class Meta(object):
        verbose_name_plural=_("Galleries")
        verbose_name=_("Gallery")
    #endregion

    #region         -----Internal Methods-----
    def _images(self)->Html:
        """@return related images"""
        return render_related_images(
        images=self.images.all()[:5])

    def __str__(self)->str:
        """@return gallery title"""
        return self.title
    #endregion

    #region          -----Rename Methods-----
    _images.short_description=_("Images")
    #endregion

class Image(TranslatableModel):
    #region           -----Translation-----
    translations=TranslatedFields(
    description=TextField(verbose_name=_("Description"),
    max_length=1500, blank=True, null=True),
    image=ImageField(verbose_name=_("Image"),
    upload_to="images", blank=False))
    #endregion

    #region            -----Relation-----
    gallery=ForeignKey("Gallery", blank=False, 
    null=False, on_delete=CASCADE, default=1,
    verbose_name=_("Gallery"),
    related_name="images")
    #endregion

    #region            -----Metadata----- 
    class Meta(object):
        verbose_name_plural=_("Images")
        verbose_name=_("Image")
    #endregion

    #region         -----Internal Methods-----
    def _gallery(self)->Html:
        """@return gallery link"""
        return reverse_related_url(
        title=self.gallery.title,
        id=self.gallery.pk, 
        model="gallery",
        app="gallery")

    def _title(self)->Html:
        """@return editing link"""
        return reverse_related_url(
        id=self.pk, model="image",
        title=self.image.name,
        app="gallery")

    def __str__(self)->str:
        """@return image url"""
        return self.image.url
    #endregion