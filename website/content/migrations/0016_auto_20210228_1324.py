# Generated by Django 3.0.10 on 2021-02-28 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0015_auto_20210227_2255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hidingsection',
            name='title',
            field=models.CharField(max_length=300, verbose_name='Section title'),
        ),
    ]
