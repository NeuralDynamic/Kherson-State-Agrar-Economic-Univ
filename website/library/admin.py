#region				-----External Imports-----
from django.contrib.admin import ModelAdmin
from django.contrib import admin
#endregion

#region				-----Internal Imports-----
from .models import Library, Book
#endregion

#region               -----Admin Pages-----
class LibraryAdmin(ModelAdmin):
    fields=["title", "description", "_books"]
    readonly_fields=["_books"]
    list_display=["_title"]
    
class BookAdmin(ModelAdmin):
    list_display=["_title", "_library"]
    fields=["title", "description", 
    "authors", "cover", "library"]
#endregion

#region               -----Page Record-----
admin.site.register(Library, LibraryAdmin)
admin.site.register(Book, BookAdmin)
#endregion