# Generated by Django 3.2.13 on 2022-05-25 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('woofme_app', '0010_breedreview_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='breedreview',
            name='adaptability',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=0),
        ),
        migrations.AlterField(
            model_name='breedreview',
            name='friendliness',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=0),
        ),
        migrations.AlterField(
            model_name='breedreview',
            name='health_and_grooming_needs',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=0),
        ),
        migrations.AlterField(
            model_name='breedreview',
            name='trainability',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=0),
        ),
    ]
