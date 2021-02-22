# Generated by Django 3.0.10 on 2021-02-22 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0027_auto_20210222_1352'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reward',
            name='staff',
        ),
        migrations.AddField(
            model_name='staff',
            name='rewards',
            field=models.ManyToManyField(blank=True, related_name='staff_rewards', to='university.Reward', verbose_name='Rewards'),
        ),
    ]
