#region				-----External Imports-----
from datetime import date
from django.db.models import (Model, URLField, OneToOneField,
CASCADE, CharField, ForeignKey, SET_NULL, ImageField, 
TextField, DateField, ManyToManyField, IntegerField)
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from parler.models import (TranslatableModel, TranslatedFields)
from typing import (TypeVar, List)
from multi_email_field.fields import MultiEmailField
#endregion

#region				-----Internal Imports-----
from gallery.models import Gallery
from library.models import Library
#endregion

#region             -----Connecting Table-----
class StaffCathedra(TranslatableModel):
    #region           -----Translation-----
    translations=TranslatedFields(
    rank=CharField(verbose_name=_("Rank"),
    max_length=100, blank=True, null=True))
    #endregion

    #region            -----Relation-----
    cathedras=ForeignKey("Cathedra", on_delete=CASCADE, 
    null=True, verbose_name=_("Cathedra"))
    staff=ForeignKey("Staff", on_delete=CASCADE, 
    null=True, verbose_name=_("Staff"))
    #endregion

    #region            -----Metadata-----
    class Meta(object):
        verbose_name_plural=_("Cathedra staffs")
        verbose_name=_("Cathedra staff")
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
    max_length=100, blank=True, null=True))
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
#endregion

#region               -----Subdivisions-----
class Discipline(TranslatableModel):
    #region           -----Translation-----
    translations=TranslatedFields(
    title=CharField(verbose_name=_("Title"),
    max_length=100, blank=False, default=""))
    #endregion

    #region            -----Relation-----
    staff=ManyToManyField("Staff", blank=False,
    null=True, verbose_name=_("Staff"))
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
    #region           -----Translation-----
    translations=TranslatedFields(
    description=TextField(verbose_name=_("Description"),
    max_length=1500, blank=False, default=""),

    title=CharField(verbose_name=_("Title"),
    max_length=100, blank=False, default=""))
    #endregion

    #region           -----Information-----
    number=CharField(verbose_name=_("Number"),
    max_length=10, blank=False, default="")
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
    #region           -----Translation-----
    translations=TranslatedFields(
    description=TextField(verbose_name=_("Description"),
    max_length=1500, blank=False, default=""),

    goal=TextField(max_length=1500, blank=False,
    verbose_name=_("Goal"), default=""),

    title=CharField(verbose_name=_("Title"),
    max_length=100, blank=False, default=""))
    #endregion

    #region           -----Information-----
    emblem=ImageField(upload_to="cathedras/emblems", 
    blank=False, verbose_name=_("Emblem"), 
    default="")
    number=CharField(verbose_name=_("Number"),
    max_length=20, blank=False, default="")
    #endregion

    #region            -----Database-----
    created_at=DateField(default=timezone.now,
    verbose_name=_("Created at"))
    #endregion

    #region            -----Relation-----
    faculty=ForeignKey("Faculty", blank=False,
    null=False, on_delete=CASCADE, default=1,
    verbose_name=_("Faculty"),
    related_name="cathedras")
    gallery=ForeignKey(Gallery, blank=True,
    null=True, on_delete=SET_NULL,
    verbose_name=_("Gallery"),
    related_name="cathedras")
    staff=ManyToManyField("StaffCathedra",
    verbose_name=_("Staff"))
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
        "translations__goal"]

    def __str__(self)->str:
        """@return title of cathedra"""
        return self.title
    #endregion

class Faculty(TranslatableModel):
    #region           -----Translation-----
    translations=TranslatedFields(
    description=TextField(verbose_name=_("Description"),
    max_length=1500, blank=False, default=""),

    title=CharField(verbose_name=_("Title"),
    max_length=100, blank=False, default=""))
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
#endregion

#region                  -----Staff-----
class Reward(TranslatableModel):
    YEAR_CHOICES = [(r,r) for r in reversed(
    range(1950, date.today().year+1))]

    #region           -----Translation-----
    translations=TranslatedFields(
    title=CharField(max_length=300, blank=False,
    verbose_name=_("Title")))
    #endregion

    #region           -----Information-----
    year = IntegerField(verbose_name=_("Year"), 
    choices=YEAR_CHOICES, null=True)
    #endregion

    #region            -----Relation-----
    staff=ManyToManyField("Staff", blank=False,
    null=True, verbose_name=_("Staff"))
    #endregion

    #region            -----Metadata-----
    class Meta(object):
        verbose_name_plural=_("Rewards")
        verbose_name=_("Reward")
    #endregion

    #region         -----Internal Methods-----
    def __str__(self)->str:
        """@return title of reqard"""
        return self.title
    #endregion

class Staff(TranslatableModel):
    #region           -----Translation-----
    translations=TranslatedFields(
    second_name=CharField(max_length=40, blank=False,
    verbose_name=_("Second name")),

    first_name=CharField(max_length=40, blank=False,
    verbose_name=_("First name")),

    third_name=CharField(max_length=40, blank=False,
    verbose_name=_("Third name")),
    
    rank=CharField(max_length=100, blank=True,
    verbose_name=_("Rank")),

    methodical_works=TextField(blank=False,
    verbose_name=_("Methodical works")),

    description=TextField(blank=False,
    verbose_name=_("Description")))
    #endregion

    #region           -----Information-----
    photo=ImageField(verbose_name=_("Photo"),
    upload_to="photos", blank=False)
    phone=CharField(max_length=20, blank=False,
    verbose_name=_("Phone number"))
    emails=MultiEmailField()
    #endregion

    #region            -----Relation-----
    library=ForeignKey(Library, blank=True,
    null=True, on_delete=SET_NULL,
    verbose_name=_("Library"),
    related_name="staff")
    #endregion

    #region            -----Metadata-----
    class Meta(object):
        verbose_name_plural=_("Staff")
        verbose_name=_("Staff")
    #endregion

    #region         -----Internal Methods-----
    def searching_fields(self)->List[str]:
        """@return translated fields"""
        return ["translations__first_name",
        "translations_methodical_works",
        "translations__second_name",
        "translations__description",
        "translations__third_name"]

    def __str__(self)->str:
        """@return staff information"""
        return (self.second_name+
        " "+self.first_name+
        " "+self.third_name)
    #endregion

class Links(Model):
    #region           -----Information-----
    google_scholar=URLField(max_length=200, blank=True,
    verbose_name=_("Google Scholar"), null=True)
    web_of_science=URLField(max_length=200, blank=True,
    verbose_name=_("Web Of Science"), null=True)
    researchgate=URLField(max_length=200, blank=True,
    verbose_name=_("Researchgate"), null=True)
    scopus=URLField(verbose_name=_("Scopus"),
    max_length=200, blank=True, null=True)
    orcid=URLField(verbose_name=_("ORCID"),
    max_length=200, blank=True, null=True)
    #endregion

    #region            -----Relation-----
    staff=OneToOneField("Staff", blank=False,
    null=False, on_delete=CASCADE, default=1,
    verbose_name=_("Staff"))
    #endregion    

    #region            -----Metadata-----
    class Meta(object):
        verbose_name_plural=_("Links")
        verbose_name=_("Links")
    #endregion

    #region         -----Internal Methods-----
    def __str__(self)->str:
        """@return staff information"""
        return (self.staff.second_name+
        " "+self.staff.first_name+
        " "+self.staff.third_name)
    #endregion
#endregion