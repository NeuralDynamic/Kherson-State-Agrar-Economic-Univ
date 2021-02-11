#region				-----External Imports-----
from django.urls import path
#endregion

#region				-----Internal Imports-----
from .views import gallery_catalog_view
from .views import gallery_view
#endregion

urlpatterns = [
    path('gallery/<int:gallery_id>/', gallery_view, name="gallery"),
    path('galleries/', gallery_catalog_view, name="galleries"),
]