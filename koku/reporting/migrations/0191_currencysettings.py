# Generated by Django 3.1.13 on 2021-09-03 16:02
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [("reporting", "0190_ocp_on_all_partitioned_models")]

    operations = [
        migrations.CreateModel(
            name="CurrencySettings",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("currency", models.TextField()),
            ],
            options={"db_table": "currency_settings"},
        )
    ]