# Generated by Django 4.1.5 on 2023-05-18 16:22

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("content", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="seekingad",
            options={"ordering": ["date"]},
        ),
    ]
