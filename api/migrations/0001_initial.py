# Generated by Django 5.1.2 on 2024-10-10 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('tconst', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('title_type', models.CharField(max_length=50)),
                ('primary_title', models.CharField(max_length=255)),
                ('original_title', models.CharField(max_length=255)),
                ('is_adult', models.BooleanField(default=False)),
                ('start_year', models.IntegerField(null=True)),
                ('end_year', models.IntegerField(null=True)),
                ('runtime_minutes', models.IntegerField(null=True)),
                ('genres', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('nconst', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('primary_name', models.CharField(max_length=255)),
                ('birth_year', models.IntegerField(null=True)),
                ('death_year', models.IntegerField(null=True)),
                ('primary_profession', models.CharField(max_length=255)),
                ('known_for_titles', models.CharField(max_length=255)),
            ],
        ),
    ]
