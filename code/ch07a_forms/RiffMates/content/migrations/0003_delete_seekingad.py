# Generated by Django 5.0.1 on 2024-02-11 19:47

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("content", "0002_alter_seekingad_options"),
    ]

    operations = [
        migrations.DeleteModel(
            name="SeekingAd",
        ),
    ]
