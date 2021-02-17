#region				-----External Imports-----
from content import cms_models

from cms.models.pluginmodel import CMSPlugin
from cms.plugin_base import CMSPluginBase

from django.conf import settings
from django.core.files.images import get_image_dimensions
from django.utils.translation import ugettext as _

from news.models import Paper
#endregion

#region				-----Banner plugins-----
class BannerPlugin(CMSPluginBase):
    render_template=settings.TEMPLATE_DIR+"/cms-plugins/home__banner.html"
    module=_("Banner plugins")
    model=cms_models.Banner
    name=_("Banner")

    #region            -----Rendering-----
    def render(self, context, instance, placeholder):
        context.update({"instance": instance})
        return context
    #endregion
#endregion

#region				-----Cards plugins-----
class CardsPlugin(CMSPluginBase):
    render_template=settings.TEMPLATE_DIR+"/cms-plugins/home__cards.html"
    module=_("Cards plugins")
    model=cms_models.Cards
    name=_("Cards")

    #region            -----Rendering-----
    def render(self, context, instance, placeholder):
        context.update({"instance": instance})
        return context
    #endregion
#endregion

#region				-----Infos plugins-----
class Info1Plugin(CMSPluginBase):
    render_template=settings.TEMPLATE_DIR+"/cms-plugins/home__info.html"
    module=_("Info1 plugins")
    model=cms_models.Info1
    name=_("Info1")

    #region            -----Rendering-----
    def render(self, context, instance, placeholder):
        context.update({"instance": instance})
        return context
    #endregion

class Info2Plugin(CMSPluginBase):
    render_template=settings.TEMPLATE_DIR+"/cms-plugins/home__info.html"
    module=_("Info2 plugins")
    model=cms_models.Info2
    name=_("Info2")

    #region            -----Rendering-----
    def render(self, context, instance, placeholder):
        context.update({"instance": instance})
        return context
    #endregion
#endregion

#region				-----News plugins-----
class NewsPlugin(CMSPluginBase):
    render_template=settings.TEMPLATE_DIR+"/cms-plugins/home__news.html"
    module=_("News plugins")
    model=cms_models.News
    name=_("News")

    #region            -----Rendering-----
    def render(self, context, instance, placeholder):
        context.update({"articles": Paper.objects.all()[:5]})
        context.update({"instance": instance})
        return context
    #endregion
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