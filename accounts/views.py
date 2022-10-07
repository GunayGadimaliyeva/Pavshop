from distutils.log import Log
import imp
from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import get_user_model
User = get_user_model()
from django.views.generic import CreateView, View
from django.urls import reverse_lazy
from django.http import request
from django.contrib.auth.mixins import LoginRequiredMixin



# def login_view(request):
#     login_form = LoginForm()
#     user = User.objects.all().count()
#     if request.method == 'POST':
#         login_form = LoginForm(request.POST)
#         if login_form.is_valid():
#             username = request.POST['username']
#             password = request.POST['password']
#             if user := authenticate(username=username, password=password):
#                 messages.success(request,f'You are logged in as {username}')
#                 login(request, user)
#                 return redirect('/')
#             # else:
#             #     messages.add_message(request, messages.INFO, 'Included information is false! Please enter write username and password!')
    
#     else:
#         login_form = LoginForm()
#     return render(request, 'login.html', {'loginform': login_form, 'user': user})


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
            messages.error(request,'Included information is false! Please enter write username and password!')
            return render(request, 'login.html', {'form': form})
    
        

    
# def register_view(request):
#     form = RegisterForm()
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')
#     return render(request, 'register.html', {'form': form})


class register(CreateView):
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

    # def form_valid(self, form):
    #     form.instance.username = self.request.user
    #     # form.instance.save()
    #     return super().form_valid(form)



# @login_required()
# def logout_view(request):
#     logout(request)
#     return redirect('/')

class Logout(LoginRequiredMixin ,View):
    def get(self, request):
        logout(request)
        return redirect('login')

