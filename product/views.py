import imp
from django.shortcuts import render, redirect
from .models import brand, product_version, Image, productCategory
from django.views.generic import ListView, DetailView
# Create your views here.
from django.db.models import Count
from django.http import Http404
from django.contrib import messages


# def product_detail_view(request, slug):
#     product = product_version.objects.get(slug=slug)
#     images = Image.objects.all()
#     # print(request.COOKIES)
#     # print(request.session.keys())
#     # Note: Bu cur deyishsek private mode olan iIncognito tabinda da acilacaq :
#     # request.session['name'] = 'Gunay'
#     # print(request.session['name'])
#     # request.session['_auth_user_id']
#     # print(request.session['_auth_user_id'])
#     # print(request.session['_auth_user_backend'])
#     # print(request.session['_auth_user_hash'])
#     return render(request, 'product-detail.html', {'product': product,'images': images})


class ProductDetail(DetailView):
    model = product_version
    template_name = 'product-detail.html'
    context_object_name = 'product'

    
    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
            context = self.get_context_data(object=self.object)
            return self.render_to_response(context)
        except Http404:
            messages.warning(request, "There aren't any product for your searching!")
            return redirect('/')

            
# def product_list_view(request):
#     products = product_version.objects.all()
#     return render(request, 'product-list.html', {'products': products})

class ProductList(ListView):
    model = product_version
    template_name = "product-list.html"
    context_object_name= 'products'
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = productCategory.objects.all()
        context['brands'] = brand.objects.all()
        return context
    
    def get_queryset(self):
        category_name = self.request.GET.get('category')
        if category_name:
            queryset = product_version.objects.filter(product__category__category_name=category_name)
        else:
            queryset = product_version.objects.all()
        return queryset




        