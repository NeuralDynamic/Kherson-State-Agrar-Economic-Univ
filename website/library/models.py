#region				-----External Imports-----
from djangocms_text_ckeditor.fields import HTMLField
from django.db.models import (TextField, CharField, ImageField, 
ManyToManyField, CASCADE, URLField)
from django.utils.translation import ugettext_lazy as _
from parler.models import (TranslatableModel, TranslatedFields)
from typing import (TypeVar, List)
#endregion

#region				   -----Type Hints-----
Html=TypeVar("Html", str, bytes)
#endregion

class Book(TranslatableModel):
    #region           -----Translation-----
    translations=TranslatedFields(
    description=HTMLField(verbose_name=_("Description"),
    max_length=1500, blank=True, null=True),

    authors=HTMLField(verbose_name=_("Authors"),
    max_length=500, blank=False),
    
    title=CharField(verbose_name=_("Title"),
    max_length=300, blank=False))
    #endregion

    #region           -----Information-----
    link=URLField(verbose_name=_("Link"), null=True,
    max_length=300, blank=True)
    cover=ImageField(verbose_name=_("Cover"),
    upload_to="covers", blank=False)
    #endregion

    #region            -----Metadata----- 
    class Meta(object):
        verbose_name_plural=_("Books")
        verbose_name=_("Book")
    #endregion

    #region         -----Internal Methods-----
    def searching_fields(self)->List[str]:
        """@return translated fields"""
        return ["translations__title",
        "translations__description",
        "translations__authors"]

    def __str__(self)->str:
        """@return book title"""
        return self.title
    #endregion