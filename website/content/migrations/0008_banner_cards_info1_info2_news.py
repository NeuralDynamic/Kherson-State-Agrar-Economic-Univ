# Generated by Django 3.0.10 on 2021-02-16 18:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
        ('content', '0007_auto_20210216_0916'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='content_banner', serialize=False, to='cms.CMSPlugin')),
                ('header', models.CharField(blank=True, max_length=100, null=True, verbose_name='Header')),
                ('subheader', models.CharField(blank=True, max_length=400, null=True, verbose_name='Subheader')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='Cards',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='content_cards', serialize=False, to='cms.CMSPlugin')),
                ('left_card_image', models.ImageField(upload_to='cms', verbose_name='Left card image')),
                ('left_card_title', models.CharField(blank=True, max_length=100, null=True, verbose_name='Left card title')),
                ('left_card_text', models.TextField(blank=True, max_length=400, null=True, verbose_name='Left card text')),
                ('middle_card_image', models.ImageField(upload_to='cms', verbose_name='Middle card image')),
                ('middle_card_title', models.CharField(blank=True, max_length=100, null=True, verbose_name='Middle card title')),
                ('middle_card_text', models.TextField(blank=True, max_length=400, null=True, verbose_name='Middle card text')),
                ('right_card_image', models.ImageField(upload_to='cms', verbose_name='Right card image')),
                ('right_card_title', models.CharField(blank=True, max_length=100, null=True, verbose_name='Right card title')),
                ('right_card_text', models.TextField(blank=True, max_length=400, null=True, verbose_name='Right card text')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='Info1',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='content_info1', serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(blank=True, max_length=100, null=True, verbose_name='Title')),
                ('description', models.TextField(blank=True, max_length=500, null=True, verbose_name='Description')),
                ('button_title', models.CharField(blank=True, max_length=100, null=True, verbose_name='Button title')),
                ('button_url', models.URLField(blank=True, null=True, verbose_name='Button url')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='Info2',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='content_info2', serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(blank=True, max_length=100, null=True, verbose_name='Title')),
                ('description', models.TextField(blank=True, max_length=500, null=True, verbose_name='Description')),
                ('button_title', models.CharField(blank=True, max_length=100, null=True, verbose_name='Button title')),
                ('button_url', models.URLField(blank=True, null=True, verbose_name='Button url')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='content_news', serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(blank=True, max_length=100, null=True, verbose_name='Title')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]