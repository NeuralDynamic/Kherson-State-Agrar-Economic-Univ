#region				-----External Imports-----
from cms.plugin_pool import plugin_pool
from django.contrib import admin
#endregion

#region				-----Internal Imports-----
from .cms_plugins import ExternalLinkPlugin
from .cms_plugins import FooterBlock
#endregion

plugin_pool.register_plugin(ExternalLinkPlugin)
plugin_pool.register_plugin(FooterBlock)