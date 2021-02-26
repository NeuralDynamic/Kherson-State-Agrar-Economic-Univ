#region				-----External Imports-----
from django.urls import path
#endregion

#region				-----Internal Imports-----
from .views import contact_form_request
#endregion

urlpatterns = [
    path('request', contact_form_request, name="contact_form_request"),
]