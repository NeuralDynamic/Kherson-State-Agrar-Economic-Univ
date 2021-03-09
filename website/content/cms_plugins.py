#region				-----External Imports-----
from content import cms_models

from cms.models.pluginmodel import CMSPlugin
from cms.plugin_base import CMSPluginBase

from django.conf import settings
from django.core.files.images import get_image_dimensions
from django.utils.translation import ugettext as _

from news.models import Paper, Announcement
#endregion

#region				-----Banner plugins-----
class IntroPlugin(CMSPluginBase):
    render_template=settings.TEMPLATE_DIR+"/cms-plugins/home__banner.html"
    module=_("Main page")
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
    module=_("Main page")
    model=cms_models.Cards
    name=_("Cards")

    #region            -----Rendering-----
    def render(self, context, instance, placeholder):
        context.update({"instance": instance})
        return context
    #endregion
#endregion

#region				-----Infos plugins-----
class InfoPlugin(CMSPluginBase):
    render_template=settings.TEMPLATE_DIR+"/cms-plugins/home__info.html"
    module=_("Main page")
    model=cms_models.Info
    name=_("Info")

    #region            -----Rendering-----
    def render(self, context, instance, placeholder):
        context.update({"instance": instance})
        return context
    #endregion
#endregion

#region				-----News plugins-----
class NewsPlugin(CMSPluginBase):
    render_template=settings.TEMPLATE_DIR+"/cms-plugins/home__news.html"
    module=_("Main page")
    model=cms_models.News
    name=_("News")

    #region            -----Rendering-----
    def render(self, context, instance, placeholder):
        articles = Paper.objects\
            .prefetch_related('category')\
            .filter(primary=True).all()
        context.update({"articles": articles})
        return context
    #endregion
#endregion

#region				-----Contact form plugin-----
class ContactFormPlugin(CMSPluginBase):
    render_template=settings.TEMPLATE_DIR+"/cms-plugins/home_contact-form.html"
    module=_("Main page")
    name=_("Contact Form")
#endregion

class AnnouncementsPlugin(CMSPluginBase):
    render_template=settings.TEMPLATE_DIR+"/cms-plugins/home__announcements.html"
    module=_("Main page")
    name=_("Announcements")

    #region            -----Rendering-----
    def render(self, context, instance, placeholder):
        announcements = Announcement.objects.filter(active=True).all()
        context.update({"announcements": announcements})
        return context
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

class InternalLinkPlugin(CMSPluginBase):
    #region           -----Information-----
    render_template=settings.TEMPLATE_DIR+"/cms-plugins/internal-link.html"
    module=_("Utils plugins")
    model=cms_models.InternalLink
    name=_("Internal Link")
    #endregion

    #region            -----Rendering-----
    def render(self, context, instance, placeholder):
        context.update({"instance": instance})
        return context
    #endregion
#endregion

class SectionBlock(CMSPluginBase):
    render_template=settings.TEMPLATE_DIR+"/cms-plugins/section.html"
    module=_("Base blocks")
    model=cms_models.Section
    name=_("Section Block")

    #region            -----Rendering-----
    def render(self, context, instance, placeholder):
        context.update({"instance": instance})
        return context
    #endregion

class SectionHidingPlugin(CMSPluginBase):
    model = cms_models.HidingSection
    module=_("Base blocks")
    name = _("Section Hiding Block")
    render_template = settings.TEMPLATE_DIR+"/cms-plugins/section-hiding.html"

    #region            -----Rendering-----
    def render(self, context, instance, placeholder):
        context.update({"instance": instance})
        return context
    #endregion

class TeacherSliderPlugin(CMSPluginBase):
    model = cms_models.TeacherSlider
    module=_("Base blocks")
    name = _("Teacher Slider")
    render_template = settings.TEMPLATE_DIR+"/cms-plugins/teacher-slider.html"

    #region            -----Rendering-----
    def render(self, context, instance, placeholder):
        context.update({"instance": instance})
        return context
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