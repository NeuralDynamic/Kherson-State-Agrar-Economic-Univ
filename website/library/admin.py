#region				-----External Imports-----
from django.contrib.admin import (ModelAdmin, register)
from django.contrib import admin
#endregion

#region				-----Internal Imports-----
from .models import Library, Book
#endregion

@register(Library)
class LibraryAdmin(ModelAdmin):
    fields=["title", "description", "_books"]
    readonly_fields=["_books"]
    list_display=["__str__"]

@register(Book)
class BookAdmin(ModelAdmin):
    fields=["cover", "title", "description", 
    "authors", "libraries"]
    list_display=["__str__"]