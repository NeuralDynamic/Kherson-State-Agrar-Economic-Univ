#region				-----External Imports-----
from django.db.models import (Model, CharField, TextField,
ImageField, ForeignKey, CASCADE)
from typing import TypeVar
#endregion

#region				-----Internal Imports-----
from .utils import (render_related_images, 
reverse_related_url)
#endregion

#region				   -----Type Hints-----
Html=TypeVar("Html", str, bytes)
#endregion

class Gallery(Model):
    #region           -----Information-----
    description=TextField(max_length=1500, blank=True, null=True)
    title=CharField(max_length=100, blank=False, null=False)
    #endregion

    #region            -----Metadata-----
    class Meta(object): 
        verbose_name_plural="Galleries"
        verbose_name="Gallery"
    #endregion

    #region         -----Internal Methods-----
    def _images(self)->Html:
        """@return related images"""
        return render_related_images(
        images=self.image_set.all()[:5])

    def __str__(self)->str:
        """@return gallery title"""
        return self._title()
        
    def _title(self)->str:
        """@return gallery title"""
        return self.title
    #endregion

class Image(Model): 
    #region           -----Information-----
    description=TextField(max_length=1500, blank=True, null=True)
    image=ImageField(upload_to="images", blank=False)
    #endregion

    #region            -----Relation-----
    gallery=ForeignKey("Gallery", blank=False, 
    null=False, on_delete=CASCADE, default=1)
    #endregion

    #region            -----Metadata----- 
    class Meta(object):
        verbose_name_plural="Images"
        verbose_name="Image"
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
        return self._url()

    def _url(self)->str:
        """@return image url"""
        return self.image.url
    #endregion