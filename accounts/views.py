from django.shortcuts import render
from django.contrib.auth.views import (
     LoginView as BaseLoginView, 
     LogoutView as BaseLogoutView

)

class LoginView(BaseLoginView):
    template_name = 'accounts/login.html'

# class LogoutView(BaseLogoutView):
#     def get(self, )