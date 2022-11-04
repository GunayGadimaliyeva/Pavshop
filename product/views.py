from django.shortcuts import render, redirect
from .models import Brand, Product_version, ProductCategory, ProductPropertyValue, Image, Product
from django.views.generic import ListView, DetailView
# Create your views here.
from django.db.models import Count
from django.http import Http404
from django.contrib import messages
# from rest_framework import generics

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
    model = Product_version
    template_name = 'product-detail.html'
    context_object_name = 'product'

    
    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
            context = self.get_context_data(object=self.object)
            # context['colorproperties']  = ProductPropertyValue.objects.all().filter(product__id =context['product'].id)
            # # print(context['product'].id)
            # print((context['colorproperties']))
            context['images'] = Image.objects.all().filter(product__id =context['product'].id).filter(is_main=False)
            context['relatedimg'] = Image.objects.filter(is_main=True)
            # context['related'] = product.objects.filter(category__id = context['product'].Product.category.id)
            context['related'] = Product_version.objects.filter(product__category__id = context['product'].product.category.id).exclude(id=context['product'].id)[:4]
            # print(context['product'].Product.category.id)

            return self.render_to_response(context)
            
        except Http404:
            messages.warning(request, "There aren't any product for your searching!")
            return redirect('/')

            
# def product_list_view(request):
#     products = Product_version.objects.all()
#     return render(request, 'product-list.html', {'products': products})

class ProductList(ListView):
    model = Product_version
    template_name = "product-list.html"
    context_object_name= 'products'
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = ProductCategory.objects.all()
        context['brands'] = Brand.objects.all()
        context['images'] = Image.objects.filter(is_main=True)
        return context
    
    def get_queryset(self):
        category_name = self.request.GET.get('category')
        if category_name:
            queryset = Product_version.objects.filter(product__category__category_name=category_name)
        else:
            queryset = Product_version.objects.all()
        return queryset






        