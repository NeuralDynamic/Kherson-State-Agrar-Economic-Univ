#region				-----External Imports-----
from django.shortcuts import render
from gallery.models import Image
from typing import (TypeVar, Dict)
#endregion

#region				-----Internal Imports-----
from .services.service import PaperService
from .models import Paper
#endregion

#region				   -----Type Hints-----
Html=TypeVar("Html", str, bytes)
#endregion

#region				   -----News views-----
def paper_view(request: Dict, paper_id: int)->Html:
    """
    Renders paper template page using paper id\n
    :param paper_id: id of paper\n
    :param request: Http request\n
    @return built template
    """
    context = PaperService().get_paper(pk=paper_id)
    return render(request=request, context=context,
    template_name='news/article.html')

def news_view(request: Dict)->Html:
    """
    Renders news catalog template page\n
    :param request: Http request\n
    @return built template
    """
    current_page=request.GET.get('page', 1)
    context = PaperService().paginator(current_page)
    return render(request=request, context=context,
    template_name='news/news.html')
#endregion
