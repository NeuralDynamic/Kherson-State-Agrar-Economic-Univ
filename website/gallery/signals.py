#region             -----External Imports-----
from django.db.models.signals import (post_delete, pre_save)
from django.dispatch import receiver
#endregion

#region             -----Internal Imports-----
from .models import Image
#endregion

@receiver(pre_save, sender=Image)
def delete_on_change(instance: Image,
**kwargs)->None:
    """
    Deletes an old version file when 
    the image was updated by admin\n
    :param instance: image instance\n
    @return None
    """
    try: gallery=Image.objects.get(pk=instance.pk)
    except: return "No such object in database"
    if gallery.image!=instance.image:
        gallery.image.delete(save=False)

@receiver(post_delete, sender=Image)
def delete_on_delete(instance: Image,
**kwargs)->None:
    """
    Deletes file reference when the image
    was removed from database by admin\n
    :param instance: image instance\n
    @return None
    """
    instance.image.delete(save=False)