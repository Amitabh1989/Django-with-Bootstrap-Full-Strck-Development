# Generated by Django 4.2.1 on 2023-05-28 12:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shadow", "0003_alter_patient_heartrate"),
    ]

    operations = [
        migrations.AlterField(
            model_name="patient",
            name="age",
            field=models.IntegerField(
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(120),
                ]
            ),
        ),
    ]
