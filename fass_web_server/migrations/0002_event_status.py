# Generated by Django 3.2 on 2023-05-22 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fass_web_server', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='status',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
