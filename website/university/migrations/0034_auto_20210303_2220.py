# Generated by Django 3.0.10 on 2021-03-03 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0033_auto_20210228_1941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='disciplines',
            field=models.ManyToManyField(blank=True, to='university.Discipline'),
        ),
    ]
