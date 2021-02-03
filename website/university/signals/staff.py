#region             -----External Imports-----
from django.db.models.signals import (post_delete, pre_save)
from django.dispatch import receiver

from university.models import Staff
#endregion


@receiver(post_delete, sender=Staff)
def delete_on_change_photo(instance: object,
**kwargs)->None:
    """
    Deletes an old version file when 
    the photo was updated by admin\n
    :param instance: object instance\n
    @return None
    """
    try: old_staff=sender.objects.get(pk=instance.pk)
    except: return "No such object in database"
    if old_staff.photo!=instance.photo:
        old_staff.photo.delete(save=False)

@receiver(post_delete, sender=Staff)
def delete_on_delete(instance: Staff,
**kwargs)->None:
    """
    Deletes related library of staff\n
    :param instance: staff instance\n
    @return None
    """
    instance.photo.delete(save=False)
    (instance.library.delete() if
    instance.library else None)