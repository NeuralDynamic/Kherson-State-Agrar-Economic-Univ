# Generated by Django 3.0.10 on 2021-02-23 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0029_auto_20210223_1954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speciality',
            name='number',
            field=models.CharField(default='', max_length=10, verbose_name='Number'),
        ),
        migrations.AlterField(
            model_name='specialitytranslation',
            name='title',
            field=models.CharField(default='', max_length=100, verbose_name='Title'),
        ),
    ]