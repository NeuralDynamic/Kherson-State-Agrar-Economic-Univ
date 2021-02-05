# Generated by Django 3.0.10 on 2021-02-04 16:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0008_auto_20210204_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discipline',
            name='staff',
            field=models.ManyToManyField(null=True, related_name='disciplines', to='university.Staff', verbose_name='Staff'),
        ),
        migrations.AlterField(
            model_name='links',
            name='staff',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='links', to='university.Staff', verbose_name='Staff'),
        ),
        migrations.AlterField(
            model_name='reward',
            name='staff',
            field=models.ManyToManyField(null=True, related_name='rewards', to='university.Staff', verbose_name='Staff'),
        ),
    ]