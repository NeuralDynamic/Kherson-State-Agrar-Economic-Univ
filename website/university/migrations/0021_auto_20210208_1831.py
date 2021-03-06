# Generated by Django 3.0.10 on 2021-02-08 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0020_auto_20210208_1812'),
    ]

    operations = [
        migrations.AddField(
            model_name='scientificsociety',
            name='staff',
            field=models.ManyToManyField(related_name='staff', to='university.Staff', verbose_name='Staffs'),
        ),
        migrations.AlterField(
            model_name='cathedratranslation',
            name='title',
            field=models.CharField(default='', max_length=100, unique=True, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='disciplinetranslation',
            name='title',
            field=models.CharField(default='', max_length=100, unique=True, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='facultytranslation',
            name='title',
            field=models.CharField(default='', max_length=100, unique=True, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='speciality',
            name='number',
            field=models.CharField(default='', max_length=10, unique=True, verbose_name='Number'),
        ),
        migrations.AlterField(
            model_name='specialitytranslation',
            name='title',
            field=models.CharField(default='', max_length=100, unique=True, verbose_name='Title'),
        ),
    ]
