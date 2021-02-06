#region				-----External Imports-----
from .services.service import PaperService
from django.shortcuts import render
from gallery.models import Image
#endregion

#region				-----Internal Imports-----
from .models import Paper
#endregion

#region				   -----News views-----

def news_view(request):
    articles = Paper.objects.all()
    last_articles = articles[:5]
    return render(request,'news/news.html',
                        context={'articles':articles,
                                'last_articles':last_articles})

def paper_view(request, paper_id):
    context = PaperService().get_paper(pk=paper_id)
    return render(request,'news/article.html', context=context)

#endregion
