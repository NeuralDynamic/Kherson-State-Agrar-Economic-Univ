#region				-----External Imports-----
from django.shortcuts import render
from gallery.models import Image
#endregion

#region				-----Internal Imports-----
from .models import NewsFeed, Paper
#endregion

#region				   -----Type Hints-----
#endregion

#region				   -----News views-----

def news_view(request):
    articles = Paper.objects.all()
    last_articles = articles[:5]
    return render(request,'news/news.html',
                        context={'articles':articles,
                                'last_articles':last_articles})

def paper_view(request, paper_id):
    paper = Paper.objects.get(pk=paper_id)
    images = Image.objects.filter(gallery_id=paper.gallery_id).all()
    return render(request,'news/article.html',
                        context={'paper':paper,
                                'images':images})

#endregion
