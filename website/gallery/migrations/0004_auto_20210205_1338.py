# Generated by Django 3.0.10 on 2021-02-05 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_auto_20210205_1223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='medium_image',
            field=models.ImageField(blank=True, default='', max_length=400, upload_to='gallery'),
        ),
        migrations.AlterField(
            model_name='image',
            name='small_image',
            field=models.ImageField(blank=True, default='', max_length=400, upload_to='gallery'),
        ),
    ]
