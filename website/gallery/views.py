#region				-----External Imports-----
from django.shortcuts import render
#endregion

#region				-----Internal Imports-----
from .services.service import GalleryService
from .models import Gallery, Image 
#endregion

#region				   -----Type Hints-----
#endregion


#region				   -----Gallery views-----

def gallery_catalog_view(request):
    context = GalleryService().gallery_catalog()
    return render(request,'gallery/catalog.html', context=context)

def gallery_view(request, gallery_id):
    context = GalleryService().get_gallery(pk=gallery_id)
    return render(request,'gallery/gallery.html', context=context)

#endregion
