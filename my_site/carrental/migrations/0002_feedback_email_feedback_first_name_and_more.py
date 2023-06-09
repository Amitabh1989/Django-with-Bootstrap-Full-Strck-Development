# Generated by Django 4.2.1 on 2023-05-29 01:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("carrental", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="feedback",
            name="email",
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name="feedback",
            name="first_name",
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="feedback",
            name="last_name",
            field=models.CharField(default="Woohoo", max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="feedback",
            name="stars",
            field=models.CharField(
                choices=[
                    ("0", "0"),
                    ("1", "1"),
                    ("2", "2"),
                    ("3", "3"),
                    ("4", "4"),
                    ("5", "5"),
                ],
                max_length=1,
            ),
        ),
    ]
