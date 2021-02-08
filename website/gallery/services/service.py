from ..models import Gallery, Image
from django.http import Http404

class GalleryService(object):
    def gallery_catalog(self)->object:
        try:
            context = dict()

            galleries=Gallery.objects.all()

            context['galleries'] = galleries

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