#region				-----External Imports-----
from django.core.paginator import Paginator, EmptyPage
from django.http import Http404
#endregion

#region				-----Internal Imports-----
from ..models import Gallery, Image
#endregion


class GalleryService(object):
    def paginator(self, page_num: int)->object:
        try:
            context = dict()

            galleries=Gallery.objects.all()
            
            paginator = Paginator(galleries, 9)

            try:
                page = paginator.page(page_num)
            except EmptyPage:
                page = paginator.page(1)

            context['galleries'] = page

            return context
        except Gallery.DoesNotExist:
            raise Http404
    
    def get_gallery(self, pk: int)->object:
        try:
            context = dict()

            gallery=Gallery.objects.prefetch_related('images').get(pk=pk)

            context['gallery'] = gallery

            try:
                images=gallery.images.all()
                context['images'] = images
            except Exception:
                pass
            return context
        except Gallery.DoesNotExist:
            raise Http404