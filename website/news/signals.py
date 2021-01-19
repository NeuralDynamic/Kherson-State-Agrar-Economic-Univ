#region             -----External Imports-----
from django.db.models.signals import post_delete
from django.dispatch import receiver
#endregion

#region             -----Internal Imports-----
from .models import Paper
#endregion

@receiver(post_delete, sender=Paper)
def delete_on_delete(instance: Paper,
**kwargs)->None:
    """
    Deletes related gallery of paper\n
    :param instance: paper instance\n
    @return None
    """
    instance.gallery.delete()