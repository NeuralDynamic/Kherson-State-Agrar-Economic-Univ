#region				-----External Imports-----
from django.contrib.admin import (ModelAdmin, register)
from django.contrib import admin
#endregion

#region				-----Internal Imports-----
from .models import (Links, Staff, Speciality,
Cathedra, Faculty)
#endregion

@register(Speciality)
class SpecialityAdmin(ModelAdmin):
    #region           ----Configuration-----
    fields=["number", "title", "description"]
    list_display=["__str__", "number"]
    #endregion

@register(Cathedra)
class CathedraAdmin(ModelAdmin):
    #region           ----Configuration-----
    fields=["emblem", "title", "created_at", 
    "goal", "description", "gallery"]
    list_display=["__str__"]
    #endregion

@register(Faculty)
class FacultyAdmin(ModelAdmin):
    #region           ----Configuration-----
    fields=["emblem", "title", 
    "description", "gallery"]
    list_display=["__str__"]
    #endregion

@register(Staff)
class StaffAdmin(ModelAdmin):
    #region           ----Configuration-----
    list_display=["__str__", "phone", "rank"]
    fields=["photo", "first_name", 
    "second_name", "third_name", 
    "phone", "emails", "rank",
    "library", "description"]
    #endregion