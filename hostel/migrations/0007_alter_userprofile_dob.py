# Generated by Django 5.1.6 on 2025-03-08 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostel', '0006_remove_customuser_bed_number_remove_customuser_dob_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='dob',
            field=models.DateField(blank=True, null=True),
        ),
    ]
