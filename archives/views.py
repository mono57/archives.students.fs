from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from app.models import *


class HomeTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recent_documents'] = []
        context['recent_students'] = Student.objects.get_recents()
        context['verbal_proces'] = VerbalProces.objects.all()
        return context