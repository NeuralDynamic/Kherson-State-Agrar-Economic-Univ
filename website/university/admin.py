#region				-----External Imports-----
from django.contrib.admin import register, ModelAdmin
from django.contrib import admin
from parler.admin import TranslatableAdmin
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.html import format_html
#endregion

#region				-----Internal Imports-----
from .models import (Staff, Speciality,
Cathedra, Faculty, StaffCathedra, StaffFaculty,
Discipline, Reward, ScientificSociety, MaterialBaseNode)
#endregion

@register(StaffCathedra)
class StaffCathedraAdmin(TranslatableAdmin):
    #region           ----Configuration-----
    list_display=["staff", "rank", "cathedras"]
    list_filter=["translations__rank", "cathedras"]
    #endregion

@register(StaffFaculty)
class StaffFacultyAdmin(TranslatableAdmin):
    #region           ----Configuration-----
    list_display=["staff", "position", "faculties"]
    list_filter=["translations__position", "faculties"]
    #endregion

@register(Discipline)
class DisciplineAdmin(TranslatableAdmin):
    #region           ----Configuration-----
    fields=["title"]
    list_display=["__str__"]
    #endregion

@register(Speciality)
class SpecialityAdmin(TranslatableAdmin):
    #region           ----Configuration-----
    fields=["number", "title", "cathedra",
    "educational_level", "form_of_studying",
    "description"]
    list_display=["__str__", "number", "faculty"]
    list_filter=["number", "cathedra__faculty"]
    #endregion

@register(Cathedra)
class CathedraAdmin(TranslatableAdmin):
    change_form_template="admin/university/change_form.html"

    #region           ----Configuration-----
    fields=["emblem", "title", "year", "faculty",
    "educational_programs","catalog_of_disciplines",
    "goal", "description", "history",
    "gallery","material_technical_base", "phone", "emails"]
    list_display=["__str__", "faculty", "preview"]
    list_filter=["faculty"]
    #endregion

    #region         -----Internal Methods-----
    def response_change(self, request, obj):
        if "_preview" in request.POST:
            return HttpResponseRedirect(obj.get_absolute_url())
        return super().response_change(request, obj)
    def preview(self, obj)->str:
        return format_html(
            f"""<a class="button" target=_blank
            href={obj.get_absolute_url()}>Preview</a>"""
        )
    #endregion

@register(Faculty)
class FacultyAdmin(TranslatableAdmin):
    change_form_template="admin/university/change_form.html"

    #region           ----Configuration-----
    fields=["emblem", "title", "description", 
    "gallery", "scientific_society"]
    list_display=["__str__", "preview"]
    #endregion

    #region         -----Internal Methods-----
    def response_change(self, request, obj):
        if "_preview" in request.POST:
            return HttpResponseRedirect(obj.get_absolute_url())
        return super().response_change(request, obj)
    def preview(self, obj)->str:
        return format_html(
            f"""<a class="button" target=_blank
            href={obj.get_absolute_url()}>Preview</a>"""
        )
    #endregion

@register(Reward)
class RewardAdmin(TranslatableAdmin):
    #region           ----Configuration-----
    fields=["title", "year", "staff"]
    list_display=["__str__"]
    #endregion

@register(Staff)
class StaffAdmin(TranslatableAdmin):
    change_form_template="admin/university/change_form.html"
    
    #region           ----Configuration-----
    list_display=["__str__", "phone", "preview"]
    fields=["photo", "first_name", 
    "second_name", "third_name", "rank",
    "phone", "emails", "ndr_theme", "books", 
    "methodical_works","description", "disciplines",
    "google_scholar", "web_of_science", "researchgate",
    "scopus", "orcid"]
    #endregion

    #region         -----Internal Methods-----
    def response_change(self, request, obj):
        if "_preview" in request.POST:
            return HttpResponseRedirect(obj.get_absolute_url())
        return super().response_change(request, obj)
    def preview(self, obj)->str:
        return format_html(
            f"""<a class="button" target=_blank
            href={obj.get_absolute_url()}>Preview</a>"""
        )
    #endregion

@register(ScientificSociety)
class ScientificSocietyAdmin(TranslatableAdmin):
    #region           ----Configuration-----
    fields=["staff", "phone", "sub_title",
    "emails","description"]
    #endregion

@register(MaterialBaseNode)
class MaterialBaseNodeAdmin(TranslatableAdmin):
    #region           ----Configuration-----
    list_display=["__str__", "title"]
    fields=["title","local_title",
            "content"]
    #endregion