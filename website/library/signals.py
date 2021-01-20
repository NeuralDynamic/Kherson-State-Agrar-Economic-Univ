#region             -----External Imports-----
from django.db.models.signals import post_delete
from django.dispatch import receiver
#endregion

#region             -----Internal Imports-----
from .models import Book
#endregion

@receiver(post_delete, sender=Book)
def delete_on_delete(instance: Book,
**kwargs)->None:
    """
    Deletes related cover of book\n
    :param instance: book instance\n
    @return None
    """
    instance.cover.delete(save=False)