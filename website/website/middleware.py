from django.conf import settings
from django.shortcuts import redirect


class LocaleRedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        language_list = [lang[0] for lang in settings.LANGUAGES]

        allowed_paths = ('favicon.ico',
                        'manifest.json',
                        'sitemap.xml',
                        'robots.txt')

        if len(request.path) < 3 or request.path[1:3] not in language_list:
            if not request.path.replace('/','') in allowed_paths:
                return redirect(f'/{request.LANGUAGE_CODE}{request.path}')

        response = self.get_response(request)
        return response