#region             -----External Imports-----
from django.db.models.signals import (post_delete, 
pre_save, post_save)
from django.dispatch import receiver
from os import remove
from PIL import Image as Editor
#endregion

#region             -----Internal Imports-----
from .settings import SIZES, EXTENSION
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
    try: old_image=Image.objects.get(pk=instance.pk)
    except: return "No such such object in database"
    if old_image.large_image!=instance.large_image:
        for image in old_image.related():
            image.delete(save=False)

@receiver(post_delete, sender=Image)
def delete_on_delete(instance: Image,
**kwargs)->None:
    """
    Deletes file reference when the image
    was removed from database by admin\n
    :param instance: image instance\n
    @return None
    """
    for image in instance.related():
        image.delete(save=False)

@receiver(post_save, sender=Image)
def create_on_save(instance: Image,
**kwargs)->None:
    """
    Creates and compresses images for
    a better rendering performance\n
    :param instance: image instance\n
    @return None
    """
    image=Editor.open(instance.large_image.path)
    name=image.filename.split("/")[-1].split(".")[0]

    pathes=[f"{name}_{size}.{EXTENSION.lower()}" 
    for size in SIZES]

    parameters={f"{size}_image": path 
    for path, size in zip(pathes, SIZES)}

    for path, size in zip(pathes, SIZES):
        image.resize(size=SIZES[size]).save(
        optimize=True, quality=75, fp=path)
    
    Image.objects.filter(pk=instance.pk).update(**parameters)

    remove(image.filename)