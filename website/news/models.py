#region				-----External Imports-----
from django.db.models import (Model, CharField, TextField, 
SET_NULL, ForeignKey, DateTimeField)
from django.utils import timezone
from typing import TypeVar
#endregion

#region				-----Internal Imports-----
from gallery.models import Gallery
from .utils import (render_related_papers, 
reverse_related_url)
#endregion

#region				   -----Type Hints-----
Html=TypeVar("Html", str, bytes)
#endregion

class NewsFeed(Model):
    #region           -----Information-----
    description=TextField(max_length=500, blank=True, null=True)
    title=CharField(max_length=100, blank=False)
    #endregion

    #region            -----Metadata----- 
    class Meta(object):
        verbose_name_plural="News Feed"
        verbose_name="News Feed"
    #endregion

    #region         -----Internal Methods-----
    #endregion

class Paper(Model):
    #region           -----Information-----
    story=TextField(max_length=500, blank=True, null=True)
    title=CharField(max_length=100, blank=False)
    #endregion

    #region            -----Database-----
    created_at=DateTimeField(default=timezone.now)
    #endregion

    #region            -----Relation-----
    gallery=ForeignKey(Gallery, blank=True, 
    null=True, on_delete=SET_NULL)
    #endregion

    #region            -----Metadata----- 
    class Meta(object):
        verbose_name_plural="Papers"
        verbose_name="Paper"
    #endregion

    #region         -----Internal Methods-----
    #endregion