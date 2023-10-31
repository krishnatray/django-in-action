# Generated by Django 4.1.5 on 2023-02-21 15:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("bands", "0002_venue_room"),
    ]

    operations = [
        migrations.CreateModel(
            name="Band",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=20)),
                ("musicians", models.ManyToManyField(to="bands.musician")),
            ],
        ),
    ]
