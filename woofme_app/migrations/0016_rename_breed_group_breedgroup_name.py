# Generated by Django 3.2.13 on 2022-06-27 20:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('woofme_app', '0015_rename_name_breedgroup_breed_group'),
    ]

    operations = [
        migrations.RenameField(
            model_name='breedgroup',
            old_name='breed_group',
            new_name='name',
        ),
    ]
