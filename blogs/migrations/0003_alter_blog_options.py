# Generated by Django 4.2 on 2024-07-19 04:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blogs", "0002_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="blog",
            options={
                "ordering": ("count_views",),
                "permissions": [
                    ("View_any_entries", "Просматривать любые записи"),
                    ("Edit_entries", "Редактировать запись"),
                ],
                "verbose_name": "блог",
                "verbose_name_plural": "блоги",
            },
        ),
    ]