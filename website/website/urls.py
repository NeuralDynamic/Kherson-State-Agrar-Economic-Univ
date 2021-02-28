from content.views import manifest_view
from cms.sitemaps import CMSSitemap
from django.conf import settings
from django.conf.urls import handler404, handler500
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.views.generic import RedirectView
from django.urls import include, path
from django.template.defaulttags import register

from university.sitemaps import (StaffSitemap, FacultySitemap, CathedraSitemap)
from news.sitemaps import (PaperSitemap, NewsSitemap)

admin.autodiscover()

handler404 = 'content.views.custom_template_handler404'
handler500 = 'content.views.custom_template_handler500'

sitemaps = {
    "cmspages": CMSSitemap,
    "teacher": StaffSitemap,
    "faculty": FacultySitemap,
    "cathedra": CathedraSitemap,
    "articles": PaperSitemap,
    "news": NewsSitemap
}

urlpatterns = [
    path('favicon.ico/', RedirectView.as_view(
    url='/assets/images/favicon.png'), 
    name='favicon'),
    path('manifest.json/', manifest_view, name='manifest'),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}),
    path("", include("searcher.urls"))
]

urlpatterns += i18n_patterns(

    path('', include('gallery.urls')),

    path('news/',include('news.urls')),
    
    path('university/',include('university.urls')),

    path('content/',include('content.urls')),

    #region				-----Service Imports-----
    path('jet/', include('jet.urls', 'jet')),
    path("admin/", admin.site.urls),
    path("", include("cms.urls")),
    #endregion
  
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# This is only needed when using runserver.
if settings.DEBUG:
    urlpatterns += [path('silk/', include('silk.urls', namespace='silk'))]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
