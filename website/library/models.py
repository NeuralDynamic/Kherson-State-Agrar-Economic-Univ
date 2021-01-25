#region				-----External Imports-----
from django.db.models import (Model, TextField, CharField, 
ImageField, ManyToManyField, CASCADE)
from typing import TypeVar
#endregion

#region				-----Internal Imports-----
from .utils import (render_related_books)
#endregion

#region				   -----Type Hints-----
Html=TypeVar("Html", str, bytes)
#endregion

class Library(Model):
    #region           -----Information-----
    description=TextField(max_length=500, blank=True, null=True)
    title=CharField(max_length=500, blank=False)
    #endregion

    #region            -----Metadata----- 
    class Meta(object):
        verbose_name_plural="Libraries"
        verbose_name="Library"
    #endregion

    #region         -----Internal Methods-----
    def _books(self)->Html:
        """@return related books"""
        return render_related_books(
        books=self.book_set.all()[:5])

    def __str__(self)->str:
        """@return library title"""
        return self.title
    #endregion

class Book(Model):
    #region           -----Information-----
    description=TextField(max_length=1500, blank=True, null=True)
    cover=ImageField(upload_to="covers", blank=False)
    authors=TextField(max_length=500, blank=False)
    title=CharField(max_length=100, blank=False)
    #endregion

    #region            -----Relation-----
    library=ManyToManyField("Library")
    #endregion

    #region            -----Metadata----- 
    class Meta(object):
        verbose_name_plural="Books"
        verbose_name="Book"
    #endregion

    #region         -----Internal Methods-----
    def __str__(self)->str:
        """@return book title"""
        return self.title
    #endregion