from django.db import models
from product.models import Product_version, ProductPropertyValue
from accounts.models import Country
from core.models import TimeStampedModel
from django.contrib import admin
from django.utils.html import format_html
from django.contrib.auth import get_user_model
User = get_user_model()



class Promocode (TimeStampedModel, models.Model):
    promocode = models.CharField(max_length=8)
    is_active = models.BooleanField(default=True)
    is_percent = models.BooleanField(default=True)
    discount = models.IntegerField()

    def __str__(self):
        return f'{self.promocode}--created at: {self.created_at}'


class Basket(TimeStampedModel,models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, null=True)
    # promocode = models.ForeignKey(promocode, on_delete=models.CASCADE)
    # total_price = models.FloatField()

class Basket_item(TimeStampedModel, models.Model):
    product_version = models.ForeignKey(Product_version, on_delete=models.CASCADE, null=True)
    quantity = models.PositiveIntegerField(default=0)
    property = models.ForeignKey(ProductPropertyValue, on_delete =models.CASCADE, null=True)
    basket = models.ForeignKey(Basket, on_delete = models.CASCADE, null = True)
    price = models.FloatField()
    # customer = models.ForeignKey(customer, on_delete=models.CASCADE)

    # def __str__(self) -> str:
    #     return f'{self.quantity}--> created_at: {self.created_at}'



class Cart (TimeStampedModel, models.Model):
    cart_number = models.IntegerField()
    cvv_code = models.CharField(max_length=3)
    expiration_date = models.DateField()
    user= models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    

    #Bu cur  yazaraq biz foreign keyde verdiyimizin diger valuelerine cata bilerik, ve daha sonra hemin valueni admin.py da qeyd ederek admin panelde modelimizde elave field olaraq gostere bilerik ; Eger decoratoru yazmasaq==> admin panelde modelimiz ucun yaratdigi elave columna bashligi funksiyamiza uygun olaraq verecekdir (yeni, display_customer_phone), amma decoratoru yazsaq hemin columna adi descriptionda yazdigimizi verecek(yeni "Customer's  phone number"):
    @admin.display(description="Customer's  phone number")
    def display_customer_phone(self):
        return format_html(f'<font color="red">{ self.user_id.phone}</font>')

    # ============================================================================================================================

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



 
class Billing_detail (ShippingBillingInfo, TimeStampedModel, models.Model):
    choices =((1, 'Ship to a different address'),) 
    Ship_to_a_different_address = models.BooleanField(choices=choices,  default=False, null=True)

class Shipping_info (ShippingBillingInfo, TimeStampedModel, models.Model):
    billing_info = models.ForeignKey(Billing_detail, on_delete=models.CASCADE, null=True, blank=True)
    


class Payment_method (TimeStampedModel, models.Model):
    method = models.CharField(max_length=100)
    desc = models.CharField(max_length=255)

    
class OrderStatus(TimeStampedModel):
    is_ordered = models.BooleanField(default=False)
    is_shipped =  models.BooleanField(default=False)
    is_delivered = models.BooleanField(default=False)

class Order(TimeStampedModel):
    status = models.ForeignKey(OrderStatus, on_delete=models.CASCADE)
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE)
    total_price = models.FloatField()