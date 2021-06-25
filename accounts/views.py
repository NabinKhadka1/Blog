from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls.base import reverse_lazy
from django.views.generic.edit import CreateView



# Create your views here.
class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')
    
