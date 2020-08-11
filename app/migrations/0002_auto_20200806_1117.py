# Generated by Django 3.0.8 on 2020-08-06 11:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='matricule',
            new_name='serial_number',
        ),
        migrations.RemoveField(
            model_name='bacheloradmission',
            name='department_first_choice',
        ),
        migrations.RemoveField(
            model_name='bacheloradmission',
            name='department_second_choice',
        ),
        migrations.RemoveField(
            model_name='bacheloradmission',
            name='fd_course_study_fc',
        ),
        migrations.RemoveField(
            model_name='bacheloradmission',
            name='fd_course_study_sc',
        ),
        migrations.RemoveField(
            model_name='bacheloradmission',
            name='sd_course_study_fc',
        ),
        migrations.RemoveField(
            model_name='bacheloradmission',
            name='sd_course_study_sc',
        ),
        migrations.AddField(
            model_name='bacheloradmission',
            name='course_of_study',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, related_name='admissions_course', to='app.CourseOfStudy', verbose_name="Parcours de l'étudiant"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='nationality',
            field=models.CharField(blank=True, max_length=50, verbose_name='Nationnalité'),
        ),
        migrations.AlterField(
            model_name='bacheloradmission',
            name='academic_year',
            field=models.CharField(blank=True, max_length=10, verbose_name='Année académique'),
        ),
        migrations.AlterField(
            model_name='bacheloradmission',
            name='bac_serial',
            field=models.CharField(blank=True, max_length=25, verbose_name='Série Bac'),
        ),
        migrations.AlterField(
            model_name='bacheloradmission',
            name='city',
            field=models.CharField(blank=True, max_length=150, verbose_name='Ville'),
        ),
        migrations.AlterField(
            model_name='bacheloradmission',
            name='country',
            field=models.CharField(blank=True, max_length=100, verbose_name='Pays'),
        ),
        migrations.AlterField(
            model_name='bacheloradmission',
            name='date_obtained',
            field=models.DateField(blank=True, verbose_name="Année d'obtention"),
        ),
        migrations.AlterField(
            model_name='bacheloradmission',
            name='entry_qualification',
            field=models.CharField(blank=True, max_length=100, verbose_name="Diplôme d'entrée"),
        ),
        migrations.AlterField(
            model_name='bacheloradmission',
            name='father_occupation',
            field=models.CharField(blank=True, max_length=100, verbose_name='Occupation du père'),
        ),
        migrations.AlterField(
            model_name='bacheloradmission',
            name='grade',
            field=models.CharField(blank=True, max_length=50, verbose_name='Mention'),
        ),
        migrations.AlterField(
            model_name='bacheloradmission',
            name='level',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='bachelor_level', to='app.Level', verbose_name='Niveau'),
        ),
        migrations.AlterField(
            model_name='bacheloradmission',
            name='mother_occupation',
            field=models.CharField(blank=True, max_length=100, verbose_name='Occupation de la mère'),
        ),
        migrations.AlterField(
            model_name='bacheloradmission',
            name='parents_address',
            field=models.CharField(blank=True, max_length=100, verbose_name='Adresse des parents'),
        ),
        migrations.AlterField(
            model_name='bacheloradmission',
            name='student',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='app.Student', verbose_name='Etudiant'),
        ),
        migrations.AlterField(
            model_name='courseofstudy',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_of_studies', to='app.Department'),
        ),
    ]
