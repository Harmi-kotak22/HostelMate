# Generated by Django 5.1.6 on 2025-03-12 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostel', '0007_alter_userprofile_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userroom',
            name='room_id',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10'), (11, '11'), (12, '12'), (13, '13'), (14, '14'), (15, '15'), (16, '16'), (17, '17'), (18, '18'), (19, '19'), (20, '20')]),
        ),
    ]
