from .cms import CMS_LANGUAGES

PARLER_DEFAULT_LANGUAGE_CODE = "ua"

# Used django cms languages
PARLER_LANGUAGES = {
    1: tuple({"code": i["code"]} for i in CMS_LANGUAGES[1]),
    None: tuple({"code": i["code"]} for i in CMS_LANGUAGES[1]),
    'default': CMS_LANGUAGES.get('default'),
}