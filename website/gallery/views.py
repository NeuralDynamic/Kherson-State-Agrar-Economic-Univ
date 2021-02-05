#region				-----External Imports-----
from django.shortcuts import render
#endregion

#region				-----Internal Imports-----
from .models import Gallery, Image 
#endregion

#region				   -----Type Hints-----
#endregion


#region				   -----Gallery views-----

def gallery_catalog_view(request):
    galleries = Gallery.objects.all()
    return render(request,'gallery/catalog.html',
                        context={'galleries':galleries})

def gallery_view(request, gallery_id):
    gallery = Gallery.objects.get(pk=gallery_id)
    images = Image.objects.filter(gallery_id=gallery_id).all()
    return render(request,'gallery/gallery.html',
                        context={'gallery':gallery,
                                'images':images})

#endregion
