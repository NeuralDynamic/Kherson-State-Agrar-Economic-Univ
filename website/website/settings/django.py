import os, pathlib, sys

import django.conf.locale
from django.conf import global_settings

gettext = lambda s: s

BASE_DIR = pathlib.Path(__file__).parent.parent.parent



INSTALLED_APPS = [
    'jet',
    # 'djangocms_admin_style',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'django.contrib.messages',
    'cms',
    'menus',
    'sekizai',
    'treebeard',
    'djangocms_text_ckeditor',
    'filer',
    'easy_thumbnails',
    'djangocms_bootstrap4',
    'djangocms_bootstrap4.contrib.bootstrap4_alerts',
    'djangocms_bootstrap4.contrib.bootstrap4_badge',
    'djangocms_bootstrap4.contrib.bootstrap4_card',
    'djangocms_bootstrap4.contrib.bootstrap4_carousel',
    'djangocms_bootstrap4.contrib.bootstrap4_collapse',
    'djangocms_bootstrap4.contrib.bootstrap4_content',
    'djangocms_bootstrap4.contrib.bootstrap4_grid',
    'djangocms_bootstrap4.contrib.bootstrap4_jumbotron',
    'djangocms_bootstrap4.contrib.bootstrap4_link',
    'djangocms_bootstrap4.contrib.bootstrap4_listgroup',
    'djangocms_bootstrap4.contrib.bootstrap4_media',
    'djangocms_bootstrap4.contrib.bootstrap4_picture',
    'djangocms_bootstrap4.contrib.bootstrap4_tabs',
    'djangocms_bootstrap4.contrib.bootstrap4_utilities',
    'djangocms_file',
    'djangocms_icon',
    'djangocms_link',
    'djangocms_picture',
    'djangocms_style',
    'djangocms_googlemap',
    'djangocms_video',
    'djangocms_snippet',
    'website',
    'library',
    'gallery',
    'news',
    'university',
    'compressor',
    'multi_email_field',
    'parler',
    'searcher',
    'content',
]

MIDDLEWARE = [
    'cms.middleware.utils.ApphookReloadMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
    'website.middleware.LocaleRedirectMiddleware',
]

ROOT_URLCONF = 'website.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'),],
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.media',
                'django.template.context_processors.csrf',
                'django.template.context_processors.tz',
                'sekizai.context_processors.sekizai',
                'django.template.context_processors.static',
                'cms.context_processors.cms_settings'
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader'
            ],
        },
    },
]

WSGI_APPLICATION = 'website.wsgi.application'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


LANGUAGE_CODE = 'uk'

TIME_ZONE = 'Europe/Kiev'

USE_I18N = True

USE_L10N = True

USE_TZ = True

EXTRA_LANG_INFO = {
    'uk': {
        'code': 'uk',
        'name': 'Ukrainian',
        'name_local': u'\u0055\u006b\u0072\u0061\u0069\u006e\u0069\u0061\u006e', #unicode codepoints here
    },
}

LANGUAGES = (
    ## Customize this
    ('en', gettext('en')),
)

# Add custom languages not provided by Django
LANG_INFO = dict(django.conf.locale.LANG_INFO, **EXTRA_LANG_INFO)
django.conf.locale.LANG_INFO = LANG_INFO
LANGUAGES = (*LANGUAGES, ('uk', gettext('uk')),)

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

DATE_INPUT_FORMATS = ('%d.%m.%Y','%Y-%m-%d')

STATIC_URL = '/static/'
ADMIN_MEDIA_PREFIX = '/static/admin/'

STATIC_ROOT = os.path.join(BASE_DIR, 'allstaticfiles')

STATICFILE_DIR = os.path.join(BASE_DIR, 'allstaticfiles/static')
STATICFILES_DIRS = (
    STATICFILE_DIR,
    # os.path.join(BASE_DIR, 'static'),
)

MEDIA_FOLDER = 'media'
MEDIA_ROOT = os.path.join(BASE_DIR, MEDIA_FOLDER)
MEDIA_URL = '/assets/'

TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')

CMS_ENABLE_UPDATE_CHECK = True

SITE_ID = 1

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'stream': sys.stdout,
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True,
        },
        "errors_log": {
            "level": "ERROR",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": os.path.join(BASE_DIR, "errors.log"),
            "maxBytes": 1024 * 1024 * 10,
            "backupCount": 7,
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console','mail_admins','errors_log'],
            'level': 'INFO',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['mail_admins','errors_log','console'],
            'level': 'INFO',
            'propagate': False,
        },
    }
}


JET_SIDE_MENU_COMPACT = True
JET_THEMES = [
    {
        'theme': 'default', # theme folder name
        'color': '#47bac1', # color of the theme's button in user menu
        'title': 'Default' # theme title
    },
    {
        'theme': 'green',
        'color': '#44b78b',
        'title': 'Green'
    },
    {
        'theme': 'light-green',
        'color': '#2faa60',
        'title': 'Light Green'
    },
    {
        'theme': 'light-violet',
        'color': '#a464c4',
        'title': 'Light Violet'
    },
    {
        'theme': 'light-blue',
        'color': '#5EADDE',
        'title': 'Light Blue'
    },
    {
        'theme': 'light-gray',
        'color': '#222',
        'title': 'Light Gray'
    }
]