from django.urls import path
from django.views.generic import TemplateView
from app.views import (
    StudentCreateView,
    StudentDetailView,
    DocumentCreateView,
    AdmissionFileCreateView,
    StudentSearchListView,
    VerbalProcesCreateView
)

app_name = 'app'

urlpatterns = [
    path(
        'department/<int:pk_department>/course/<int:pk_course>/',
        TemplateView.as_view(template_name='app/course_study-list.html'),
        name='course_study_list'),
    path(
        'student/form/',
        StudentCreateView.as_view(),
        name='student-add'
    ),
    path(
        'student/<str:uid>/detail/',
        StudentDetailView.as_view(),
        name='student-detail'
    ),
    path(
        'student/<str:uid>/document/add/', 
        DocumentCreateView.as_view(),
        name='document-create'
    ),
    path(
        'student/<str:uid>/admisssion/form/',
        AdmissionFileCreateView.as_view(),
        name='admission-form'
    ),
    path(
        'student/search/', 
        StudentSearchListView.as_view(),
        name='search'),
    path(
        'proces/',
        VerbalProcesCreateView.as_view(),
        name='proces'
    )
    
]
