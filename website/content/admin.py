#region				-----External Imports-----
from cms.plugin_pool import plugin_pool
from django.contrib.admin import register
from django.contrib import admin
from parler.admin import TranslatableAdmin
#endregion

#region				-----Internal Imports-----
from .cms_plugins import ExternalLinkPlugin
from .cms_plugins import FooterBlock
from .seo import UniversitySite
#endregion

plugin_pool.register_plugin(ExternalLinkPlugin)
plugin_pool.register_plugin(FooterBlock)


@register(UniversitySite)
class UniversitySiteAdmin(TranslatableAdmin):
    #region           ----Configuration-----
    list_display=["name"]
    fields=["name","primary","description","keywords","author",
            "og_url","og_title","og_image","og_image_alt",
            "twitter_image","twitter_image_alt","twitter_card","twitter_site"]
    #endregion