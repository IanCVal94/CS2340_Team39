from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from django.shortcuts import redirect
from django.contrib.auth import logout

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'registration/profile.html'

def LogoutView(request):
    logout(request)
    return redirect('home')