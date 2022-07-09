# Generated by Django 3.2.14 on 2022-07-09 10:13

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('woofme_app', '0002_breedgroup_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='breedreview',
            name='breed_image',
            field=cloudinary.models.CloudinaryField(blank=True, default='https://res.cloudinary.com/nikkibudeanu/image/upload/v1657234328/dog_gif_e5azfj.gif', max_length=255, verbose_name='image'),
        ),
    ]