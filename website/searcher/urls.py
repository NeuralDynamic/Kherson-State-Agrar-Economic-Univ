#region             -----External Imports-----
from django.urls import path
#endregion

#region             -----Internal Imports-----
from . import views
#endregion

urlpatterns = [
    path(route="search/<str:phrase>", view=views.search)
]