from django.urls import path
from .views import ListCreateProductView, ProductDetailView

urlpatterns = [
    path('products/', ListCreateProductView.as_view()),
    path('products/<int:pk>', ProductDetailView.as_view())

]
