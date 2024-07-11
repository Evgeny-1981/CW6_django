# Generated by Django 4.2 on 2024-07-11 07:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("mailings", "0010_alter_mailing_message"),
    ]

    operations = [
        migrations.AlterField(
            model_name="mailing",
            name="message",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="mailings.message",
                verbose_name="Сообщение для рассылки",
            ),
        ),
    ]
