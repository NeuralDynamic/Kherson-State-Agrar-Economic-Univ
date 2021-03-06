#region				-----External Imports-----
from datetime import date
from djangocms_text_ckeditor.fields import HTMLField
from django.db.models import (Model, URLField, OneToOneField,
CASCADE, CharField, ForeignKey, SET_NULL, ImageField, 
TextField, DateField, ManyToManyField, IntegerField)
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from parler.models import (TranslatableModel, TranslatedFields)
from typing import (TypeVar, List)
from multi_email_field.fields import MultiEmailField
#endregion

class StaffCathedra(TranslatableModel):
    #region           -----Translation-----
    translations=TranslatedFields(
    rank=CharField(verbose_name=_("Rank"),
    max_length=300, blank=True, null=True))
    #endregion

    #region            -----Relation-----
    cathedras=ForeignKey("Cathedra", on_delete=CASCADE, 
    null=True, verbose_name=_("Department"))
    staff=ForeignKey("Staff", on_delete=CASCADE, 
    null=True, verbose_name=_("Staff"))
    #endregion

    #region            -----Metadata-----
    class Meta(object):
        verbose_name_plural=_("Department staffs")
        verbose_name=_("Department staff")
    #endregion

    #region         -----Internal Methods-----
    def searching_fields(self)->List[str]:
        """@return translated fields"""
        return ["translations__rank"]

    def __str__(self)->str:
        """@return name of staff and its rank"""
        return f"{self.staff} {self.cathedras}"
    #endregion

class StaffFaculty(TranslatableModel):
    #region           -----Information-----
    translations=TranslatedFields(
    position=CharField(verbose_name=_("Position"),
    max_length=300, blank=True, null=True))
    #endregion

    #region            -----Relation-----
    faculties=ForeignKey("Faculty", on_delete=CASCADE, 
    null=True, verbose_name=_("Faculty"))
    staff=ForeignKey("Staff", on_delete=CASCADE, 
    null=True, verbose_name=_("Staff"))
    #endregion

    #region            -----Metadata-----
    class Meta(object):
        verbose_name_plural=_("Faculty staffs")
        verbose_name=_("Faculty staff")
    #endregion

    #region         -----Internal Methods-----
    def searching_fields(self)->List[str]:
        """@return translated fields"""
        return ["translations__position"]

    def __str__(self)->str:
        """@return name of staff and its rank"""
        return f"{self.staff} {self.faculties}"
    #endregion

class MaterialBaseNode(TranslatableModel):
    #region           -----Information-----
    translations=TranslatedFields(
    local_title=CharField(verbose_name=_("Local title"), 
    help_text=_("""Additional field with local name 
    for best admin usage experience. Will be filled 
    from title field, if  field empty."""),
    max_length=100, blank=True, null=True),

    content=HTMLField(verbose_name=_("Content"),
    blank=False, default=""),

    title=CharField(verbose_name=_("Title"),
    max_length=100))
    #endregion

    #region            -----Metadata-----
    class Meta(object):
        verbose_name_plural=_("Material-technical bases")
        verbose_name=_("Material-technical base")
    #endregion

    #region         -----Internal Methods-----
    def searching_fields(self)->List[str]:
        """@return translated fields"""
        return ["translations__title"]

    def __str__(self)->str:
        """@return local title of node"""
        return f"{self.local_title}"
    #endregion