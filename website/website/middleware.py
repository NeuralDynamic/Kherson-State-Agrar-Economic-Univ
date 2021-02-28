from django.conf import settings
from django.shortcuts import redirect


class LocaleRedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        language_list = [lang[0] for lang in settings.LANGUAGES]

        if len(request.path) < 3 or request.path[1:3] not in language_list:
            return redirect(f'/{request.LANGUAGE_CODE}{request.path}')

        response = self.get_response(request)
        return response