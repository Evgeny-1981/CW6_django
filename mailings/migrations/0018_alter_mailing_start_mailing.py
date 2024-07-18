# Generated by Django 4.2 on 2024-07-15 03:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("mailings", "0017_alter_mailing_start_mailing"),
    ]

    operations = [
        migrations.AlterField(
            model_name="mailing",
            name="start_mailing",
            field=models.DateTimeField(
                default=django.utils.timezone.now,
                verbose_name="Дата и время первой отправки",
            ),
        ),
    ]