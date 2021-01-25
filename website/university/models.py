#region				-----External Imports-----
from django.db.models import (Model, URLField, OneToOneField,
CASCADE, CharField, ForeignKey, SET_NULL, ImageField, 
TextField, DateTimeField)
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
    rank=CharField(max_length=100, blank=True, null=True)
    #endregion

    #region            -----Relation-----
    staff=ForeignKey("Staff", on_delete=CASCADE, null=True)
    cathedra=ForeignKey("Cathedra", on_delete=CASCADE, 
    null=True)
    #endregion
class StaffFaculty(Model):
    #region           -----Information-----
    position=CharField(max_length=100, blank=True, null=True)
    #endregion

    #region            -----Relation-----
    staff=ForeignKey("Staff", on_delete=CASCADE, null=True)
    faculty=ForeignKey("Faculty", on_delete=CASCADE, 
    null=True)
    #endregion
#endregion

#region               -----Subdivisions-----
class Speciality(Model):
    #region           -----Information-----
    description=TextField(max_length=1500, blank=False, default="")
    title=CharField(max_length=100, blank=False, default="")
    number=CharField(max_length=10, blank=False, default="")
    #endregion

    #region            -----Relation-----
    cathedra=ForeignKey("Cathedra", blank=False,
    null=False, on_delete=CASCADE, default=1)
    #endregion

    #region            -----Metadata-----
    class Meta(object):
        verbose_name_plural="Specialities"
        verbose_name="Speciality"
    #endregion

    #region         -----Internal Methods-----
    def __str__(self)->str:
        """@return title of speciality"""
        return self.title
    #endregion

class Cathedra(Model):
    #region           -----Information-----
    description=TextField(max_length=1500, blank=False, default="")
    emblem=ImageField(upload_to="emblems", blank=False, default="")
    title=CharField(max_length=100, blank=False, default="")
    number=CharField(max_length=20, blank=False, default="")
    goal=CharField(max_length=500, blank=False, default="")
    #endregion

    #region            -----Database-----
    created_at=DateTimeField(default=timezone.now)
    #endregion

    #region            -----Relation-----
    faculty=ForeignKey("Faculty", blank=False,
    null=False, on_delete=CASCADE, default=1)
    gallery=ForeignKey(Gallery, blank=True,
    null=True, on_delete=SET_NULL)
    #endregion

    #region            -----Metadata-----
    class Meta(object):
        verbose_name_plural="Cathedras"
        verbose_name="Cathedra"
    #endregion

    #region         -----Internal Methods-----
    def __str__(self)->str:
        """@return title of cathedra"""
        return self.title
    #endregion
    
class Faculty(Model):
    #region           -----Information-----
    description=TextField(max_length=1500, blank=False, default="")
    emblem=ImageField(upload_to="emblems", blank=False, default="")
    title=CharField(max_length=100, blank=False, default="")
    #endregion

    #region            -----Relation-----
    gallery=ForeignKey(Gallery, blank=True,
    null=True, on_delete=SET_NULL)
    #endregion

    #region            -----Metadata-----
    class Meta(object):
        verbose_name_plural="Faculties"
        verbose_name="Faculty"
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
    google_scholar=URLField(max_length=200, blank=True, null=True)
    web_of_science=URLField(max_length=200, blank=True, null=True)
    researchgate=URLField(max_length=200, blank=True, null=True)
    scopus=URLField(max_length=200, blank=True, null=True)
    orcid=URLField(max_length=200, blank=True, null=True)
    #endregion

    #region            -----Relation-----
    staff=OneToOneField("Staff", blank=False,
    null=False, on_delete=CASCADE, default=1)
    #endregion    

    #region            -----Metadata-----
    class Meta(object):
        verbose_name_plural="Links"
        verbose_name="Links"
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
    description=TextField(max_length=1500, blank=False)
    photo=ImageField(upload_to="photos", blank=False)
    second_name=CharField(max_length=40, blank=False)
    first_name=CharField(max_length=40, blank=False)
    third_name=CharField(max_length=40, blank=False)
    phone=CharField(max_length=20, blank=False)
    rank=CharField(max_length=40, blank=False)
    emails=MultiEmailField()
    #endregion

    #region            -----Relation-----
    library=ForeignKey(Library, blank=True,
    null=True, on_delete=SET_NULL)
    #endregion

    #region            -----Metadata-----
    class Meta(object):
        verbose_name_plural="Staff"
        verbose_name="Staff"
    #endregion

    #region         -----Internal Methods-----
    def __str__(self)->str:
        """@return staff information"""
        return (self.second_name+
        " "+self.first_name+
        " "+self.third_name)
    #endregion
#endregion