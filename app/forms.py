from django import forms
from django.db.models import Q
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

from app.models import (
    Student,
    BachelorAdmission,
    Document,
    DocumentFile,
    AdmissionFile,
    VerbalProces
)


class CustomDateInput(forms.DateInput):
    input_type = 'date'


class StudentModelForm(forms.ModelForm):
    class Meta:
        model = Student
        # fields = '__all__'
        exclude = ('uid',)
        # widgets = {
        #     'date_of_birth': CustomDateInput()
        # }

    def clean_serial_number(self):
        serial = self.cleaned_data.get('serial_number')
        if Student.objects.filter(serial_number=serial).exists():
            raise forms.ValidationError('Un étudiant avec ce matricule existe déjà !')
        
        return serial
class DocumentModelForm(forms.ModelForm):
    # semester = forms.ChoiceField(
    #     label='Semestre concerné',
    #     choices=((1,'Semestre 1'), (2, 'Semestre 2'), (3, 'Semestre 3')))
    # files = forms.FileField(
    #     label="Fichier(s) associé(s) au document",
    #     widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta:
        model = Document
        fields = ('type', 'semester', 'file')
        labels = {
            'type': 'Type de document'
        }

    # def save(self, commit=True):
    #     files = self.cleaned_data.get('files')
    #     print(files)
    #     for file in files:
    #         DocumentFile.objects.create(
    #             file=file
    #         )
    #     if not commit:
    #         return super().save(commit=False)

    #     return super().save()


class SuplementInfoModelForm(forms.ModelForm):
    class Meta:
        model = BachelorAdmission
        fields = (
            'father_occupation',
            'mother_occupation',
            'parents_address',
        )


class VerbalProcesModelForm(forms.ModelForm):
    # students_list = forms.FileField(
    #     label='Fichier étudiants', help_text='La liste des étudiants ayant validés')

    class Meta:
        model = VerbalProces
        fields = '__all__'

    def clean(self):
        data = self.cleaned_data
        level = data.get('level')
        year = data.get('academic_year')

        if VerbalProces.objects.filter(Q(level=level) & Q(academic_year=year)).exists():
            self.add_error('level', 'Un procès verbal du même niveau et même année existe !')
            return
        return data
class AdmissionForm(forms.ModelForm):
    class Meta:
        model = AdmissionFile
        exclude = ('student', 'name', 'ext', 'size')
