from django.contrib import admin

# Register your models here.
from .models import *

# admin.site.register(blog)
admin.site.register(tag)
admin.site.register(comment)
admin.site.register(image)
admin.site.register(BlogStatistic)
admin.site.register(BlogCategory)


# yaxud:
# admin.site.register([blog,tag,comments,images])
from django.contrib.admin import SimpleListFilter

class TagFilter(SimpleListFilter):
    title = 'Tags Filter'
    parameter_name = 'blogTag'  #bu parametr filteri qurdugumuz modelin fieldlerden biri olmalidir.
    def lookups(self, request, model_admin):
        return (
           ( 'has_tag', 'has_tag'),
           ( 'no_tag', 'no_tag')

        )
    def queryset(self, request, queryset) :
        if not self.value():
            return queryset
        if self.value().lower() == 'has_tag':
            return queryset.exclude(blogTag__isnull=True)  #burdaki tag_blog parametrde yazdigimizdir.
        if self.value().lower() == 'no_tag':
            return queryset.exclude(blogTag__isnull=False)

@admin.register(blog)
class blogAdmin(admin.ModelAdmin):
    list_filter=["created_at",TagFilter]


