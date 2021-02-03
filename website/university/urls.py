#region				-----External Imports-----
from django.urls import path
#endregion

#region				-----Internal Imports-----
from .views import teacher_view
#endregion


urlpatterns = [
    path('/teacher/<int:teacher_id>/', teacher_view),
]