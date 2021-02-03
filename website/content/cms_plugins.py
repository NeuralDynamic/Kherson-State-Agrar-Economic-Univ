#region				-----External Imports-----
from content import cms_models

from cms.models.pluginmodel import CMSPlugin
from cms.plugin_base import CMSPluginBase

from django.conf import settings
from django.core.files.images import get_image_dimensions
from django.utils.translation import ugettext as _
#endregion



#region				-----Utils plugins-----
class ExternalLinkPlugin(CMSPluginBase):
    #region           -----Information-----
    render_template=settings.TEMPLATE_DIR+"/cms-plugins/external-link.html"
    module=_("Utils plugins")
    model=cms_models.ExternalLink
    name=_("External Link")
    #endregion

    #region            -----Rendering-----
    def render(self, context, instance, placeholder):
        context.update({"instance": instance})
        return context
    #endregion
#endregion


#region				-----Pages plugins-----

class FooterBlock(CMSPluginBase):
    #region           -----Information-----
    render_template=settings.TEMPLATE_DIR+"/cms-plugins/footer.html"
    module=_("Base blocks")
    model=cms_models.Footer
    name=_("Footer Block")
    #endregion

    #region            -----Rendering-----
    def render(self, context, instance, placeholder):
        context.update({"instance": instance})
        return context
    #endregion

#endregion