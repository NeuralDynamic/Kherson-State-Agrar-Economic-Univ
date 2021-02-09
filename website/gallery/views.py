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
    page_num=request.GET.get('page', 1)
    context = GalleryService().paginator(page_num)
    return render(request,'gallery/catalog.html', context=context)

def gallery_view(request, gallery_id):
    context = GalleryService().get_gallery(pk=gallery_id)
    return render(request,'gallery/gallery.html', context=context)

#endregion
