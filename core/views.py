from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages
from django.views.generic import View, CreateView, TemplateView
from django.http import request
from .models import Team, Sponsor


class Homeview(View):
    def get(self,request):
        return render(request, 'index.html', {})
    

class about(TemplateView):
    template_name = 'about-us.html'
   
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['members'] = Team.objects.all()
        context['sponsors'] = Sponsor.objects.all()
        return context

class contact(CreateView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = '/contact'
    
