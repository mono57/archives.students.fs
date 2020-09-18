from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.contrib import messages
from django.urls import reverse_lazy, reverse
from django.conf import settings
from django.shortcuts import redirect
from django.contrib.messages.views import SuccessMessageMixin
from formtools.wizard.views import SessionWizardView
from app.models import *
from app.forms import (
    StudentModelForm, SuplementInfoModelForm, VerbalProcesModelForm,
    DocumentModelForm, AdmissionForm, DocumentFile)

import json


class StudentCreateView(
        LoginRequiredMixin,
        CreateView,
        SuccessMessageMixin):
    form_class = StudentModelForm
    template_name = 'app/student-form.html'
    success_url = reverse_lazy('home')
    success_message = 'Etudiant ajouté avec succès !'


class StudentSearchListView(LoginRequiredMixin, ListView):
    template_name = 'app/student-list.html'
    model = Student
    context_object_name = 'students'

    def get(self, request, *args, **kwargs):
        self.query = request.GET.get('serial_number', None)
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        qs = super().get_queryset()
        qs.filter(serial_number=self.query)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.query
        return context


class StudentDetailView(LoginRequiredMixin, DetailView):
    template_name = 'app/student-detail.html'
    model = Student
    context_object_name = 'student'

    # def get_context_data(self, **kwargs):
    #     ctx = super().get_context_data(**kwargs)
    #     obj = self.get_object()
    #     documents = [*obj.documents.all(), *obj.admissions.all()]
    #     ctx['documents'] = documents
    #     print(documents)
    #     return ctx

    def get_object(self):
        uid = self.kwargs.get('uid')
        print(uid)
        return get_object_or_404(
            self.model,
            uid=uid
        )


class CourseStudyDetail(LoginRequiredMixin, ListView):
    template_name = 'app/course_study-detail.html'
    context_object_name = 'students'
    paginate_by = 50

    def get_object(self):
        return get_object_or_404(CourseOfStudy, pk=self.kwargs.get('pk'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Liste des étudiants en {}'.format(
            self.get_object().name)
        return context

    def get_queryset(self):
        course = self.get_object()
        # file =
        return course.students.all()


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


# class CourseOfStudyDetailView(
#         LoginRequiredMixin,
#         DetailView):
#     template_name = 'course_study-list.html'
#     model = CourseOfStudy
#     context_object_name = 'course_of_study'

#     def get_context_data(self, **kwargs):
#         ctx = super().get_context_data(**kwargs)
#         course_of_study_choice = self.get_object().name
#         ctx['students'] = Student.objects.filter(
#             Q(course_of_study_first_choice=course_of_study_choice))
#         return ctx


class DocumentCreateView(
        LoginRequiredMixin,
        SuccessMessageMixin,
        CreateView):
    form_class = DocumentModelForm
    template_name = 'app/document-form.html'
    success_message = 'Document(s) ajouté(s)'

    # def post(self, request, *args, **kwargs):
    #     fiels

    def form_valid(self, form):
        doc = form.save(commit=False)
        doc.student = get_object_or_404(
            Student, uid=self.kwargs.get('uid'))
        file_str = str(doc.file)
        file_splited = file_str.split('.')
        doc.file_name = file_splited[0]
        print(file_splited[0])
        doc.ext = file_splited[1]
        doc.save()

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
    success_message = 'Fiche d\'inscription ajoutée avec succès !'

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

        student = self.get_concern_object()
        obj.student = student
        obj.save()

        student.course_of_study = obj.course_of_study
        student.save()

        return super().form_valid(form)

    def get_success_url(self):
        return self.get_concern_object().get_absolute_url()


class VerbalProcesCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = VerbalProcesModelForm
    template_name = 'app/verbal_proces-form.html'
    success_url = reverse_lazy('home')
    success_message = 'Procès verbal ajouté avec succès !'

    def form_valid(self, form):
        v_proces = form.save()

        with open(settings.BASE_DIR + v_proces.student_list.url, 'r') as json_proces:
            json_data = json_proces.read()
            dict_data = json.loads(json_data)
            serial_list = dict_data.get('matricules')

            fail_serials = []

            for serial in serial_list:
                try:
                    student = Student.objects.get(serial_number=serial)
                    student.verbal_proces.add(v_proces)
                    student.save()
                except:
                    fail_serials.append(serial)

            if fail_serials:
                return render(
                    self.request,
                    'app/fail_serials.html',
                    {'serials': fail_serials})

        return super().form_valid(form)


class VerbalProcesListView(LoginRequiredMixin, ListView):
    template_name = 'app/verbal_proces-list.html'
    model = VerbalProces
    context_object_name = 'verbal_process'
    