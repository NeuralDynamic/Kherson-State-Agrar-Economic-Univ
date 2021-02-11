#region				-----External Imports-----
from django.shortcuts import render
from typing import (TypeVar, Dict)
#endregion

#region				-----Internal Imports-----
from .services.service import GalleryService
from .models import Gallery, Image 
#endregion

#region				   -----Type Hints-----
Html=TypeVar("Html", str, bytes)
#endregion

#region				 -----Gallery views-----
def gallery_view(request: Dict, gallery_id: int)->Html:
    """
    Renders gallery template page using gallery id\n
    :param gallery_id: id of gallery\n
    :param request: Http request\n
    @return built template
    """
    context=GalleryService().get_gallery(pk=gallery_id)
    return render(request=request, context=context,
    template_name='gallery/gallery.html')

def gallery_catalog_view(request: Dict)->Html:
    """
    Renders gallery catalog template page\n
    :param request: Http request\n
    @return built template
    """
    current_page=request.GET.get('page', 1)
    context=GalleryService().paginator(current_page)
    return render(request=request, context=context,
    template_name='gallery/catalog.html')
#endregion
