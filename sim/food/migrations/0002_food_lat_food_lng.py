# Generated by Django 4.0.7 on 2022-09-28 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='lat',
            field=models.FloatField(blank=True, null=True, verbose_name='latitude'),
        ),
        migrations.AddField(
            model_name='food',
            name='lng',
            field=models.FloatField(blank=True, null=True, verbose_name='longtite'),
        ),
    ]
