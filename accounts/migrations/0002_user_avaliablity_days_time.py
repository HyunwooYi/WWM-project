# Generated by Django 4.1 on 2022-08-06 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="avaliablity_days_time",
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
