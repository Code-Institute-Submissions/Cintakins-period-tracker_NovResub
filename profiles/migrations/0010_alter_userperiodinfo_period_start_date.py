# Generated by Django 4.1.1 on 2022-11-22 21:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0009_alter_userperiodinfo_period_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userperiodinfo',
            name='period_start_date',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]
