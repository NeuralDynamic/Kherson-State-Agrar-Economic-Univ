#region				-----External Imports-----
from datetime import date
from djangocms_text_ckeditor.fields import HTMLField
from django.db.models import (Model, URLField, OneToOneField,
CASCADE, CharField, ForeignKey, SET_NULL, ImageField, 
TextField, DateField, ManyToManyField, IntegerField)
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.urls import reverse
from library.models import Book
from parler.models import (TranslatableModel, TranslatedFields)
from typing import (TypeVar, List)
from multi_email_field.fields import MultiEmailField
#endregion

#region				-----Internal Imports-----
from .university import Discipline
#endregion


class Reward(TranslatableModel):
    YEAR_CHOICES = [(r,r) for r in reversed(
    range(1950, date.today().year+1))]

    #region           -----Translation-----
    translations=TranslatedFields(
    title=CharField(max_length=300, blank=False,
    verbose_name=_("Title")))
    #endregion

    #region           -----Information-----
    year=IntegerField(verbose_name=_("Year"), 
    choices=YEAR_CHOICES, null=True)
    #endregion

    #region            -----Metadata-----
    class Meta(object):
        verbose_name_plural=_("Rewards")
        verbose_name=_("Reward")
    #endregion

    #region         -----Internal Methods-----
    def __str__(self)->str:
        """@return title of reqard"""
        return self.title
    #endregion

class Staff(TranslatableModel):
    #region           -----Translation-----
    translations=TranslatedFields(
    second_name=CharField(max_length=40, blank=False,
    verbose_name=_("Second name")),
    
    first_name=CharField(max_length=40, blank=False,
    verbose_name=_("First name")),

    third_name=CharField(max_length=40, blank=False,
    verbose_name=_("Third name")),
    
    rank=CharField(max_length=300, blank=True,
    verbose_name=_("Rank")),

    methodical_works=HTMLField(blank=True,
    verbose_name=_("Methodical works")),

    description=HTMLField(blank=True,
    verbose_name=_("Description")),
    
    ndr_theme=TextField(blank=True,
    verbose_name=_("Topics of research work")))
    #endregion

    #region           -----Information-----
    google_scholar=URLField(blank=True,
    verbose_name=_("Google Scholar"), null=True)
    web_of_science=URLField(blank=True,
    verbose_name=_("Web Of Science"), null=True)
    researchgate=URLField(blank=True,
    verbose_name=_("Researchgate"), null=True)
    scopus=URLField(verbose_name=_("Scopus"),
    blank=True, null=True)
    orcid=URLField(verbose_name=_("ORCID"),
    blank=True, null=True)
    photo=ImageField(verbose_name=_("Photo"),
    upload_to="photos", blank=False)
    phone=CharField(max_length=20, blank=True, null=True,
    verbose_name=_("Phone number"))
    emails=MultiEmailField(blank=True)
    #endregion

    #region            -----Relation-----
    disciplines=ManyToManyField(Discipline, blank=True, null=True)
    books=ManyToManyField(Book, blank=True)
    rewards=ManyToManyField("Reward", blank=True,
                        verbose_name=_("Rewards"),
                        related_name="staff_rewards")
    #endregion

    #region            -----Metadata-----
    class Meta(object):
        verbose_name_plural=_("Staff")
        verbose_name=_("Staff")
    #endregion

    #region         -----Internal Methods-----
    def get_absolute_url(self)->str:
        """@return link to model"""
        return reverse('teacher', kwargs={'teacher_id':self.pk})

    def searching_fields(self)->List[str]:
        """@return translated fields"""
        return ["translations__first_name",
        "translations__methodical_works",
        "translations__second_name",
        "translations__description",
        "translations__third_name"]

    def __str__(self)->str:
        """@return staff information"""
        return (self.second_name+
        " "+self.first_name+
        " "+self.third_name)
    #endregion