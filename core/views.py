from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages
from django.views.generic import View, CreateView, TemplateView
# from django.shortcuts import HttpResponse
from django.http import request
from .models import Team, Sponsor


class Homeview(View):
    def get(self,request):
        return render(request, 'index.html', {})
        # return HttpResponse('<h1>Your Name </h1>')
    

# def about_us_view(request):
#     return render(request, 'about-us.html')

class about(TemplateView):
    template_name = 'about-us.html'
   
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['members'] = Team.objects.all()
        context['sponsors'] = Sponsor.objects.all()
        return context
# def contact_view(request):
#     form = ContactForm()
#     if request.method=='POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             print('Muracietiniz qebul olundu !')
#             form.save()
#             messages.add_message(request, messages.INFO, 'Dear customer, your message is accepted ! Thank you so much! ')
#             # form = ContactForm()          #Bunu bele yazanda goruntu olaraq sehifede refresh olunur yeni doldurdugumuz datalar temizlenir amma biz sehifeye yeniden request atanda onun yaddashinda POST methodu qalir ve bizim datani yeniden gonderir db-a. Bunu duzeltmek ucun "redirect" methodundan istifade ede bilerik: 
#             return redirect('/contact')        #Burda yazdigimiz "/contact"---> contact viewmuzdaki namedir.

#         else:
#             print('Yeniden cehd edin ! ')
#             messages.warning(request, 'Melumatlarin dogrulugundan emin olun!')
#             return render(request, 'contact.html', {'form': form} )


    #     print(request.POST)
        # print(request.POST['message'])
        # print(request.POST.get('message'))
    # print(request.method)
    # return render(request, 'contact.html', {'form': form} )


class contact(CreateView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = '/contact'
    
