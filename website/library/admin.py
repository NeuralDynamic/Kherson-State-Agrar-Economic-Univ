#region				-----External Imports-----
from django.contrib.admin import (ModelAdmin, register)
from django.contrib import admin
#endregion

#region				-----Internal Imports-----
from .models import Library, Book
#endregion

@register(Library)
class LibraryAdmin(ModelAdmin):
    #region           ----Configuration-----
    fields=["title", "description", "_books"]
    readonly_fields=["_books"]
    list_display=["__str__"]
    #endregion

@register(Book)
class BookAdmin(ModelAdmin):
    #region           ----Configuration-----
    fields=["cover", "title", "description", 
    "authors", "libraries"]
    list_display=["__str__"]
    #endregion