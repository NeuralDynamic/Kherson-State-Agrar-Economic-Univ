#region				-----External Imports-----
from django.core.paginator import Paginator, EmptyPage
from django.http import Http404
#endregion

#region				-----Internal Imports-----
from ..models import Paper, NewsFeed
#endregion

class PaperService(object):
    def paginator(self, page_num: int)-> object:
        try:

            articles = Paper.objects.all()
            last_articles = articles.filter(primary=True).all()

            paginator = Paginator(articles, 9)

            try:
                page = paginator.page(page_num)
            except EmptyPage:
                page = paginator.page(1)
            return {
                "articles": page,
                "last_articles": last_articles
            }
        except Paper.DoesNotExist:
            raise Http404

    def get_paper(self, pk: int)->object:
        try:
            context = dict()

            paper = (Paper.objects
            .prefetch_related("gallery__images")
            .get(pk=pk))

            context['paper']=paper

            try:
                gallery=paper.gallery.images.all()
                context['gallery'] = gallery
            except Exception:
                pass
            return context
        except Paper.DoesNotExist:
            raise Http404