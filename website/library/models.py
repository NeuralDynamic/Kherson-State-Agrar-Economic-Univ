#region				-----External Imports-----
from django.db.models import (Model, TextField, CharField, 
ImageField, ManyToManyField, CASCADE)
from django.utils.translation import ugettext_lazy as _
from typing import TypeVar
#endregion

#region				-----Internal Imports-----
from .utils import render_related_books
#endregion

#region				   -----Type Hints-----
Html=TypeVar("Html", str, bytes)
#endregion

class Library(Model):
    #region           -----Information-----
    description=TextField(verbose_name=_("Description"),
    max_length=500, blank=True, null=True)
    title=CharField(verbose_name=_("Title"),
    max_length=500, blank=False)
    #endregion

    #region            -----Metadata----- 
    class Meta(object):
        verbose_name_plural=_("Libraries")
        verbose_name=_("Library")
    #endregion

    #region         -----Internal Methods-----
    def _books(self)->Html:
        """@return related books"""
        return render_related_books(
        books=self.books.all()[:5])

    def __str__(self)->str:
        """@return library title"""
        return self.title
    #endregion

    #region          -----Rename Methods-----
    _books.short_description=_("Books")
    #endregion

class Book(Model):
    #region           -----Information-----
    description=TextField(verbose_name=_("Description"),
    max_length=1500, blank=True, null=True)
    authors=TextField(verbose_name=_("Authors"),
    max_length=500, blank=False)
    cover=ImageField(verbose_name=_("Cover"),
    upload_to="covers", blank=False)
    title=CharField(verbose_name=_("Title"),
    max_length=100, blank=False)
    #endregion

    #region            -----Relation-----
    libraries=ManyToManyField("Library", blank=False,
    verbose_name=_("Libraries"),
    related_name="books")
    #endregion

    #region            -----Metadata----- 
    class Meta(object):
        verbose_name_plural=_("Books")
        verbose_name=_("Book")
    #endregion

    #region         -----Internal Methods-----
    def __str__(self)->str:
        """@return book title"""
        return self.title
    #endregion