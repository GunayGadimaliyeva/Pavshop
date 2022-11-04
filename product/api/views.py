from rest_framework import generics
from product.models import Product_version
from .serializers import ProductListCreateSerializer, ProductDetailSerializer

class ListCreateProductView(generics.ListCreateAPIView):
    queryset = Product_version.objects.all()
    serializer_class = ProductListCreateSerializer


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductDetailSerializer
    queryset = Product_version.objects.all()
