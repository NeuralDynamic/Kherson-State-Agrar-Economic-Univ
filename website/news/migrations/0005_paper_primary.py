# Generated by Django 3.0.10 on 2021-02-24 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20210215_1458'),
    ]

    operations = [
        migrations.AddField(
            model_name='paper',
            name='primary',
            field=models.BooleanField(default=False, verbose_name='Primary article'),
        ),
    ]
