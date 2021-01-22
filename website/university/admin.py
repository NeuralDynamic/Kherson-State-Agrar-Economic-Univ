#region				-----External Imports-----
from django.contrib.admin import ModelAdmin
from django.contrib import admin
#endregion

#region				-----Internal Imports-----
from .models import (Links, Staff, Speciality,
Cathedra, Faculty)
#endregion

#region               -----Admin Pages-----
class SpecialityAdmin(ModelAdmin):
    fields=["number", "title", "description"]
    list_display=["__str__", "number"]

class CathedraAdmin(ModelAdmin):
    fields=["emblem", "title", "created_at", 
    "goal", "description", "gallery"]
    list_display=["__str__"]

class FacultyAdmin(ModelAdmin):
    fields=["emblem", "title", "description",
    "gallery"]
    list_display=["__str__"]

class StaffAdmin(ModelAdmin):
    fields=["photo", "first_name", "second_name", 
    "third_name", "phone", "rank", "library", 
    "description"]
    list_display=["__str__", "phone", "rank"]
#endregion

#region               -----Page Record-----
admin.site.register(Speciality, SpecialityAdmin)
admin.site.register(Cathedra, CathedraAdmin)
admin.site.register(Faculty, FacultyAdmin)
admin.site.register(Staff, StaffAdmin)
admin.site.register(Links)
#endregion