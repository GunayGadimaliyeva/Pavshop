from django.contrib import admin

from .models import *

admin.site.register(tag)
admin.site.register(comment)
admin.site.register(image)
admin.site.register(BlogStatistic)
admin.site.register(BlogCategory)



# for modeltranslation:
from modeltranslation.admin import TranslationAdmin
class BlogsAdmin(TranslationAdmin):
    pass


from django.contrib.admin import SimpleListFilter

class TagFilter(SimpleListFilter):
    title = 'Tags Filter'
    parameter_name = 'blogTag' 
    def lookups(self, request, model_admin):
        return (
           ( 'has_tag', 'has_tag'),
           ( 'no_tag', 'no_tag')

        )
    def queryset(self, request, queryset) :
        if not self.value():
            return queryset
        if self.value().lower() == 'has_tag':
            return queryset.exclude(blogTag__isnull=True)  
        if self.value().lower() == 'no_tag':
            return queryset.exclude(blogTag__isnull=False)

class blogAdmin(admin.ModelAdmin):
    list_filter=["created_at",TagFilter]

admin.site.register(blog, BlogsAdmin)

