from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login, logout , get_user_model
from django.contrib import messages
User = get_user_model()
from django.views.generic import CreateView, View
from django.urls import reverse_lazy
from django.http import request
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import gettext as _





class loginView(View):
    form_class = LoginForm
    template_name = 'login.html'
    success_url = '/'

    def get(self, request):
        form = self.form_class
        return render (request, self.template_name, {'form': form,})

    def post(self,request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            if user := authenticate(username=username, password=password):
                messages.success(request,f'You are logged in as {username}')
                login(request, user)
                return redirect('/')
        else:
            messages.error(request, _('Included information is false! Please enter write username and password!'))
            return render(request, 'login.html', {'form': form})
    

class register(CreateView):
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

   
class Logout(LoginRequiredMixin ,View):
    def get(self, request):
        logout(request)
        return redirect('login')

