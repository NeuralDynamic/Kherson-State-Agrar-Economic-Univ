#region				-----External Imports-----
from django.shortcuts import render
#endregion

#region				-----Internal Imports-----
from .services.service import SearchService
#endregion

def search(request):
    phrase=request.GET.get("q")
    SearchService().search(phrase)
    return render(request)