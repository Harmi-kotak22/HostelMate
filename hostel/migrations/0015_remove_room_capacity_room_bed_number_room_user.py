# Generated by Django 5.1.6 on 2025-03-25 13:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostel', '0014_rename_dates_feedback_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='capacity',
        ),
        migrations.AddField(
            model_name='room',
            name='bed_number',
            field=models.CharField(default='A', max_length=5),
        ),
        migrations.AddField(
            model_name='room',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
