# Generated by Django 3.0.10 on 2021-02-23 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0028_auto_20210222_1418'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='specialitytranslation',
            name='educational_level',
        ),
        migrations.AddField(
            model_name='speciality',
            name='educational_level',
            field=models.IntegerField(choices=[(0, 'Junior bachelor'), (1, 'Bachelor'), (2, 'Doctor of Philosophy'), (3, 'Master'), (4, 'PHD')], null=True, verbose_name='Educational Level'),
        ),
    ]
