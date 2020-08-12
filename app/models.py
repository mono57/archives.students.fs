from django.db import models
import uuid
from django.urls import reverse

from app.managers import StudentManager


class TimeStampModel(models.Model):
    created_at = models.DateField(auto_now=True, auto_now_add=False)
    updated_at = models.DateField(auto_now=False, auto_now_add=True)

    class Meta:
        abstract = True


class CommonModel(TimeStampModel):
    name = models.CharField(max_length=150, verbose_name='Nom')

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Level(TimeStampModel):
    full_name = models.CharField(max_length=150, verbose_name='Nom')
    short_name = models.CharField(max_length=10, verbose_name='Abbréviation')

    def __str__(self):
        return self.short_name


class Student(TimeStampModel):
    uid = models.UUIDField(blank=True, default=uuid.uuid4())
    first_name = models.CharField(max_length=200, verbose_name='Prénom(s)')
    last_name = models.CharField(max_length=200, verbose_name='Nom(s)')
    serial_number = models.CharField(max_length=10, verbose_name='Matricule')
    date_of_birth = models.DateField(verbose_name='Date de naissance')
    place_of_birth = models.CharField(
        max_length=100, verbose_name='Lieu de naissance')
    region_of_origin = models.CharField(
        max_length=100, verbose_name='Region d\'origine')
    father_name = models.CharField(
        max_length=255, verbose_name='Nom(s) du père')
    mother_name = models.CharField(
        max_length=255, verbose_name='Nom(s) de la mère')
    gender = models.CharField(max_length=10, verbose_name='Sexe', default='male', choices=(
        ('female', 'Feminin'), ('male', 'Masculin')))
    nationality = models.CharField(
        max_length=50,
        verbose_name='Nationnalité'
    )

    objects = StudentManager()

    def get_full_name(self):
        return '{} {}'.format(self.last_name, self.first_name)

    def get_absolute_url(self):
        return reverse("app:student-detail", kwargs={"uid": self.uid})

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Department(CommonModel):
    class Meta:
        verbose_name = 'Departement'
        verbose_name_plural = 'Departements'

    def has_course_of_studies(self):
        return self.course_of_studies.all()


class CourseOfStudy(CommonModel):
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name='course_of_studies'
    )

    class Meta:
        verbose_name = 'Parcours'
        verbose_name_plural = 'Parcours'


class Speciality(CommonModel):
    course_of_study = models.ForeignKey(
        CourseOfStudy,
        on_delete=models.CASCADE,
        related_name='specialities'
    )

    class Meta:
        verbose_name = 'Spécialité'
        verbose_name_plural = 'Spécialités'


class BachelorAdmission(CommonModel):
    academic_year = models.CharField(
        max_length=10,
        blank=True,
        verbose_name='Année académique'
    )
    level = models.ForeignKey(
        Level,
        blank=True,
        on_delete=models.CASCADE,
        verbose_name='Niveau',
        related_name='bachelor_level')

    father_occupation = models.CharField(
        max_length=100,
        blank=True,
        verbose_name='Occupation du père')

    mother_occupation = models.CharField(
        max_length=100,
        blank=True,
        verbose_name='Occupation de la mère')

    parents_address = models.CharField(
        max_length=100,
        blank=True,
        verbose_name='Adresse des parents')

    course_of_study = models.ForeignKey(
        CourseOfStudy,
        blank=True,
        on_delete=models.CASCADE,
        verbose_name='Parcours de l\'étudiant',
        related_name='admissions_course')

    # Camerounian Bachelor Admission fields
    bac_serial = models.CharField(
        max_length=25,
        blank=True,
        verbose_name='Série Bac')

    grade = models.CharField(
        max_length=50,
        blank=True,
        verbose_name='Mention')

    date_obtained = models.DateField(
        blank=True,
        verbose_name='Année d\'obtention')

    # Foreign Bachelor Admission fields
    entry_qualification = models.CharField(
        max_length=100,
        blank=True,
        verbose_name='Diplôme d\'entrée')

    other_entry_qualification = models.CharField(
        max_length=100,
        verbose_name='Autre diplôme d\'entrée',
        blank=True
    )

    city = models.CharField(
        max_length=150,
        blank=True,
        verbose_name='Ville'
    )

    country = models.CharField(
        max_length=100,
        blank=True,
        verbose_name='Pays'
    )

    student = models.ForeignKey(
        Student,
        blank=True,
        on_delete=models.CASCADE,
        verbose_name='Etudiant'
    )

    def __str__(self):
        return '{} {}'.format(self.student.first_name, self.student.lastname)


class Folder(TimeStampModel):
    name = models.CharField(
        max_length=100,
        blank=True,
        verbose_name='Nom du dossier'
    )


class Semester(TimeStampModel):
    number = models.IntegerField(
        verbose_name='Numero de semestre'
    )

    def __str__(self):
        return 'Semestre: {}'.format(self.number)


class DocumentType(TimeStampModel):
    name = models.CharField(max_length=255, verbose_name='Nom')

    def __str__(self):
        return self.name


class Document(TimeStampModel):
    type = models.ForeignKey(
        DocumentType,
        on_delete=models.CASCADE,
        related_name='documents')
    level = models.ForeignKey(
        Level,
        on_delete=models.CASCADE,
        verbose_name='niveau')
        
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        verbose_name='Etudiant',
        related_name = 'documents'
    )


class DocumentFile(TimeStampModel):
    file = models.FileField(upload_to='documents/', verbose_name='fichier')
    ext = models.CharField(max_length=10, blank=True, verbose_name='extension')
    document = models.ForeignKey(
        Document,
        on_delete=models.CASCADE,
        related_name='files'
    )

    def __str__(self):
        return 'Fichier: {}'.format(self.pk)


class AdmissionFile(TimeStampModel):
    level = models.ForeignKey(
        Level,
        on_delete=models.CASCADE,
        verbose_name='Niveau d\'étude'
    )
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        verbose_name='Etudiant',
        related_name='admissions'
    )
    file = models.FileField(
        upload_to='admission/', 
        verbose_name='Fiche d\'inscription'
    )
    name = models.CharField(
        max_length=255, 
        verbose_name='Nom du fichier',
    )
    ext = models.CharField(
        max_length=10,
        verbose_name='Extension du fichier'
    )

    def __str__(self):
        return 'Fiche : {}'.format(self.pk)
