from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from .models import product_version

@receiver(pre_save, sender=product_version)
def slug_func(sender, instance, *args, **kwargs ):
    instance.slug = slugify(f'{instance.title}- {instance.code}' )
