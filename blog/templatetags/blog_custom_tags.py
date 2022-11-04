from django.template.defaulttags import register
from blog.models import BlogCategory



@register.simple_tag
def get_categories():
    return BlogCategory.objects.all()


