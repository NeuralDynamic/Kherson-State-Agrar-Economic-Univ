#region				-----External Imports-----
from cms.plugin_pool import plugin_pool
from django.contrib.admin import register
from django.contrib import admin
from parler.admin import TranslatableAdmin
#endregion

#region				-----Internal Imports-----
from .cms_plugins import ExternalLinkPlugin
from .cms_plugins import FooterBlock
from .cms_plugins import IntroPlugin
from .cms_plugins import CardsPlugin
from .cms_plugins import InfoPlugin
from .cms_plugins import NewsPlugin
from .cms_plugins import ContactFormPlugin
from .cms_plugins import AnnouncementsPlugin
from .seo import UniversitySite
#endregion

plugin_pool.register_plugin(ExternalLinkPlugin)
plugin_pool.register_plugin(FooterBlock)
plugin_pool.register_plugin(IntroPlugin)
plugin_pool.register_plugin(CardsPlugin)
plugin_pool.register_plugin(InfoPlugin)
plugin_pool.register_plugin(NewsPlugin)
plugin_pool.register_plugin(ContactFormPlugin)
plugin_pool.register_plugin(AnnouncementsPlugin)


@register(UniversitySite)
class UniversitySiteAdmin(TranslatableAdmin):
    #region           ----Configuration-----
    list_display=["name"]
    fields=["name","primary","description","keywords","author",
            "og_url","og_title","og_image","og_image_alt",
            "twitter_image","twitter_image_alt","twitter_card","twitter_site"]
    #endregion