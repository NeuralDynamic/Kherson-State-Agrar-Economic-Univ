#region				-----External Imports-----
from django.contrib.admin import register
from django.contrib import admin
from parler.admin import TranslatableAdmin
#endregion

#region				-----Internal Imports-----
from .models import NewsFeed, Paper
#endregion

@register(NewsFeed)
class NewsFeedAdmin(TranslatableAdmin):
    #region           ----Configuration-----
    fields=["title", "description", "_papers"]
    readonly_fields=["_papers"]
    list_display=["__str__"]
    #endregion

@register(Paper)
class PaperAdmin(TranslatableAdmin):
    #region           ----Configuration-----
    ordering = ['created_at']
    fields=["header", "title", "story", 
    "news_feed", "gallery"]
    list_display=["__str__", "_news_feed", 
    "_gallery"]
    list_filter=["news_feed__translations__title",
    "gallery__translations__title"]
    #endregion