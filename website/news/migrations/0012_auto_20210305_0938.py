# Generated by Django 3.0.10 on 2021-03-05 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0011_announcement_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='papertranslation',
            name='authors',
            field=models.CharField(max_length=300, verbose_name='Authors'),
        ),
        migrations.AlterField(
            model_name='papertranslation',
            name='title',
            field=models.CharField(max_length=300, verbose_name='Title'),
        ),
    ]