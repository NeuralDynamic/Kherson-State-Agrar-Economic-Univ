# Generated by Django 3.0.10 on 2021-02-26 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_announcement_announcementtranslation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='image',
            field=models.ImageField(blank=True, upload_to='announcements', verbose_name='Image'),
        ),
    ]