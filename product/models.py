from distutils.command.upload import upload
from django.db import models
from datetime import date
from blog.models import BlogStatistic
from core.models import TimeStampedModel
from django.contrib.auth import get_user_model
User = get_user_model()
from django.utils.text import slugify

class Brand (TimeStampedModel, models.Model):
    brand = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return f'{self.brand} - {self.created_at}'


class Discount(TimeStampedModel, models.Model):
    name = models.CharField(max_length=255, unique=True)
    desc = models.CharField(max_length=255)
    disc_is_percent = models.BooleanField(default=True)
    disc_amount = models.IntegerField()

    def __str__(self) -> str:
        if self.disc_is_percent == True:
            return f'{self.name} - {self.disc_amount}%'
        else:
            return f'{self.name} - {self.disc_amount}AZN'


class Designer (models.Model):
    designer = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        return self.designer
   

class ProductCategory(TimeStampedModel):
    category_name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.category_name
    class Meta:
        verbose_name_plural = 'productCategories'


class Product (TimeStampedModel, models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, related_name = 'categor')
    small_desc = models.TextField()
    large_desc = models.TextField()
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, blank=True)


class Product_version (TimeStampedModel, models.Model):
    title = models.CharField(max_length=50, default='')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=True)
    code = models.IntegerField()
    price = models.FloatField()
    quantity = models.PositiveIntegerField(default=0)
    discount = models.ForeignKey(Discount, on_delete=models.CASCADE, blank=True, null=True, default=None)
    designer= models.ForeignKey(Designer, on_delete=models.CASCADE, default=True)
    slug = models.SlugField(null=True, blank=True, unique=True)

    def __str__(self):
        return self.title


class Image(models.Model):
    img = models.ImageField(upload_to = 'product_images')
    product = models.ForeignKey(Product_version, related_name='images',  on_delete=models.CASCADE )
    is_main = models.BooleanField (default = False )

    def __str__(self):
        return f'Image of {self.product.title}'


class Rating (models.Model):
    point = models.IntegerField()


class Review(TimeStampedModel, models.Model):
    review_text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    email = models.EmailField()
    product_version = models.ForeignKey(Product_version, on_delete=models.CASCADE, null=True)
    rating = models.ForeignKey(Rating, on_delete=models.CASCADE, default=1)



class Property(models.Model):
    title = models.CharField(max_length=50)
    category = models.ForeignKey(ProductCategory, on_delete = models.CASCADE)

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
    product = models.ForeignKey(Product_version, on_delete=models.CASCADE)


class Wishlist(models.Model):
    product_version = models.ForeignKey(Product_version, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.product_version} is liked by {self.user}'