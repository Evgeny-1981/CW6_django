# Generated by Django 4.2 on 2024-07-16 18:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("mailings", "0024_alter_mailingattempt_options_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="mailingattempt",
            options={
                "ordering": ("status", "answer"),
                "verbose_name": "Отчет о рассылке",
                "verbose_name_plural": "Отчеты о рассылках",
            },
        ),
    ]
