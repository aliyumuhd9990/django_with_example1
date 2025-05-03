from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

app_name = 'account'

# Create your views here.
class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('account:login')

@login_required
def LogoutView(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('pages:home')

