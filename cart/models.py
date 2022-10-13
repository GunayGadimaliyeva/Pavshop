from django.db import models
from product.models import product_version
from accounts.models import Country, customer
from django.contrib import admin
from django.utils.html import format_html
from core.models import TimeStampedModel

class basket_item(TimeStampedModel, models.Model):
    product_version = models.ForeignKey(product_version, on_delete=models.CASCADE, null=True)
    quantity = models.PositiveIntegerField(default=0)
    total_price = models.FloatField()
    customer = models.ForeignKey(customer, on_delete=models.CASCADE)

    

class promocode (TimeStampedModel, models.Model):
    promocode = models.CharField(max_length=8)
    is_active = models.BooleanField(default=True)
    is_percent = models.BooleanField(default=True)
    discount = models.IntegerField()

    def __str__(self):
        return f'{self.promocode}--created at: {self.created_at}'

class basket(TimeStampedModel,models.Model):
    basket_item = models.ForeignKey( basket_item ,on_delete=models.CASCADE) 
    promocode = models.ForeignKey(promocode, on_delete=models.CASCADE)
    total_price = models.FloatField()


class cart (TimeStampedModel, models.Model):
    cart_number = models.IntegerField()
    cvv_code = models.CharField(max_length=3)
    expiration_date = models.DateField()
    customer= models.ForeignKey(customer, on_delete=models.CASCADE)
    

    @admin.display(description="Customer's  phone number")
    def display_customer_phone(self):
        return format_html(f'<font color="red">{ self.customer_id.phone}</font>')


    def __str__(self) :
        return f'{self.cart_number} - {self.expiration_date}'



class ShippingBillingInfo(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255) 
    town = models.CharField(max_length=150)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True, blank=True)
    email = models.EmailField()
    phone = models.IntegerField()

    class Meta:
        abstract=True



 
class billing_detail (ShippingBillingInfo, TimeStampedModel, models.Model):
    choices =((1, 'Ship to a different address'),) 
    Ship_to_a_different_address = models.BooleanField(choices=choices,  default=False, null=True)

class shipping_info (ShippingBillingInfo, TimeStampedModel, models.Model):
    billing_info = models.ForeignKey(billing_detail, on_delete=models.CASCADE, null=True, blank=True)
    


class payment_method (TimeStampedModel, models.Model):
    method = models.CharField(max_length=100)
    desc = models.CharField(max_length=255)

    