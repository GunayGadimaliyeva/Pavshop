from django.contrib import admin

# Register your models here.

from .models import *
admin.site.register(adress)
admin.site.register(contanct_info)
admin.site.register(ContactMessage)
admin.site.register(Team)
admin.site.register(Sponsor)