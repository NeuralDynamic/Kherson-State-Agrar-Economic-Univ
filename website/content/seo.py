from django.contrib.sites.models import Site
from django.db import models
from django.utils.translation import ugettext_lazy as _
from parler.models import (TranslatableModel, TranslatedFields)


TWITCH_CARDS=(
    (1,'summary'),
    (2,'summary_large_image'),
    (3,'app'),
    (4,'player')
)

class UniversitySite(TranslatableModel,Site):
    #region           -----Translation-----
    translations=TranslatedFields(
        keywords=models.TextField(blank=True),
        description=models.TextField(blank=True),
        author=models.CharField(blank=True,max_length=200),
        og_title=models.CharField(blank=True,max_length=200),
        og_image_alt=models.CharField(blank=True,max_length=200),
        twitter_image_alt=models.CharField(blank=True,max_length=200),
    )
    #endregion

    #region           -----Information-----
    primary=models.BooleanField(default=False)

    og_url=models.URLField(blank=True, null=True)
    og_image=models.ImageField(blank=True, upload_to="seo")

    twitter_image=models.ImageField(blank=True, upload_to="seo")
    twitter_card=models.IntegerField(blank=True, null=True, choices=TWITCH_CARDS)
    twitter_site=models.CharField(blank=True,max_length=200)
    #endregion

    #region            -----Metadata-----
    class Meta(object):
        verbose_name=_("University Site")
    #endregion

    #region         -----Internal Methods-----
    def __str__(self)->str:
        """@return site name"""
        return self.name
    #endregion