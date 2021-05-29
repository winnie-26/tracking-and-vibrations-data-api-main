# Generated by Django 2.1.15 on 2021-03-30 11:42

from django.db import migrations, models
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coordinates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gps_coordinates', models.CharField(max_length=31)),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, max_length=31, populate_from=['gps_coordinates'])),
            ],
            options={
                'ordering': ['gps_coordinates'],
            },
        ),
        migrations.CreateModel(
            name='Vibrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vibration_reading', models.CharField(max_length=31)),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, max_length=31, populate_from=['vibration_reading'])),
            ],
            options={
                'ordering': ['vibration_reading'],
            },
        ),
    ]