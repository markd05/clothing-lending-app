# Generated by Django 5.2 on 2025-04-30 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothing_lending', '0017_remove_collection_example_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='lending',
            name='rejected_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
