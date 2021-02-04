#region             -----External Imports-----
from django.db.models.signals import (post_delete, pre_save)
from django.dispatch import receiver

from university.models import Cathedra, Faculty, MaterialBaseNode
#endregion


@receiver(pre_save, sender=Cathedra)
@receiver(pre_save, sender=Faculty)
def delete_on_change_emblem(instance: object,
**kwargs)->None:
    """
    Deletes an old version file when 
    the emblem was updated by admin\n
    :param instance: object instance\n
    @return None
    """
    try: old_object=sender.objects.get(pk=instance.pk)
    except: return "No such object in database"
    if old_object.emblem!=instance.emblem:
        old_object.emblem.delete(save=False)

@receiver(post_delete, sender=Cathedra)
@receiver(post_delete, sender=Faculty)
def delete_emblems(instance: object,
**kwargs)->None:
    """
    Deletes related gallery of object\n
    :param instance: object instance\n
    @return None
    """
    instance.emblem.delete(save=False)
    (instance.gallery.delete() if
    instance.gallery else None)

@receiver(pre_save, sender=MaterialBaseNode)
def local_title_fill_on_save(instance: object,
**kwargs)->None:
    """
    Fill local title of MaterialBaseNode if won't fill by user
    @return None
    """
    if not instance.local_title:
        instance.local_title = instance.title