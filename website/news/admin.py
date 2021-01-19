#region				-----External Imports-----
from django.contrib.admin import ModelAdmin
from django.contrib import admin
#endregion

#region				-----Internal Imports-----
from .models import NewsFeed, Paper
#endregion

#region               -----Admin Pages-----
class NewsFeedAdmin(ModelAdmin):
    fields=["title", "description", "_papers"]
    readonly_fields=["_papers"]
    list_display=["_title"]
    
class PaperAdmin(ModelAdmin):
    fields=["title", "story", "news_feed", "gallery"]
    list_display=["_title", "_news_feed", "_gallery"]
#endregion

#region               -----Page Record-----
admin.site.register(NewsFeed, NewsFeedAdmin)
admin.site.register(Paper, PaperAdmin)
#endregion