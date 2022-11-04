from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import AbstractUser
from core.models import TimeStampedModel

class Country (models.Model):
    country_name = models.CharField(max_length=100)
    country_code = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Countries"


    def __str__(self) -> str:
        return f'{self.country_name} - {self.country_code}'


class User(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    image = models.ImageField(upload_to = 'user_avatars', null=True)
    phone = models.IntegerField(null=True)
    address1 = models.CharField(max_length=255,null=True)
    address2 = models.CharField(max_length=255,null=True)
    town = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, default="", null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} --- {self.username}'


class SubscriberEmail(TimeStampedModel):
    email = models.EmailField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.email
