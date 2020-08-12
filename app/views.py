from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.contrib import messages
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect
from django.contrib.messages.views import SuccessMessageMixin
from formtools.wizard.views import SessionWizardView
from app.models import *
from app.forms import (
    StudentModelForm, SuplementInfoModelForm, DocumentModelForm, AdmissionForm)


class StudentCreateView(
        LoginRequiredMixin,
        CreateView,
        SuccessMessageMixin):
    form_class = StudentModelForm
    template_name = 'app/student-form.html'
    success_url = reverse_lazy('home')
    success_message = 'Etudiant ajouté avec succès !'


class StudentDetailView(LoginRequiredMixin, DetailView):
    template_name = 'app/student-detail.html'
    model = Student
    context_object_name = 'student'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        obj = self.get_object()
        documents = [*obj.documents.all(), *obj.admissions.all()]
        ctx['documents'] = documents
        return ctx

    def get_object(self):
        uid = self.kwargs.get('uid')
        print(uid)
        return get_object_or_404(
            self.model,
            uid=uid
        )


class AdmissionSessionWizardView(
        LoginRequiredMixin,
        SessionWizardView):
    form_list = (StudentModelForm, SuplementInfoModelForm)
    template_name = 'app/admission-form.html'
    success_url = reverse_lazy('home')
    success_message = 'Enregistrement effectué avec succès'

    def make_message(self, ):
        messages.add_message(
            self.request,
            messages.SUCCESS,
            self.success_message
        )

    def get_success_url(self):
        self.make_message()
        return redirect(self.success_url)

    def done(self, form_list, form_dict, **kwargs):
        print(form_list)
        print(form_dict)
        return self.get_success_url()


class CourseOfStudyDetailView(
        LoginRequiredMixin,
        DetailView):
    template_name = 'course_study-list.html'
    model = CourseOfStudy
    context_object_name = 'course_of_study'

    # def get_context_data(self, **kwargs):
    #     ctx = super().get_context_data(**kwargs)
    #     course_of_study_choice = self.get_object().name
    #     ctx['students'] = Student.objects.filter(
    #         Q(course_of_study_first_choice=course_of_study_choice))
    #     return ctx


class DocumentCreateView(
        LoginRequiredMixin,
        SuccessMessageMixin,
        CreateView):
    form_class = DocumentModelForm
    template_name = 'app/document-form.html'
    success_message = 'Document(s) ajouté(s)'

    def form_valid(self, form):
        doc = form.save(commit=False)
        print(doc)
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['student'] = get_object_or_404(
            Student, uid=self.kwargs.get('uid'))
        return context

    def get_success_url(self):
        return reverse('app:student-detail', kwargs={'uid': self.kwargs.get('uid')})


class AdmissionFileCreateView(
        LoginRequiredMixin,
        SuccessMessageMixin,
        CreateView):
    form_class = AdmissionForm
    template_name = 'app/admission-form.html'
    success_message = 'Fiche d\'admission ajoutée avec succès !'

    def get_concern_object(self):
        return get_object_or_404(
            Student,
            uid=self.kwargs.get('uid'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['student'] = self.get_concern_object()
        return context

    def form_valid(self, form):
        obj = form.save(commit=False)
        file_str = str(obj.file)
        file_splited = file_str.split('.')
        obj.name = file_splited[0]
        obj.ext = file_splited[1]
        obj.student = self.get_concern_object()
        obj.save()
        return super().form_valid(form)

    def get_success_url(self):
        return self.get_concern_object().get_absolute_url()
