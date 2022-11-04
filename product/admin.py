from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from django.contrib.admin import SimpleListFilter
from .models import *

admin.site.register(Brand)
admin.site.register(Discount)
admin.site.register(Designer)
admin.site.register(Product)
admin.site.register(Image)
admin.site.register(Property)
admin.site.register(PropertyValue)
admin.site.register(ProductPropertyValue)
admin.site.register(Review)
admin.site.register(Wishlist)


class ProductCategoryAdmin(TranslationAdmin):
    pass

admin.site.register(ProductCategory, ProductCategoryAdmin)

class ImageInlineAdmin(admin.TabularInline):
    model = Image


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
        

@admin.register(Product_version)
class ProductVersionAdmin(admin.ModelAdmin):
    list_filter = [discountFilter]
    inlines = (ImageInlineAdmin,)   