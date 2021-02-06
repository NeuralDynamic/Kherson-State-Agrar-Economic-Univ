#region				-----External Imports-----
from django.http import Http404
#endregion

#region				-----Internal Imports-----
from ..models import Paper, NewsFeed
#endregion

class PaperService(object):
    def get_paper(self, pk: int)->object:
        try:
            context = dict()

            paper = Paper.objects.prefetch_related("gallery__images").get(pk=pk)

            context['paper']=paper

            try:
                gallery=paper.gallery.images.all()
                context['gallery'] = gallery
            except Exception:
                pass
            return context
        except Paper.DoesNotExist:
            raise Http404
