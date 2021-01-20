#region				-----External Imports-----
from django.db.models import (Model, CharField, TextField, 
OneToOneField, DateTimeField, CASCADE, SET_NULL, 
ForeignKey)
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
    def _papers(self)->Html:
        """@return related papers"""
        return render_related_papers(
        papers=self.paper_set.all()[:5])

    def __str__(self)->str:
        """@return feed title"""
        return self._title()

    def _title(self)->str:
        """@return feed title"""
        return self.title
    #endregion

class Paper(Model):
    #region           -----Information-----
    story=TextField(max_length=1500, blank=False, default="")
    title=CharField(max_length=100, blank=False)
    #endregion

    #region            -----Database-----
    created_at=DateTimeField(default=timezone.now)
    #endregion

    #region            -----Relation-----
    news_feed=ForeignKey("NewsFeed", blank=False,
    null=False, on_delete=CASCADE, default=1)
    gallery=OneToOneField(Gallery, blank=True, 
    null=True, on_delete=SET_NULL)
    #endregion

    #region            -----Metadata----- 
    class Meta(object):
        verbose_name_plural="Papers"
        verbose_name="Paper"
    #endregion

    #region         -----Internal Methods-----
    def _news_feed(self)->Html:
        """@return gallery link"""
        return reverse_related_url(
        title=self.news_feed.title,
        id=self.news_feed.pk, 
        model="newsfeed",
        app="news")

    def _gallery(self)->Html:
        """@return gallery link"""
        if self.gallery:
            return reverse_related_url(
            title=self.gallery.title,
            id=self.gallery.pk, 
            model="gallery",
            app="gallery")

    def _title(self)->Html:
        """@return editing link"""
        return reverse_related_url(
        id=self.pk, model="paper",
        title=self.title,
        app="news")

    def __str__(self)->str:
        """@return image url"""
        return self.title
    #endregion