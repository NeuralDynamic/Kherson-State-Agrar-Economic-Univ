from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone


class ContactRequest(models.Model):
    name = models.CharField(verbose_name=_("Ім'я"), 
        max_length=200, blank=False)
    email = models.CharField(verbose_name=_("Email"), 
        max_length=200, blank=False)
    message = models.TextField(verbose_name=_("Питання"), blank=False)

    created_at=models.DateField(verbose_name=_("Дата"),
    default=timezone.now)

    class Meta:
        verbose_name_plural=_("Запити на контакт")
        verbose_name=_("Запит на контакт")