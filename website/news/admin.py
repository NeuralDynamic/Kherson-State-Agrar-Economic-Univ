#region				-----External Imports-----
from django.contrib.admin import (ModelAdmin, register)
from django.contrib import admin
#endregion

#region				-----Internal Imports-----
from .models import NewsFeed, Paper
#endregion

@register(NewsFeed)
class NewsFeedAdmin(ModelAdmin):
    #region           ----Configuration-----
    fields=["title", "description", "_papers"]
    readonly_fields=["_papers"]
    list_display=["__str__"]
    #endregion

@register(Paper)
class PaperAdmin(ModelAdmin):
    #region           ----Configuration-----
    fields=["header", "title", "story", 
    "news_feed", "gallery"]
    list_display=["__str__", "_news_feed", 
    "_gallery"]
    #endregion