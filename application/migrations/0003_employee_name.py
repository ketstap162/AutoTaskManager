# Generated by Django 4.2.4 on 2023-09-04 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("application", "0002_order"),
    ]

    operations = [
        migrations.AddField(
            model_name="employee",
            name="name",
            field=models.CharField(default="UnknownUser", max_length=100),
        ),
    ]