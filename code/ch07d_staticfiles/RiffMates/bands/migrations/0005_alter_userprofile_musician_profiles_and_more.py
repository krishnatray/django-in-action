# Generated by Django 4.1.5 on 2023-05-15 17:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("bands", "0004_alter_band_options_alter_musician_options_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofile",
            name="musician_profiles",
            field=models.ManyToManyField(blank=True, to="bands.musician"),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="venues_controlled",
            field=models.ManyToManyField(blank=True, to="bands.venue"),
        ),
    ]
