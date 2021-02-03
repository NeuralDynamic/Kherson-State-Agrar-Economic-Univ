#region				-----External Imports-----
from django.contrib.admin import register
from django.contrib import admin
from parler.admin import TranslatableAdmin
#endregion

#region				-----Internal Imports-----
from .models import (Links, Staff, Speciality,
Cathedra, Faculty, StaffCathedra, StaffFaculty,
Discipline, Reward, ScientificSociety)
#endregion

@register(StaffCathedra)
class StaffCathedraAdmin(TranslatableAdmin):
    #region           ----Configuration-----
    list_display=["staff", "rank", "cathedras"]
    #endregion

@register(StaffFaculty)
class StaffFacultyAdmin(TranslatableAdmin):
    #region           ----Configuration-----
    list_display=["staff", "position", "faculties"]
    #endregion

@register(Discipline)
class DisciplineAdmin(TranslatableAdmin):
    #region           ----Configuration-----
    fields=["title", "staff"]
    list_display=["__str__"]
    #endregion

@register(Speciality)
class SpecialityAdmin(TranslatableAdmin):
    #region           ----Configuration-----
    fields=["number", "title", "cathedra",
    "description"]
    list_display=["__str__", "number"]
    #endregion

@register(Cathedra)
class CathedraAdmin(TranslatableAdmin):
    #region           ----Configuration-----
    fields=["emblem", "title", "faculty",
    "created_at", "goal", "description", 
    "gallery"]
    list_display=["__str__"]
    #endregion

@register(Faculty)
class FacultyAdmin(TranslatableAdmin):
    #region           ----Configuration-----
    fields=["emblem", "title", "description", 
    "gallery"]
    list_display=["__str__"]
    #endregion

@register(Reward)
class RewardAdmin(TranslatableAdmin):
    #region           ----Configuration-----
    fields=["title", "year", "staff"]
    list_display=["__str__"]
    #endregion

@register(Staff)
class StaffAdmin(TranslatableAdmin):
    #region           ----Configuration-----
    list_display=["__str__", "phone"]
    fields=["photo", "first_name", 
    "second_name", "third_name", 
    "phone", "emails", "library", 
    "description"]
    #endregion

@register(ScientificSociety)
class ScientificSocietyAdmin(TranslatableAdmin):
    #region           ----Configuration-----
    fields=["description", "phone", "emails"
    "staff"]
    #endregion