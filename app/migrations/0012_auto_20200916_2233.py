# Generated by Django 3.0.8 on 2020-09-16 21:33

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20200916_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='uid',
            field=models.UUIDField(blank=True, default=uuid.UUID('465d4b2e-21da-4741-b1bc-d58ce569a67c')),
        ),
        migrations.RemoveField(
            model_name='student',
            name='verbal_proces',
        ),
        migrations.AddField(
            model_name='student',
            name='verbal_proces',
            field=models.ManyToManyField(blank=True, related_name='students', to='app.VerbalProces', verbose_name='Procès verbal'),
        ),
    ]