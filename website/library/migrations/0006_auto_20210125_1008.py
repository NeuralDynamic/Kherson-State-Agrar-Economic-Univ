# Generated by Django 3.1.5 on 2021-01-25 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_auto_20210125_1008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='library',
            field=models.ManyToManyField(to='library.Library'),
        ),
    ]