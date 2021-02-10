#region				-----External Imports-----
from django.contrib.sitemaps import Sitemap
#endregion

#region				-----Internal Imports-----
from university.models import (Staff, Faculty, Cathedra)
#endregion

class StaffSitemap(Sitemap):
    changefreq="monthly"
    priority=0.9

    def items(self):
        return Staff.objects.all()

    def lstmod(self, obj):
        return obj.updated

class FacultySitemap(Sitemap):
    changefreq="monthly"
    priority=0.9

    def items(self):
        return Faculty.objects.all()

    def lstmod(self, obj):
        return obj.updated

class CathedraSitemap(Sitemap):
    changefreq="monthly"
    priority=0.9

    def items(self):
        return Cathedra.objects.all()

    def lstmod(self, obj):
        return obj.updated