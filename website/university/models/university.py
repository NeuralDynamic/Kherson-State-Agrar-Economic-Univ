#region				-----External Imports-----
from datetime import date
from djangocms_text_ckeditor.fields import HTMLField
from django.db.models import (Model, URLField, OneToOneField,
CASCADE, CharField, ForeignKey, SET_NULL, ImageField, 
TextField, DateField, ManyToManyField, IntegerField, Choices)
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from gallery.models import Gallery
from parler.models import (TranslatableModel, TranslatedFields)
from typing import (TypeVar, List)
from multi_email_field.fields import MultiEmailField
#endregion

#region				-----Internal Imports-----
from .utils import MaterialBaseNode
#endregion

class ScientificSociety(TranslatableModel):
    #region           -----Translation-----
    translations=TranslatedFields(
    description=HTMLField(verbose_name=_("Description"),
    blank=False, default=""),

    sub_title=CharField(verbose_name=_("Sub title"),
    max_length=400, blank=False, default=""))
    #endregion

    #region           -----Information-----
    phone=CharField(max_length=20, blank=False,
    verbose_name=_("Phone number"))
    emails=MultiEmailField()
    #endregion

    #region            -----Relations-----
    staff=ManyToManyField("Staff",
    verbose_name=_("Staffs"),
    related_name="staff")
    #endregion

    #region            -----Metadata-----
    class Meta(object):
        verbose_name_plural=_("Scientific Societies")
        verbose_name=_("Scientific Society")
    #endregion

class Discipline(TranslatableModel):
    #region           -----Translation-----
    translations=TranslatedFields(
    title=CharField(verbose_name=_("Title"),
    max_length=100, blank=False, default="",
    unique=True))
    #endregion

    #region            -----Metadata-----
    class Meta(object):
        verbose_name_plural=_("Disciplines")
        verbose_name=_("Discipline")
    #endregion

    #region         -----Internal Methods-----
    def __str__(self)->str:
        """@return title of discipline"""
        return self.title
    #endregion

class Speciality(TranslatableModel):
    EDUCATIONAL_RANKS=[(l, l) for l in [_("Junior bachelor"), 
    _("Bachelor"), _("Master"), _("PHD"),
    _("Doctor of Philosophy")]]

    FORM_OF_STUDING=[(f, f) for f in [_("Day"), _("Extramural"), 
    _("Day, Extramural")]]
    #region           -----Translation-----
    translations=TranslatedFields(
    description=HTMLField(verbose_name=_("Description"),
    blank=True, default=""),

    educational_level=CharField(choices=EDUCATIONAL_RANKS,
    blank=False, null=True, max_length=200,
    verbose_name=_("Educational Level")),

    form_of_studying=CharField(choices=FORM_OF_STUDING,
    blank=False, null=True, max_length=200),

    title=CharField(verbose_name=_("Title"),
    max_length=100, blank=False, default="", unique=True))
    #endregion

    #region           -----Information-----
    number=CharField(verbose_name=_("Number"),
    max_length=10, blank=False, default="", unique=True)
    #endregion

    #region            -----Relation-----
    cathedra=ForeignKey("Cathedra", blank=False,
    null=False, on_delete=CASCADE, default=1,
    related_name="specialities",
    verbose_name=_("Cathedra"))
    #endregion

    #region            -----Metadata-----
    class Meta(object):
        verbose_name_plural=_("Specialities")
        verbose_name=_("Speciality")
    #endregion

    #region         -----Internal Methods-----
    def searching_fields(self)->List[str]:
        """@return translated fields"""
        return ["translations__title",
        "translations__description"]

    def __str__(self)->str:
        """@return title of speciality"""
        return self.title
    #endregion

class Cathedra(TranslatableModel):
    YEAR_CHOICES = [(r,r) for r in reversed(
    range(1800, date.today().year+1))]

    #region           -----Translation-----
    translations=TranslatedFields(
    description=HTMLField(verbose_name=_("Description"),
    blank=True, default=""),

    goal=TextField(blank=False,
    verbose_name=_("Goal"), default=""),

    title=CharField(verbose_name=_("Title"),
    max_length=100, blank=False, default="", unique=True),
    
    history=HTMLField(verbose_name=_("History of cathedra"),
    blank=True, default=""),)
    #endregion

    #region           -----Information-----
    emblem=ImageField(upload_to="cathedras/emblems", 
    blank=False, verbose_name=_("Emblem"), 
    default="")
    phone=CharField(max_length=20, blank=True,
    verbose_name=_("Phone number"))
    emails=MultiEmailField(blank=True, null=True)
    year=IntegerField(verbose_name=_("Year"), 
    choices=YEAR_CHOICES, null=True)
    educational_programs=URLField(blank=True,
    verbose_name=_("Educational programs link"), null=True)
    catalog_of_disciplines=URLField(blank=True,
    verbose_name=_("Catalog of disciplines link"), null=True)
    #endregion

    #region            -----Relation-----
    faculty=ForeignKey("Faculty", blank=False,
    null=False, on_delete=CASCADE, default=1,
    verbose_name=_("Faculty"),
    related_name="cathedras")
    gallery=ForeignKey(Gallery, blank=True,
    null=True, on_delete=SET_NULL,
    verbose_name=_("Career guidance"),
    related_name="cathedras")
    staff=ManyToManyField("StaffCathedra",
    verbose_name=_("Staff"))
    material_technical_base=ManyToManyField(MaterialBaseNode,
    verbose_name=_("Material-technical base"), blank=True)
    #endregion

    #region            -----Metadata-----
    class Meta(object):
        verbose_name_plural=_("Cathedras")
        verbose_name=_("Cathedra")
    #endregion

    #region         -----Internal Methods-----
    def searching_fields(self)->List[str]:
        """@return translated fields"""
        return ["translations__title",
        "translations__description",
        "translations__goal",
        "translations__history"]

    def __str__(self)->str:
        """@return title of cathedra"""
        return self.title
    #endregion

class Faculty(TranslatableModel):
    #region           -----Translation-----
    translations=TranslatedFields(
    description=HTMLField(verbose_name=_("Description"),
    blank=True, default=""),

    title=CharField(verbose_name=_("Title"),
    max_length=100, blank=False, default="", unique=True),
    
    council_of_employers=HTMLField(verbose_name=_("Council of employers"),
    blank=False, default=""))
    #endregion

    #region           -----Information-----
    emblem=ImageField(upload_to="faculties/emblems", 
    blank=False, verbose_name=_("Emblem"), 
    default="")
    #endregion

    #region            -----Relation-----
    gallery=ForeignKey(Gallery, blank=True,
    null=True, on_delete=SET_NULL,
    verbose_name=_("Gallery"),
    related_name="faculties")
    staff=ManyToManyField("StaffFaculty",
    verbose_name=_("Staff"))
    scientific_society=ForeignKey(ScientificSociety, blank=True,
    null=True, on_delete=SET_NULL,
    verbose_name=_("Scientific Societies"),
    related_name="scientific_society")
    #endregion

    #region            -----Metadata-----
    class Meta(object):
        verbose_name_plural=_("Faculties")
        verbose_name=_("Faculty")
    #endregion

    #region         -----Internal Methods-----
    def searching_fields(self)->List[str]:
        """@return translated fields"""
        return ["translations__title",
        "translations__description"]

    def __str__(self)->str:
        """@return title of faculty"""
        return self.title
    #endregion