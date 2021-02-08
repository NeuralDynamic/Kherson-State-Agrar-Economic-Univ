#region				-----External Imports-----
from django.contrib.admin import register
from django.contrib import admin
from parler.admin import TranslatableAdmin
#endregion

#region				-----Internal Imports-----
from .models import Book
#endregion

@register(Book)
class BookAdmin(TranslatableAdmin):
    #region           ----Configuration-----
    fields=["cover", "title", "description", 
    "authors", "link"]
    list_display=["__str__"]
    #endregion