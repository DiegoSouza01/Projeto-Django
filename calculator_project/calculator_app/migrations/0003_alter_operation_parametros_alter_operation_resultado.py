# Generated by Django 5.2.4 on 2025-07-26 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("calculator_app", "0002_rename_timestamp_operation_dt_inclusao_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="operation",
            name="parametros",
            field=models.CharField(default="", max_length=200),
        ),
        migrations.AlterField(
            model_name="operation",
            name="resultado",
            field=models.CharField(default="0", max_length=200),
        ),
    ]
