# Generated by Django 3.2.13 on 2022-05-26 15:10

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('woofme_app', '0011_auto_20220525_1729'),
    ]

    operations = [
        migrations.RenameField(
            model_name='breed',
            old_name='breed_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='breedreview',
            old_name='user_name',
            new_name='author',
        ),
        migrations.RemoveField(
            model_name='breed',
            name='group',
        ),
        migrations.RemoveField(
            model_name='breedgroup',
            name='breed_group',
        ),
        migrations.RemoveField(
            model_name='breedreview',
            name='breed_group',
        ),
        migrations.RemoveField(
            model_name='breedreview',
            name='breed_image',
        ),
        migrations.RemoveField(
            model_name='breedreview',
            name='published_date',
        ),
        migrations.RemoveField(
            model_name='breedreview',
            name='slug',
        ),
        migrations.AddField(
            model_name='breed',
            name='breed_group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='woofme_app.breedgroup'),
        ),
        migrations.AddField(
            model_name='breed',
            name='breed_image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, verbose_name='image'),
        ),
        migrations.AddField(
            model_name='breed',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='breed',
            name='slug',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='breed',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='breedgroup',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='breedgroup',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='breedreview',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='breedreview',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='breedreview',
            name='rating',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=0),
        ),
    ]