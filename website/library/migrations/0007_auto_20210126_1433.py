# Generated by Django 3.1.5 on 2021-01-26 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0006_auto_20210125_1008'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='library',
        ),
        migrations.AddField(
            model_name='library',
            name='books',
            field=models.ManyToManyField(related_name='libraries', to='library.Book'),
        ),
        migrations.AlterField(
            model_name='book',
            name='authors',
            field=models.TextField(max_length=500, verbose_name='Authors'),
        ),
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=models.ImageField(upload_to='covers', verbose_name='Cover'),
        ),
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.TextField(blank=True, max_length=1500, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='library',
            name='description',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='library',
            name='title',
            field=models.CharField(max_length=500, verbose_name='Title'),
        ),
    ]
