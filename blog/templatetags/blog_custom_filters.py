from django.template.defaulttags import register
from blog.models import Blog


@register.filter
def count(category):
    return Blog.objects.filter(category__id = category.id ).count()
