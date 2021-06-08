#region				-----External Imports-----
from django.contrib.sitemaps import Sitemap
#endregion

#region				-----Internal Imports-----
from .models import (Paper, NewsFeed)
#endregion

class PaperSitemap(Sitemap):
    changefreq="weekly"
    priority=0.8

    def items(self):
        return Paper.objects.all()

    def lstmod(self, obj):
        return obj.updated

class NewsSitemap(Sitemap):
    changefreq="weekly"
    priority=0.95

    def items(self):
        return NewsFeed.objects.all()

    def lstmod(self, obj):
        return obj.updated