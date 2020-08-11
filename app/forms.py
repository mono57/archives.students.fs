from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

from app.models import (
    Student, 
    BachelorAdmission, 
    Document,
    DocumentFile,
    AdmissionFile
    )


class CustomDateInput(forms.DateInput):
    input_type = 'date'


class StudentModelForm(forms.ModelForm):
    class Meta:
        model = Student
        # fields = '__all__'
        exclude = ('uid',)
        widgets = {
            'date_of_birth': CustomDateInput()
        }


class DocumentModelForm(forms.ModelForm):
    semester = forms.ChoiceField(
        label='Semestre concerné', 
        choices=((1,'Semestre 1'), (2, 'Semestre 2'), (3, 'Semestre 3')))
    files = forms.FileField(
        label="Fichier(s) associé(s) au document",
        widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta:
        model = Document
        fields = ('type',)
        labels = {
            'type': 'Type de document'
        }

    def save(self, commit=True):
        files = self.cleaned_data.get('files')
        print(files)
        for file in files:
            DocumentFile.objects.create(
                file=file
            )
        if not commit:
            return super().save(commit=False)

        return super().save()


class SuplementInfoModelForm(forms.ModelForm):
    class Meta:
        model = BachelorAdmission
        fields = (
            'father_occupation',
            'mother_occupation',
            'parents_address',
        )

class AdmissionForm(forms.ModelForm):
    class Meta:
        model = AdmissionFile
        exclude = ('student',)