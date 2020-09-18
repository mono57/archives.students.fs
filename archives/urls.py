from django.views.generic import TemplateView
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from archives.views import HomeTemplateView

admin.site.site_header = "SGCA-FS Admin"
admin.site.site_title = "SGCA-FS Portail"
admin.site.index_title = "Bienvenue sur SGCA-FS"

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
    path('app/', include('app.urls', namespace='app')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
