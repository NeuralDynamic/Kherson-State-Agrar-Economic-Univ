#region				-----External Imports-----
from django.urls import path
#endregion

#region				-----Internal Imports-----
from .views import faculty_view
from .views import teacher_view
#endregionsudo nginx -t


urlpatterns = [
    path('faculty/<int:faculty_id>/', faculty_view, name="faculty"),

    path('teacher/<int:teacher_id>/', teacher_view, name="teacher"),
]