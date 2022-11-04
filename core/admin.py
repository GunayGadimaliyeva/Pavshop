from django.contrib import admin

# Register your models here.

from .models import *
admin.site.register(Adress)
admin.site.register(Contanct_info)
admin.site.register(ContactMessage)
admin.site.register(Team)
admin.site.register(Sponsor)