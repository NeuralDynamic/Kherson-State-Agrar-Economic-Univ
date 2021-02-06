#region				-----External Imports-----
from django.urls import path
#endregion

#region				-----Internal Imports-----
from .views import news_view
from .views import paper_view
#endregion

urlpatterns = [
    path('', news_view, name="news"),
    path('article/<int:paper_id>', paper_view, name="article")
]