#region				-----External Imports-----
from django.db.models import (Model, URLField, OneToOneField,
CASCADE, CharField, ForeignKey, SET_NULL, ImageField, 
TextField, DateField, ManyToManyField)
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from multi_email_field.fields import MultiEmailField
#endregion

#region				-----Internal Imports-----
from gallery.models import Gallery
from library.models import Library
#endregion

#region             -----Connecting Table-----
class StaffCathedra(Model):
    #region           -----Information-----
    rank=CharField(verbose_name=_("Rank"),
    max_length=100, blank=True, null=True)
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
    def __str__(self)->str:
        """@return name of staff and its rank"""
        return f"{self.staff} {self.cathedras}"
    #endregion

class StaffFaculty(Model):
    #region           -----Information-----
    position=CharField(verbose_name=_("Position"),
    max_length=100, blank=True, null=True)
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
    def __str__(self)->str:
        """@return name of staff and its rank"""
        return f"{self.staff} {self.faculties}"
    #endregion
#endregion

#region               -----Subdivisions-----
class Speciality(Model):
    #region           -----Information-----
    description=TextField(verbose_name=_("Description"),
    max_length=1500, blank=False, default="")
    number=CharField(verbose_name=_("Number"),
    max_length=10, blank=False, default="")
    title=CharField(verbose_name=_("Title"),
    max_length=100, blank=False, default="")
    #endregion

    #region            -----Relation-----
    cathedra=ForeignKey("Cathedra", blank=False,
    null=False, on_delete=CASCADE, default=1,
    verbose_name=_("Cathedra"))
    #endregion

    #region            -----Metadata-----
    class Meta(object):
        verbose_name_plural=_("Specialities")
        verbose_name=_("Speciality")
    #endregion

    #region         -----Internal Methods-----
    def __str__(self)->str:
        """@return title of speciality"""
        return self.title
    #endregion

class Cathedra(Model):
    #region           -----Information-----
    description=TextField(verbose_name=_("Description"),
    max_length=1500, blank=False, default="")
    emblem=ImageField(upload_to="cathedras/emblems", 
    blank=False, verbose_name=_("Emblem"), 
    default="")
    goal=TextField(max_length=1500, blank=False,
    verbose_name=_("Goal"), default="")
    number=CharField(verbose_name=_("Number"),
    max_length=20, blank=False, default="")
    title=CharField(verbose_name=_("Title"),
    max_length=100, blank=False, default="")
    #endregion

    #region            -----Database-----
    created_at=DateField(default=timezone.now,
    verbose_name=_("Created at"))
    #endregion

    #region            -----Relation-----
    faculty=ForeignKey("Faculty", blank=False,
    null=False, on_delete=CASCADE, default=1,
    verbose_name=_("Faculty"))
    gallery=ForeignKey(Gallery, blank=True,
    null=True, on_delete=SET_NULL,
    verbose_name=_("Gallery"))
    staffs=ManyToManyField("StaffCathedra",
    verbose_name=_("Staff"))
    #endregion

    #region            -----Metadata-----
    class Meta(object):
        verbose_name_plural=_("Cathedras")
        verbose_name=_("Cathedra")
    #endregion

    #region         -----Internal Methods-----
    def __str__(self)->str:
        """@return title of cathedra"""
        return self.title
    #endregion

class Faculty(Model):
    #region           -----Information-----
    description=TextField(verbose_name=_("Description"),
    max_length=1500, blank=False, default="")
    emblem=ImageField(upload_to="faculties/emblems", 
    blank=False, verbose_name=_("Emblem"), 
    default="")
    title=CharField(verbose_name=_("Title"),
    max_length=100, blank=False, default="")
    #endregion

    #region            -----Relation-----
    gallery=ForeignKey(Gallery, blank=True,
    null=True, on_delete=SET_NULL,
    verbose_name=_("Gallery"))
    staffs=ManyToManyField("StaffFaculty",
    verbose_name=_("Staff"))
    #endregion

    #region            -----Metadata-----
    class Meta(object):
        verbose_name_plural=_("Faculties")
        verbose_name=_("Faculty")
    #endregion

    #region         -----Internal Methods-----
    def __str__(self)->str:
        """@return title of faculty"""
        return self.title
    #endregion
#endregion

#region                  -----Staff-----
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

class Staff(Model):
    #region           -----Information-----
    description=TextField(verbose_name=_("Description"),
    max_length=1500, blank=False)
    photo=ImageField(verbose_name=_("Photo"),
    upload_to="photos", blank=False)
    second_name=CharField(max_length=40, blank=False,
    verbose_name=_("Second name"))
    first_name=CharField(max_length=40, blank=False,
    verbose_name=_("First name"))
    third_name=CharField(max_length=40, blank=False,
    verbose_name=_("Third name"))
    phone=CharField(max_length=20, blank=False,
    verbose_name=_("Phone number"))
    emails=MultiEmailField()
    #endregion

    scientific_title=CharField(max_length=40, blank=False,
    verbose_name=_("Second name"))

    #region            -----Relation-----
    library=ForeignKey(Library, blank=True,
    null=True, on_delete=SET_NULL,
    verbose_name=_("Library"))
    #endregion

    #region            -----Metadata-----
    class Meta(object):
        verbose_name_plural=_("Staff")
        verbose_name=_("Staff")
    #endregion

    #region         -----Internal Methods-----
    def __str__(self)->str:
        """@return staff information"""
        return (self.second_name+
        " "+self.first_name+
        " "+self.third_name)
    #endregion
#endregion