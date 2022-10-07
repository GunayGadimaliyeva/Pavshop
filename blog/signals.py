from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import blog, BlogStatistic

@receiver(post_save ,sender=blog)
def post_save_func(sender, instance, *args, **kwargs):
    BlogStatistic.objects.create( blog = instance )