from urllib import request
from django.views.generic import ListView
from django.shortcuts import render, redirect
from .forms import shippingForm, billingForm

# def cart_view(request):
#     return render (request, "shopping-cart.html")

class cart(ListView):
    template_name = 'shopping-cart.html'
    def get(self, request):
        return render(request, self.template_name)

def checkout_view(request):
    form = shippingForm()
    if request.method == 'POST':
        form = shippingForm(request.POST)
        if form.is_valid():
            print(form)
            form.save()
            return redirect('/check_out')
        else:
            return render(request, 'checkout.html', {'form': form})

    return render(request, 'checkout.html', {'form': form})