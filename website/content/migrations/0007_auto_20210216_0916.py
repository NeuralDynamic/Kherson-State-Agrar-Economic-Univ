# Generated by Django 3.0.10 on 2021-02-16 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0006_auto_20210209_2018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='universitysite',
            name='primary',
            field=models.BooleanField(default=False),
        ),
    ]
