# Generated by Django 3.1.5 on 2021-01-25 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_auto_20210120_1403'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='library',
        ),
        migrations.AddField(
            model_name='book',
            name='library',
            field=models.ManyToManyField(default=1, to='library.Library'),
        ),
    ]