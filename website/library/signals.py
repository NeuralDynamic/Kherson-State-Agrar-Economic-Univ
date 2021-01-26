#region             -----External Imports-----
from django.db.models.signals import (post_delete, pre_save)
from django.dispatch import receiver
#endregion

#region             -----Internal Imports-----
from .models import Book
#endregion

@receiver(pre_save, sender=Book)
def delete_on_change(instance: Book,
**kwargs)->None:
    """
    Deletes an old version file when 
    the cover was updated by admin\n
    :param instance: cover instance\n
    @return None
    """
    try: old_book=Book.objects.get(pk=instance.pk)
    except: return "No such object in database"
    if old_book.cover!=instance.cover:
        old_book.cover.delete(save=False)

@receiver(post_delete, sender=Book)
def delete_on_delete(instance: Book,
**kwargs)->None:
    """
    Deletes related cover of book\n
    :param instance: book instance\n
    @return None
    """
    instance.cover.delete(save=False)