#region				-----External Imports-----
from cms.models.pluginmodel import CMSPlugin

from django.db import models
from django.utils.translation import ugettext_lazy as _
from djangocms_text_ckeditor.fields import HTMLField

from university.models.utils import StaffCathedra
#endregion

#region				-----Banner plugins-----
class Banner(CMSPlugin):
    #region           -----Information-----
    subheader=models.CharField(max_length=400, blank=True,
    null=True, verbose_name=_('Subheader'))

    intro_image=models.ImageField(upload_to="cms", blank=True,
    null=True, verbose_name=_("Banner image"))
    #endregion
#endregion

#region				-----Cards plugins-----
class Cards(CMSPlugin):
    #region           -----Information-----
    left_card_image=models.FileField(upload_to="cms", 
    verbose_name=_("Left card image"))
    left_card_title=models.CharField(max_length=100, blank=True,
    null=True, verbose_name=_('Left card title'))
    left_card_text=models.TextField(max_length=400,
    blank=True, null=True, verbose_name=_("Left card text"))
    left_card_url=models.URLField(blank=True, null=True,
    verbose_name=_("Left card url"))

    middle_card_image=models.FileField(upload_to="cms", 
    verbose_name=_("Middle card image"))
    middle_card_title=models.CharField(max_length=100, blank=True,
    null=True, verbose_name=_('Middle card title'))
    middle_card_text=models.TextField(max_length=400,
    blank=True, null=True, verbose_name=_("Middle card text"))
    middle_card_url=models.URLField(blank=True, null=True,
    verbose_name=_("Middle card url"))

    right_card_image=models.FileField(upload_to="cms", 
    verbose_name=_("Right card image"))
    right_card_title=models.CharField(max_length=100, blank=True,
    null=True, verbose_name=_('Right card title'))
    right_card_text=models.TextField(max_length=400,
    blank=True, null=True, verbose_name=_("Right card text"))
    right_card_url=models.URLField(blank=True, null=True,
    verbose_name=_("Right card url"))
    #endregion
#endregion

#region				-----Infos plugins-----
class Info(CMSPlugin):
    #region           -----Information-----
    title=models.CharField(max_length=100, blank=True,
    null=True, verbose_name=_("Title"))

    description=models.TextField(max_length=500, blank=True,
    null=True, verbose_name=_("Description"))

    button_title=models.CharField(max_length=100,
    blank=True, null=True, verbose_name=_("Button title"))

    button_url=models.URLField(blank=True, null=True,
    verbose_name=_("Button url"))
    #endregion
#endregion

#region				-----News plugins-----
class News(CMSPlugin):
    #region           -----Information-----
    title=models.CharField(max_length=100, blank=True,
    null=True, verbose_name=_("Title"))
    #endregion
#endregion

class Section(CMSPlugin):
    content=HTMLField(verbose_name=_("Content"))


class HidingSection(CMSPlugin):
    title=models.CharField(max_length=150, verbose_name=_("Section title"))
    content=HTMLField(verbose_name=_("Content"))

class TeacherSlider(CMSPlugin):
    title=models.CharField(max_length=150, verbose_name=_("Section title"))
    staff=models.ManyToManyField(StaffCathedra,
        verbose_name=_("Staff"), 
        help_text=_('You can choose staff from cathedra staff'))

    def copy_relations(self, oldinstance):
        self.staff = oldinstance.staff.all()

#region				-----Utils plugins-----
class ExternalLink(CMSPlugin):
    #region           -----Information-----
    title = models.CharField(max_length=100, blank=True, null=True, 
                        verbose_name=_('Link title'))
    link = models.URLField(blank=True, null=True, 
                        verbose_name=_('Link'))
    # endregion

#endregion

#region				-----Pages plugins-----
class Footer(CMSPlugin):    
    #region           -----Information-----
    location_link = models.URLField(blank=True, null=True, 
                        default='https://goo.gl/maps/gfMW9BYgLwjTVcSk7',
                        verbose_name=_('Location link'))
    location_country = models.CharField(max_length=100, blank=True, null=True, 
                        default='Україна', verbose_name=_('Location country'))
    location_city = models.CharField(max_length=100, blank=True, null=True, 
                        default='м. Херсон', verbose_name=_('Location city'))
    location_street = models.CharField(max_length=100, blank=True, null=True, 
                        default='вул. Стрітенська, 23', 
                        verbose_name=_('Location street'))
    location_zip = models.CharField(max_length=100, blank=True, null=True, 
                        default='73006', verbose_name=_('Location zip'))

    facebook_link = models.URLField(blank=True, null=True, 
                        verbose_name=_('Facebook link'))
    instagram_link = models.URLField(blank=True, null=True, 
                        verbose_name=_('Instagram link'))
    youtube_link = models.URLField(blank=True, null=True, 
                        verbose_name=_('Youtube link'))
    telegram_link = models.URLField(blank=True, null=True, 
                        verbose_name=_('Telegram link'))
    linkedin_link = models.URLField(blank=True, null=True, 
                        verbose_name=_('Linkedin link'))
    tiktok_link = models.URLField(blank=True, null=True, 
                        verbose_name=_('Tiktok link'))

    phone = models.CharField(max_length=100, blank=True, null=True, 
                        default='', verbose_name=_('Phone'))
    email = models.CharField(max_length=100, blank=True, null=True, 
                        default='', verbose_name=_('Email'))
    # endregion
#endregion