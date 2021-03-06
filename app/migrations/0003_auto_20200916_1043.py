# Generated by Django 3.0.8 on 2020-09-16 09:43

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20200916_1035'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='handicap',
            field=models.BooleanField(default=False, verbose_name='Êtes vous handicapé ?'),
        ),
        migrations.AddField(
            model_name='student',
            name='refugee',
            field=models.BooleanField(default=False, verbose_name='Êtes vous un réfugié ?'),
        ),
        migrations.AlterField(
            model_name='student',
            name='first_name',
            field=models.CharField(blank=True, max_length=200, verbose_name='Prénom(s)'),
        ),
        migrations.AlterField(
            model_name='student',
            name='uid',
            field=models.UUIDField(blank=True, default=uuid.UUID('907380df-5be2-4520-8be7-72c10d323118')),
        ),
    ]
