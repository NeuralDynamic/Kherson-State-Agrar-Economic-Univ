#region				-----External Imports-----
from django.contrib.admin import register
from django.contrib import admin
from parler.admin import TranslatableAdmin
#endregion

#region				-----Internal Imports-----
from .models import Library, Book
#endregion

@register(Library)
class LibraryAdmin(TranslatableAdmin):
    #region           ----Configuration-----
    fields=["title", "description", "_books"]
    readonly_fields=["_books"]
    list_display=["__str__"]
    #endregion

@register(Book)
class BookAdmin(TranslatableAdmin):
    #region           ----Configuration-----
    fields=["cover", "title", "description", 
    "authors", "libraries"]
    list_display=["__str__"]
    #endregion