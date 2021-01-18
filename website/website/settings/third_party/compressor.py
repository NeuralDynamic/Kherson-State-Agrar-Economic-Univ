STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #other
    'compressor.finders.CompressorFinder',
)
COMPRESS_ENABLED = True
COMPRESS_OFFLINE = True
COMPRESS_CSS_FILTERS = [
    #creates absolute urls from relative ones
    'compressor.filters.css_default.CssAbsoluteFilter',
    #css minimizer
    'compressor.filters.cssmin.CSSMinFilter'
]
COMPRESS_JS_FILTERS = [
    'compressor.filters.jsmin.JSMinFilter'
]