# Generated by Django 5.1.6 on 2025-03-25 13:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostel', '0015_remove_room_capacity_room_bed_number_room_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
