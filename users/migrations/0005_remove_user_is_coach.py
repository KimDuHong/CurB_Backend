# Generated by Django 4.2 on 2023-04-11 17:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0004_alter_user_group"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="is_coach",
        ),
    ]