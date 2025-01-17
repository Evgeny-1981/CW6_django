# Generated by Django 4.2 on 2024-07-10 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mailings", "0007_alter_mailing_frequency_alter_mailing_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="mailing",
            name="frequency",
            field=models.CharField(
                choices=[
                    ("Daily", "Ежедневно"),
                    ("Weekly", "Еженедельно"),
                    ("Monthly", "Ежемесячно"),
                ],
                max_length=15,
                verbose_name="Периодичность рассылки",
            ),
        ),
        migrations.AlterField(
            model_name="mailing",
            name="status",
            field=models.CharField(
                choices=[
                    ("Completed", "Завершена"),
                    ("Created", "Создана"),
                    ("Launched", "Запущена"),
                ],
                default="created",
                max_length=10,
                verbose_name="Статус рассылки",
            ),
        ),
    ]
