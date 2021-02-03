#region				-----External Imports-----
from django.db.models import (CharField, TextField, 
OneToOneField, DateTimeField, CASCADE, SET_NULL, 
ForeignKey, ImageField)
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from parler.models import (TranslatableModel, TranslatedFields)
from typing import (TypeVar, List)
#endregion

#region				-----Internal Imports-----
from gallery.models import Gallery
from .utils import (render_related_papers, 
reverse_related_url)
#endregion

#region				   -----Type Hints-----
Html=TypeVar("Html", str, bytes)
#endregion

class NewsFeed(TranslatableModel):
    #region           -----Translation-----
    translations=TranslatedFields(
    description=TextField(verbose_name=_("Description"),
    max_length=500, blank=True, null=True),

    title=CharField(verbose_name=_("Title"),
    max_length=100, blank=False))
    #endregion

    #region            -----Metadata----- 
    class Meta(object):
        verbose_name_plural=_("News Feed")
        verbose_name=_("News Feed")
    #endregion

    #region         -----Internal Methods-----
    def searching_fields(self)->List[str]:
        """@return translated fields"""
        return ["translations__title",
        "translations__description"]

    def _papers(self)->Html:
        """@return related papers"""
        return render_related_papers(
        papers=self.papers.all()[:5])

    def __str__(self)->str:
        """@return feed title"""
        return self.title
    #endregion

    #region          -----Rename Methods-----
    _papers.short_description=_("Papers")
    #endregion

class Paper(TranslatableModel):
    #region           -----Information-----
    header=ImageField(verbose_name=_("Header"), 
    upload_to="headers", blank=False, 
    default="")
    #endregion

    #region           -----Translation-----
    translations=TranslatedFields(
    story=TextField(verbose_name=_("Story"),
    max_length=1500, blank=False),
    
    title=CharField(verbose_name=_("Title"),
    max_length=100, blank=False))
    #endregion

    #region            -----Database-----
    created_at=DateTimeField(default=timezone.now)
    #endregion

    #region            -----Relation-----
    news_feed=ForeignKey("NewsFeed", default=1, 
    null=False, on_delete=CASCADE, blank=False,
    verbose_name=_("News Feed"),
    related_name="papers")
    gallery=OneToOneField(Gallery, blank=True, 
    null=True, on_delete=SET_NULL, 
    verbose_name=_("Gallery"),
    related_name="paper")
    #endregion

    #region            -----Metadata----- 
    class Meta(object):
        verbose_name_plural=_("Papers")
        verbose_name=_("Paper")
    #endregion

    #region         -----Internal Methods-----
    def searching_fields(self)->List[str]:
        """@return translated fields"""
        return ["translations__title",
        "translations__story"]

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

    def __str__(self)->str:
        """@return image url"""
        return self.title
    #endregion