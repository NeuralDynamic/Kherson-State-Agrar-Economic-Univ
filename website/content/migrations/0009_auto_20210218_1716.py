# Generated by Django 3.0.10 on 2021-02-18 15:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
        ('content', '0008_banner_cards_info1_info2_news'),
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='content_info', serialize=False, to='cms.CMSPlugin')),
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
        migrations.RemoveField(
            model_name='info2',
            name='cmsplugin_ptr',
        ),
        migrations.RenameField(
            model_name='footer',
            old_name='email1',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='footer',
            old_name='phone1',
            new_name='phone',
        ),
        migrations.RemoveField(
            model_name='footer',
            name='email2',
        ),
        migrations.RemoveField(
            model_name='footer',
            name='phone2',
        ),
        migrations.AddField(
            model_name='footer',
            name='tiktok_link',
            field=models.URLField(blank=True, null=True, verbose_name='Tiktok link'),
        ),
        migrations.DeleteModel(
            name='Info1',
        ),
        migrations.DeleteModel(
            name='Info2',
        ),
    ]
