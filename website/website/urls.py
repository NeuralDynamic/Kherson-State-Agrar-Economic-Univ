from content.views import manifest_view
from cms.sitemaps import CMSSitemap
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.views.generic import RedirectView
from django.urls import include, path
from django.template.defaulttags import register

admin.autodiscover()

urlpatterns = [
    path('favicon.ico/', RedirectView.as_view(url='/assets/images/favicon.png'), name='favicon'),

    path('manifest.json/', manifest_view, name='manifest'),

    path("sitemap.xml", sitemap, {"sitemaps": {"cmspages": CMSSitemap}}),
    
    path("", include("searcher.urls"))
]

urlpatterns += i18n_patterns(

    path('', include('gallery.urls')),

    path('news/',include('news.urls')),
    
    path('university/',include('university.urls')),

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
