from django.template.defaulttags import register
from product.models import Product

@register.filter
def get_range(value):
    return range(1, value+1)

@register.filter
def count(category):
    return Product.objects.filter(category__id = category.id ).count()



    