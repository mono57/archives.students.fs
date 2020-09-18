# Generated by Django 3.0.8 on 2020-09-16 17:21

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20200916_1301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admissionfile',
            name='course_of_study',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_admissions', to='app.CourseOfStudy', verbose_name='Parcours'),
        ),
        migrations.AlterField(
            model_name='admissionfile',
            name='speciality',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='speciality_admissions', to='app.Speciality', verbose_name='Spécialité'),
        ),
        migrations.AlterField(
            model_name='student',
            name='uid',
            field=models.UUIDField(blank=True, default=uuid.UUID('67334adc-d968-4e1b-808b-fbc839d95b31')),
        ),
    ]