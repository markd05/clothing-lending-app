# Generated by Django 5.2 on 2025-04-29 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothing_lending', '0013_alter_lending_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='lending',
            name='return_requsted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='lending',
            name='status',
            field=models.CharField(choices=[('PENDING', 'Pending'), ('APPROVED', 'Approved'), ('REJECTED', 'Rejected'), ('RETURNED', 'Returned')], default='PENDING', max_length=10),
        ),
    ]
