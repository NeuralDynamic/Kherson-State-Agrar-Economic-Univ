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
    page_num=request.GET.get('page', 1)
    context = PaperService().paginator(page_num)
    return render(request,'news/news.html', context=context)

def paper_view(request, paper_id):
    context = PaperService().get_paper(pk=paper_id)
    return render(request,'news/article.html', context=context)

#endregion
