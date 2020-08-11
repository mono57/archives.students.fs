from django.urls import path
from django.contrib.auth.views import LogoutView
from accounts.views import LoginView

app_name = 'accounts'

urlpatterns = [
    path(
        'login/', 
        LoginView.as_view(),
        name='login'
    ),
    path(
        'logout/',
        LogoutView.as_view(),
        name='logout'
    ),
]
