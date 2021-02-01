#region             -----External Imports-----
from django.db.models.signals import (post_delete, pre_save)
from django.dispatch import receiver
#endregion

#region             -----Internal Imports-----
from .models import Paper
#endregion

@receiver(pre_save, sender=Paper)
def delete_on_change(instance: Paper,
**kwargs)->None:
    """
    Deletes an old version file when 
    the header was updated by admin\n
    :param instance: paper instance\n
    @return None
    """
    try: old_paper=sender.objects.get(pk=instance.pk)
    except: return "No such object in database"
    if old_paper.header!=instance.header:
        old_paper.header.delete(save=False)

@receiver(post_delete, sender=Paper)
def delete_on_delete(instance: Paper,
**kwargs)->None:
    """
    Deletes related gallery of paper\n
    :param instance: paper instance\n
    @return None
    """
    instance.header.delete(save=False)
    (instance.gallery.delete() if
    instance.gallery else None)