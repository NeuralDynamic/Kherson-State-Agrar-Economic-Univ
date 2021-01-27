#region				-----External Imports-----
from django.contrib.admin import (ModelAdmin, register)
from django.contrib import admin
#endregion

#region				-----Internal Imports-----
from .models import (Links, Staff, Speciality,
Cathedra, Faculty, StaffCathedra, StaffFaculty)
#endregion

@register(StaffCathedra)
class StaffCathedraAdmin(ModelAdmin):
    #region           ----Configuration-----
    list_display=["staff", "rank", "cathedras"]
    #endregion

@register(StaffFaculty)
class StaffFacultyAdmin(ModelAdmin):
    #region           ----Configuration-----
    list_display=["staff", "position", "faculties"]
    #endregion

@register(Speciality)
class SpecialityAdmin(ModelAdmin):
    #region           ----Configuration-----
    fields=["number", "title", "cathedra",
    "description"]
    list_display=["__str__", "number"]
    #endregion

@register(Cathedra)
class CathedraAdmin(ModelAdmin):
    #region           ----Configuration-----
    fields=["emblem", "title", "faculty",
    "created_at", "goal", "description", 
    "gallery"]
    list_display=["__str__"]
    #endregion

@register(Faculty)
class FacultyAdmin(ModelAdmin):
    #region           ----Configuration-----
    fields=["emblem", "title", "description", 
    "gallery"]
    list_display=["__str__"]
    #endregion

@register(Staff)
class StaffAdmin(ModelAdmin):
    #region           ----Configuration-----
    list_display=["__str__", "phone"]
    fields=["photo", "first_name", 
    "second_name", "third_name", 
    "phone", "emails", "library", 
    "description"]
    #endregion