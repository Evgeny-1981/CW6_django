# Generated by Django 4.2 on 2024-07-15 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mailings", "0019_alter_mailingattempt_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="client",
            name="email",
            field=models.EmailField(max_length=254, verbose_name="Электронная почта"),
        ),
    ]
