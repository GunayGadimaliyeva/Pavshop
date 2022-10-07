from django.urls import path
from .views import  ProductList, ProductDetail

urlpatterns=[ 
    path('product-detail/<slug:slug>', ProductDetail.as_view(), name = 'product_detail'),
    path('product-list/', ProductList.as_view(), name='product_list')
    ]
   
