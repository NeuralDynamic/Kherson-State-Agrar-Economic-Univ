# Generated by Django 3.0.10 on 2021-02-03 12:21

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import multi_email_field.fields
import parler.fields
import parler.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('library', '0001_initial'),
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cathedra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emblem', models.ImageField(default='', upload_to='cathedras/emblems', verbose_name='Emblem')),
                ('number', models.CharField(default='', max_length=20, verbose_name='Number')),
                ('created_at', models.DateField(default=django.utils.timezone.now, verbose_name='Created at')),
            ],
            options={
                'verbose_name': 'Cathedra',
                'verbose_name_plural': 'Cathedras',
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emblem', models.ImageField(default='', upload_to='faculties/emblems', verbose_name='Emblem')),
                ('gallery', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='faculties', to='gallery.Gallery', verbose_name='Gallery')),
            ],
            options={
                'verbose_name': 'Faculty',
                'verbose_name_plural': 'Faculties',
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Speciality',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(default='', max_length=10, verbose_name='Number')),
                ('cathedra', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='specialities', to='university.Cathedra', verbose_name='Cathedra')),
            ],
            options={
                'verbose_name': 'Speciality',
                'verbose_name_plural': 'Specialities',
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='photos', verbose_name='Photo')),
                ('phone', models.CharField(max_length=20, verbose_name='Phone number')),
                ('emails', multi_email_field.fields.MultiEmailField(default=[])),
                ('library', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='staff', to='library.Library', verbose_name='Library')),
            ],
            options={
                'verbose_name': 'Staff',
                'verbose_name_plural': 'Staff',
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='StaffCathedra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cathedras', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='university.Cathedra', verbose_name='Cathedra')),
                ('staff', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='university.Staff', verbose_name='Staff')),
            ],
            options={
                'verbose_name': 'Cathedra staff',
                'verbose_name_plural': 'Cathedra staffs',
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='StaffFaculty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faculties', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='university.Faculty', verbose_name='Faculty')),
                ('staff', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='university.Staff', verbose_name='Staff')),
            ],
            options={
                'verbose_name': 'Faculty staff',
                'verbose_name_plural': 'Faculty staffs',
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Reward',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(choices=[(2021, 2021), (2020, 2020), (2019, 2019), (2018, 2018), (2017, 2017), (2016, 2016), (2015, 2015), (2014, 2014), (2013, 2013), (2012, 2012), (2011, 2011), (2010, 2010), (2009, 2009), (2008, 2008), (2007, 2007), (2006, 2006), (2005, 2005), (2004, 2004), (2003, 2003), (2002, 2002), (2001, 2001), (2000, 2000), (1999, 1999), (1998, 1998), (1997, 1997), (1996, 1996), (1995, 1995), (1994, 1994), (1993, 1993), (1992, 1992), (1991, 1991), (1990, 1990), (1989, 1989), (1988, 1988), (1987, 1987), (1986, 1986), (1985, 1985), (1984, 1984), (1983, 1983), (1982, 1982), (1981, 1981), (1980, 1980), (1979, 1979), (1978, 1978), (1977, 1977), (1976, 1976), (1975, 1975), (1974, 1974), (1973, 1973), (1972, 1972), (1971, 1971), (1970, 1970), (1969, 1969), (1968, 1968), (1967, 1967), (1966, 1966), (1965, 1965), (1964, 1964), (1963, 1963), (1962, 1962), (1961, 1961), (1960, 1960), (1959, 1959), (1958, 1958), (1957, 1957), (1956, 1956), (1955, 1955), (1954, 1954), (1953, 1953), (1952, 1952), (1951, 1951), (1950, 1950)], null=True, verbose_name='Year')),
                ('staff', models.ManyToManyField(null=True, to='university.Staff', verbose_name='Staff')),
            ],
            options={
                'verbose_name': 'Reward',
                'verbose_name_plural': 'Rewards',
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Links',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('google_scholar', models.URLField(blank=True, null=True, verbose_name='Google Scholar')),
                ('web_of_science', models.URLField(blank=True, null=True, verbose_name='Web Of Science')),
                ('researchgate', models.URLField(blank=True, null=True, verbose_name='Researchgate')),
                ('scopus', models.URLField(blank=True, null=True, verbose_name='Scopus')),
                ('orcid', models.URLField(blank=True, null=True, verbose_name='ORCID')),
                ('staff', models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='university.Staff', verbose_name='Staff')),
            ],
            options={
                'verbose_name': 'Links',
                'verbose_name_plural': 'Links',
            },
        ),
        migrations.AddField(
            model_name='faculty',
            name='staff',
            field=models.ManyToManyField(to='university.StaffFaculty', verbose_name='Staff'),
        ),
        migrations.CreateModel(
            name='Discipline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff', models.ManyToManyField(null=True, to='university.Staff', verbose_name='Staff')),
            ],
            options={
                'verbose_name': 'Discipline',
                'verbose_name_plural': 'Disciplines',
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.AddField(
            model_name='cathedra',
            name='faculty',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='cathedras', to='university.Faculty', verbose_name='Faculty'),
        ),
        migrations.AddField(
            model_name='cathedra',
            name='gallery',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cathedras', to='gallery.Gallery', verbose_name='Gallery'),
        ),
        migrations.AddField(
            model_name='cathedra',
            name='staff',
            field=models.ManyToManyField(to='university.StaffCathedra', verbose_name='Staff'),
        ),
        migrations.CreateModel(
            name='StaffTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('second_name', models.CharField(max_length=40, verbose_name='Second name')),
                ('first_name', models.CharField(max_length=40, verbose_name='First name')),
                ('third_name', models.CharField(max_length=40, verbose_name='Third name')),
                ('rank', models.CharField(blank=True, max_length=100, verbose_name='Rank')),
                ('methodical_works', models.TextField(verbose_name='Methodical works')),
                ('description', models.TextField(verbose_name='Description')),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='university.Staff')),
            ],
            options={
                'verbose_name': 'Staff Translation',
                'db_table': 'university_staff_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='StaffFacultyTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('position', models.CharField(blank=True, max_length=100, null=True, verbose_name='Position')),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='university.StaffFaculty')),
            ],
            options={
                'verbose_name': 'Faculty staff Translation',
                'db_table': 'university_stafffaculty_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='StaffCathedraTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('rank', models.CharField(blank=True, max_length=100, null=True, verbose_name='Rank')),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='university.StaffCathedra')),
            ],
            options={
                'verbose_name': 'Cathedra staff Translation',
                'db_table': 'university_staffcathedra_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='SpecialityTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('description', models.TextField(default='', max_length=1500, verbose_name='Description')),
                ('title', models.CharField(default='', max_length=100, verbose_name='Title')),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='university.Speciality')),
            ],
            options={
                'verbose_name': 'Speciality Translation',
                'db_table': 'university_speciality_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='RewardTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('title', models.CharField(max_length=300, verbose_name='Title')),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='university.Reward')),
            ],
            options={
                'verbose_name': 'Reward Translation',
                'db_table': 'university_reward_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='FacultyTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('description', models.TextField(default='', max_length=1500, verbose_name='Description')),
                ('title', models.CharField(default='', max_length=100, verbose_name='Title')),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='university.Faculty')),
            ],
            options={
                'verbose_name': 'Faculty Translation',
                'db_table': 'university_faculty_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='DisciplineTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('title', models.CharField(default='', max_length=100, verbose_name='Title')),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='university.Discipline')),
            ],
            options={
                'verbose_name': 'Discipline Translation',
                'db_table': 'university_discipline_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='CathedraTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('description', models.TextField(default='', max_length=1500, verbose_name='Description')),
                ('goal', models.TextField(default='', max_length=1500, verbose_name='Goal')),
                ('title', models.CharField(default='', max_length=100, verbose_name='Title')),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='university.Cathedra')),
            ],
            options={
                'verbose_name': 'Cathedra Translation',
                'db_table': 'university_cathedra_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
    ]
