from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Blog, BlogStatistic

@receiver(post_save ,sender=Blog)
def post_save_func(sender, instance, *args, **kwargs):
    BlogStatistic.objects.create( blog = instance )