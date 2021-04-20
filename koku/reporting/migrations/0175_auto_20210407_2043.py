# Generated by Django 3.1.7 on 2021-04-07 20:43
import django.contrib.postgres.fields
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [("reporting", "0174_update_ocpall_matviews")]

    operations = [
        migrations.AlterField(
            model_name="ocpawstagssummary",
            name="values",
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), size=None),
        ),
        migrations.AlterField(
            model_name="ocpazuretagssummary",
            name="values",
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), size=None),
        ),
    ]