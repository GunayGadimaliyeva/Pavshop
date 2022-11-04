from django.contrib import admin

# Register your models here.
from django.contrib.auth import get_user_model
from .models import Country, SubscriberEmail

User = get_user_model()
admin.site.register(User)
admin.site.register(Country)
admin.site.register(SubscriberEmail)

