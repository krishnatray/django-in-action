# Generated by Django 5.0.1 on 2024-02-08 15:52

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("bands", "0003_band"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="band",
            options={"ordering": ["name"]},
        ),
        migrations.AlterModelOptions(
            name="musician",
            options={"ordering": ["last_name", "first_name"]},
        ),
        migrations.AlterModelOptions(
            name="room",
            options={"ordering": ["name"]},
        ),
        migrations.AlterModelOptions(
            name="venue",
            options={"ordering": ["name"]},
        ),
    ]
