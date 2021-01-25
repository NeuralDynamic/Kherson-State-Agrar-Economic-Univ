#region             -----External Imports-----
from django.db.models.signals import post_delete
from django.dispatch import receiver
#endregion

#region             -----Internal Imports-----
from .models import (Staff, Faculty, Cathedra)
#endregion

#region               -----Subdivisions-----
@receiver(post_delete, sender=Cathedra)
@receiver(post_delete, sender=Faculty)
def delete_on_delete(instance: object,
**kwargs)->None:
    """
    Deletes related gallery of object\n
    :param instance: object instance\n
    @return None
    """
    instance.emblem.delete(save=False)
    (instance.gallery.delete() if
    instance.gallery else None)
#endregion

#region                  -----Staff-----
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
#endregion