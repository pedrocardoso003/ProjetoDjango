# Generated by Django 5.1.3 on 2025-04-29 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tecnologia",
            name="nome",
            field=models.CharField(max_length=255),
        ),
    ]
