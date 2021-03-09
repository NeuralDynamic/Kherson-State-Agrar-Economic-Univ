#region				-----External Imports-----
from djangocms_text_ckeditor.fields import HTMLField
from django.db.models import (CharField, TextField, 
OneToOneField, DateTimeField, DateField, CASCADE, SET_NULL, 
ForeignKey, ImageField, BooleanField,URLField)
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.urls import reverse
from parler.models import (TranslatableModel, TranslatedFields)
from gallery.models import Gallery
from typing import (TypeVar, List)
#endregion

#region				-----Internal Imports-----
from .utils import (render_related_papers, 
reverse_related_url)
#endregion

#region				   -----Type Hints-----
Html=TypeVar("Html", str, bytes)
#endregion

class Categories(TranslatableModel):
    #region           -----Translation-----
    translations=TranslatedFields(
    title=CharField(verbose_name=_("Title"),
    blank=False, null=True, max_length=100,
    unique=True))
    #endregion

    #region            -----Metadata-----
    class Meta(object):
        verbose_name_plural=_("Categories")
        verbose_name=_("Category")
    #endregion

    #region         -----Internal Methods-----
    def __str__(self)->str:
        """@return category title"""
        return self.title
    #endregion

class NewsFeed(TranslatableModel):
    #region           -----Translation-----
    translations=TranslatedFields(
    description=HTMLField(verbose_name=_("Description"),
    blank=True, null=True),

    title=CharField(verbose_name=_("Title"),
    max_length=100, blank=False))
    #endregion

    #region            -----Metadata----- 
    class Meta(object):
        verbose_name_plural=_("News Feed")
        verbose_name=_("News Feed")
    #endregion

    #region         -----Internal Methods-----
    def get_absolute_url(self)->str:
        return f"/news"

    def searching_fields(self)->List[str]:
        """@return translated fields"""
        return ["translations__title",
        "translations__description"]

    def _papers(self)->Html:
        """@return related papers"""
        return render_related_papers(
        papers=self.papers.all())

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
    primary=BooleanField(verbose_name=_("Primary article"),
    default=False)
    #endregion

    #region           -----Translation-----
    translations=TranslatedFields(
    story=HTMLField(verbose_name=_("Story"),
    blank=False),
    
    title=CharField(verbose_name=_("Title"),
    max_length=300, blank=False),
    
    authors=CharField(verbose_name=_("Authors"),
    max_length=300, blank=False))
    #endregion

    #region            -----Database-----
    created_at=DateField(verbose_name=_("Article date"),
    default=timezone.now)
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
    category=ForeignKey(Categories, blank=True,
    null=True, on_delete=SET_NULL,
    verbose_name=_("Category"),
    related_name="papers")
    #endregion

    #region            -----Metadata----- 
    class Meta(object):
        verbose_name_plural=_("Papers")
        verbose_name=_("Paper")
        ordering = ['-created_at']
    #endregion

    #region         -----Internal Methods-----
    def get_absolute_url(self)->str:
        return reverse('article', kwargs={'paper_id':self.pk})

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

class Announcement(TranslatableModel):
    #region           -----Translation-----
    translations=TranslatedFields(
        title=CharField(verbose_name=_("Title"),
            max_length=100, blank=False),
        description=TextField(verbose_name=_("Description"),
            blank=True, default=""),
    )
    #endregion

    #region            -----Database-----
    image=ImageField(verbose_name=_("Image"), 
    upload_to="announcements", blank=True)
    attach=URLField(verbose_name=_("Attach"),
    blank=True, null=True)
    active=BooleanField(verbose_name=_("Active announcement"),
    default=True)
    date=DateField(verbose_name=_("Announcement date"),
    default=timezone.now)
    #endregion

    #region            -----Metadata----- 
    class Meta(object):
        verbose_name_plural=_("Announcements")
        verbose_name=_("Announcement")
    #endregion

    def __str__(self)->str:
        return self.title
