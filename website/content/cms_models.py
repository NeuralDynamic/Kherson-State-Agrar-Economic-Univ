#region				-----External Imports-----
from cms.models.pluginmodel import CMSPlugin

from django.db import models
from django.utils.translation import ugettext_lazy as _
#endregion

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

    phone1 = models.CharField(max_length=100, blank=True, null=True, 
                        default='', verbose_name=_('Phone'))
    phone2 = models.CharField(max_length=100, blank=True, null=True, 
                        default='', verbose_name=_('Phone'))
    email1 = models.CharField(max_length=100, blank=True, null=True, 
                        default='', verbose_name=_('Email'))
    email2 = models.CharField(max_length=100, blank=True, null=True, 
                        default='', verbose_name=_('Email'))
    # endregion



#endregion