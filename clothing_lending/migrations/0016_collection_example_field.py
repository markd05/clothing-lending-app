# Generated by Django 5.2 on 2025-04-30 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothing_lending', '0015_rename_return_requsted_lending_return_requested'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='example_field',
            field=models.TextField(blank=True, null=True),
        ),
    ]
