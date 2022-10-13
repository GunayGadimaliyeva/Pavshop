from django.contrib import admin

# Register your models here.

from .models import *



admin.site.register(brand)
admin.site.register(discount)
admin.site.register(designer)
admin.site.register(product)
admin.site.register(Image)
admin.site.register(Property)
admin.site.register(PropertyValue)
admin.site.register(ProductPropertyValue)

from modeltranslation.admin import TranslationAdmin

class ProductCategoryAdmin(TranslationAdmin):
    pass

admin.site.register(productCategory, ProductCategoryAdmin)




admin.site.register(review)




from django.contrib.admin import SimpleListFilter

class discountFilter(SimpleListFilter):
    title= "Filter by discount"
    parameter_name= 'discount_id'

    def lookups(self, request, model_admin):
        return (
            ('has_discount', 'has_discount'),
            ('no_discount','no_discount')
        )
    def queryset(self, request, queryset):
        if not self.value():
            return queryset
        if self.value().lower() =='has_discount':
            return queryset.exclude(discount_id__isnull =True)
        if self.value().lower() == 'no_discount':
            return queryset.filter (discount_id__isnull=True )
        

@admin.register(product_version)
class productAdmin(admin.ModelAdmin):
    list_filter = [discountFilter]
