# Generated by Django 4.2 on 2023-04-11 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0005_remove_user_is_coach"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="is_coach",
            field=models.BooleanField(default=False),
        ),
    ]
