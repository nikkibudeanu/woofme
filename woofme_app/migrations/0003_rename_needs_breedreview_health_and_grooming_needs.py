# Generated by Django 3.2.13 on 2022-05-14 12:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('woofme_app', '0002_auto_20220514_1204'),
    ]

    operations = [
        migrations.RenameField(
            model_name='breedreview',
            old_name='needs',
            new_name='health_and_grooming_needs',
        ),
    ]