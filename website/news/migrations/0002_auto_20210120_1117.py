# Generated by Django 3.1.5 on 2021-01-20 09:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paper',
            name='gallery',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='gallery.gallery'),
        ),
    ]
