from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import *

# admin.site.register(blog)
admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(Image)
admin.site.register(BlogStatistic)
admin.site.register(BlogCategory)


# for modeltranslation:
class BlogsTranslationAdmin(TranslationAdmin):
    pass


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

class ImageInlineAdmin(admin.TabularInline):
    model = Image

@admin.register(Blog)
class blogAdmin(admin.ModelAdmin):
    list_filter=["created_at",TagFilter]
    inlines = (ImageInlineAdmin,)





