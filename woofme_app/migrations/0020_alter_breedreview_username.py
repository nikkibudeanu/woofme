# Generated by Django 3.2.13 on 2022-06-28 19:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('woofme_app', '0019_rename_author_breedreview_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='breedreview',
            name='username',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]