from django.conf import settings
from django.shortcuts import redirect


class LocaleRedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith(f'/{settings.LANGUAGE_CODE}'):
            return redirect( request.path[3:])
        response = self.get_response(request)
        return response