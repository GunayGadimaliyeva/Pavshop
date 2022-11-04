from dataclasses import fields
from rest_framework import serializers
from product.models import Product_version


class ProductListCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product_version
        fields = ('title', 'product', 'code', 'price','discount', 'designer',)

class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product_version
        fields = ('title', 'product', 'designer',)