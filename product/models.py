# Create your models here.
from distutils.command.upload import upload
from django.db import models
from datetime import date
from blog.models import BlogStatistic
from accounts.models import customer
from core.models import TimeStampedModel

from django.utils.text import slugify

class brand (TimeStampedModel, models.Model):
    brand = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return f'{self.brand} - {self.created_at}'


class discount(TimeStampedModel, models.Model):
    name = models.CharField(max_length=255, unique=True)
    desc = models.CharField(max_length=255)
    disc_is_percent = models.BooleanField(default=True)
    disc_amount = models.IntegerField()

    def __str__(self) -> str:
        if self.disc_is_percent == True:
            return f'{self.name} - {self.disc_amount}%'
        else:
            return f'{self.name} - {self.disc_amount}AZN'


class designer (models.Model):
    designer = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        return self.designer
   




class productCategory(TimeStampedModel):
    category_name = models.CharField(max_length=255, unique=True)


    def __str__(self):
        return self.category_name
    class Meta:
        verbose_name_plural = 'productCategories'


class product (TimeStampedModel, models.Model):
    category = models.ForeignKey(productCategory, on_delete=models.CASCADE)
    small_desc = models.TextField()
    large_desc = models.TextField()
    brand = models.ForeignKey(brand, on_delete=models.CASCADE, blank=True)


class product_version (TimeStampedModel, models.Model):
    title = models.CharField(max_length=50, default='')
    product = models.ForeignKey(product, on_delete=models.CASCADE, default=True)
    code = models.IntegerField()
    price = models.FloatField()
    quantity = models.PositiveIntegerField(default=0)
    discount = models.ForeignKey(discount, on_delete=models.CASCADE, blank=True, null=True, default=None)
    designer= models.ForeignKey(designer, on_delete=models.CASCADE, default=True)
    slug = models.SlugField(null=True, blank=True, unique=True)

    def __str__(self):
        return self.title


class Image(models.Model):
    img = models.ImageField(upload_to = 'product_images')
    product = models.ForeignKey(product_version, related_name='images',  on_delete=models.CASCADE )
    is_main = models.BooleanField (default = False )


    def __str__(self):
        return f'Image of {self.product.title}'



class rating (models.Model):
    point = models.IntegerField()


class review(TimeStampedModel, models.Model):
    review_text = models.TextField()
    customer = models.ForeignKey(customer, on_delete=models.CASCADE)
    email = models.EmailField()
    product_version = models.ForeignKey(product_version, on_delete=models.CASCADE, null=True)
    rating = models.ForeignKey(rating, on_delete=models.CASCADE)

    


class Property(models.Model):
    title = models.CharField(max_length=50)


    class Meta:
        verbose_name_plural = 'Properties'
    def __str__(self):
        return self.title




class PropertyValue(models.Model):
    title = models.CharField(max_length=50)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)

    def __str__(self):
        return self.title



class ProductPropertyValue(models.Model):
    property_value = models.ForeignKey(PropertyValue, on_delete=models.CASCADE)
    product = models.ForeignKey(product_version, on_delete=models.CASCADE)

  


