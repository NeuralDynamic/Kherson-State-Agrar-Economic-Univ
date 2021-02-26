# Generated by Django 3.0.10 on 2021-02-26 21:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0010_auto_20210218_1739'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name="Ім'я")),
                ('email', models.CharField(max_length=200, verbose_name='Email')),
                ('message', models.TextField(verbose_name='Питання')),
                ('created_at', models.DateField(default=django.utils.timezone.now, verbose_name='Дата')),
            ],
            options={
                'verbose_name': 'Запит на контакт',
                'verbose_name_plural': 'Запити на контакт',
            },
        ),
    ]