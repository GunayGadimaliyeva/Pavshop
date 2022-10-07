from django import template
from accounts.models import User
register = template.Library()
from product.models import product_version

@register.filter('test_filter')
def test_filter_funct(value, arg):
    return f'{value}{arg}'

@register.simple_tag(name='simple_tag')
def simple_tag_funct(arg1):
    return User.objects.all().count()+arg1


@register.inclusion_tag( filename='show_latest_products.html')
def show_latest_products( ):
    latest_products = product_version.objects.all()
    print(latest_products)
    return {
        'latest_products': latest_products
    }