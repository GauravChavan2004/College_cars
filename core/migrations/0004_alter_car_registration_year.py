# Generated by Django 5.1 on 2025-02-08 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_car_registration_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='registration_year',
            field=models.CharField(help_text='Enter in the format: YYYY-MM', max_length=7),
        ),
    ]
