# Generated by Django 3.2.13 on 2022-06-11 22:43

from django.db import migrations
import slugger.fields


class Migration(migrations.Migration):

    dependencies = [
        ('woofme_app', '0013_auto_20220526_1533'),
    ]

    operations = [
        migrations.AddField(
            model_name='breedgroup',
            name='slug',
            field=slugger.fields.AutoSlugField(default='group', populate_from='breed_group'),
        ),
    ]
