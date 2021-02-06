#region             -----External Imports-----
from django.conf import settings
from django.core.files import File
from django.db.models.signals import (post_delete, 
pre_save, post_save)
from django.dispatch import receiver

from .models import Image as ImageModel
from os import remove
from PIL import Image as Editor
#endregion

#region             -----Internal Imports-----
from .settings import (SIZES, FORMAT)
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
    filename=image.filename
    name=filename.split("/")[-1].split(".")[0]
    image=image.convert("RGB")

    #*Generates pathes the images save to
    images_folder = f"{settings.MEDIA_ROOT}/{ImageModel.large_image.field.upload_to}"
    files_pathes=[
            f"{images_folder}/{name}_{size}.{FORMAT.lower()}" 
            for size in SIZES]
    model_pathes=[
            f"{ImageModel.large_image.field.upload_to}/{name}_{size}.{FORMAT.lower()}" 
            for size in SIZES]

    #*Associates images with model fields
    parameters={f"{size}_image": path
    for path, size in zip(model_pathes, SIZES)}

    #*Generates images with sizes
    for path, size in zip(files_pathes, SIZES):
        f_width, f_height = SIZES[size]
        width, height = image.size
        # if photo in portrait orientation
        if height > width:
            f_width, f_height = f_height, f_width
        f_height = int(height * f_width/width)
        f_size = (f_width, f_height)
        image.resize(size=f_size).save(path,"webp",
                    optimize=True, quality=85)
    
    #*Updates model parameters
    (Image.objects.filter(pk=instance.pk)
    .update(**parameters))

    #*Removes temporary image
    remove(filename)