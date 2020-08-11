from django.views.generic import TemplateView
from django.contrib import admin
from django.urls import path, include
from archives.views import HomeTemplateView

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
    path('app/', include('app.urls', namespace='app')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('admin/', admin.site.urls),
]
