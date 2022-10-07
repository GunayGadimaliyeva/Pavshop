from django.contrib import admin
from .models import *
from django.contrib.admin import SimpleListFilter
from django.utils.safestring import mark_safe

# Register your models here.
#modellerimizi her appin oz admin.py inda bu cur register edirik ki, admin panelimizde gorunsun:
admin.site.register([basket_item, promocode,basket, shipping_info, billing_detail, payment_method])


class CardNumberFilter(SimpleListFilter):
    title = 'CardNumber Filter'
    parameter_name = 'mailll'
    def lookups(self, request, model_admin):
        return (
           ( 'has_mail', 'has_mail'),  #burdaki ikinci terefdeki yazdiqlarimiz admin panelde gorunendir.
           ( 'no_mail', 'no_mail')
        )
    def queryset(self, request, queryset) :
        if not self.value():
            return queryset
        if self.value().lower() == 'has_mail':     #burdaki has_mail yuxarida lookupsda yazdigimiz birinci terefdeki has_maildir.
            return queryset.exclude(mail='')
        if self.value().lower() == 'no_mail':
            return queryset.filter(mail='')


@admin.register(cart)
class CartAdmin(admin.ModelAdmin):
    list_display= ['id','cart_number', 'cvv_code', 'customer','display1_customer_phone', '__str__' , ]  
    list_filter= ['cart_number', 'cvv_code', CardNumberFilter]
    search_fields = ['cart_number', 'cvv_code', 'customer__first_name']
    list_editable= [ 'cvv_code', 'customer',  ] 
    list_max_show_all = 10
    list_per_page = 2
    # readonly_fields=['created_at']
    # fields=['cvv_code', 'expiration_date']
    # Yaxud fields-i bele de yaza bilerik ki, expiration_date ve  cart_number bir setirde gorunsun : 
    # fields=['cvv_code', ('expiration_date', 'cart_number')]
    fieldsets=[
        ("Cart details", {
            'fields':(
                "cart_number", 'cvv_code'
            )
        }),
        ('Cart Date info',{
            'fields':('expiration_date',
            )
        }),
        ('Customer info',{
            'fields':('customer',
            )
        })
    ]  
    # NOTE: Bunun==>admin.site.register(cart, CartAdmin) evezine yuxarida @admin.register(cart) decoratorunu da yazsaq ishleyecek. 
    # admin.site.register(cart, CartAdmin) 

    #Models.py da Cart modelinin altinda yazdigimizi burda bu cur de yaza bilerik, sadece burada funksiya self ve obj qebul edir, self-burada CartAdmin classina uygun gelir.
    @admin.display(description='Additional column')
    def display1_customer_phone(self, obj):
        return format_html('<font color="red">{}</font>', obj.customer.phone )   #bu format_html-dir.
        # return f'<font color="red">{ obj.customer_id.phone}'                      #bele de yaza bilerik , bu f stringdir.
        
        ##NOTE:  mark safe ile bele yaza bilerdik: 
        # msg = format_html('<font color="red">{}</font>', obj.customer_id.phone )
        # msg+='</font>'
        # return mark_safe(msg)




admin.site.site_title= "Pavshopun admin paneli"
admin.site.site_header= "Pavshop's admin panel"
admin.site.index_title= "Pavshop's site administration"




