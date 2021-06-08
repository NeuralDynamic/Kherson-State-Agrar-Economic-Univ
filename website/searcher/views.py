#region				-----External Imports-----
from django.shortcuts import render
#endregion

#region				-----Internal Imports-----
from .services.service import SearchService
#endregion

def search(request):
    phrase=request.GET.get("q")
    result=SearchService().search(phrase, request.LANGUAGE_CODE)
    return render(request,'searcher/search.html',
                context={'search_result':result})