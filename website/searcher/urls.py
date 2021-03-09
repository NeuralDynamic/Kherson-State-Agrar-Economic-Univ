#region             -----External Imports-----
from django.urls import path
#endregion

#region             -----Internal Imports-----
from . import views
#endregion

urlpatterns = [
    path("search", view=views.search, name="search")
]