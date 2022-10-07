# Create your models here.
from distutils.command.upload import upload
import email
from email.policy import default
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
   

class color(models.Model):
    color = models.CharField(max_length=100, unique=True)
    def __str__(self) -> str:
        return self.color


class productCategory(TimeStampedModel, models.Model):
    category_name = models.CharField(max_length=255, unique=True)
    # quantity = models.PositiveIntegerField(null=True)


    def __str__(self):
        return self.category_name
    #Meselen bizde admin panelde modelin adini  'productCategorys' olaraq gosterecek, amma bu duz deyil, duzeltmek ucun bu cur yaziriq:
    class Meta:
        verbose_name_plural = 'productCategories'


class product (TimeStampedModel, models.Model):
    category = models.ForeignKey(productCategory, on_delete=models.CASCADE)
    small_desc = models.TextField()
    large_desc = models.TextField()
    brand = models.ForeignKey(brand, on_delete=models.CASCADE, blank=True)
    # def save(self, *args, **kwargs):
    #     for categoryy in productCategory:
    #         if self.category == categoryy:
    #             categoryy['quantity'] += 1
    #             super(product, self).save(*args, **kwargs)




class product_version (TimeStampedModel, models.Model):
    title = models.CharField(max_length=50, default='')
    cover_image = models.ImageField( default='', upload_to ='product_cover_images' )
    product = models.ForeignKey(product, on_delete=models.CASCADE, default=True)
    code = models.IntegerField()
    price = models.FloatField()
    quantity = models.PositiveIntegerField(default=0)
    discount = models.ForeignKey(discount, on_delete=models.CASCADE, blank=True, null=True, default=None)
    designer= models.ForeignKey(designer, on_delete=models.CASCADE, default=True)
    color = models.ForeignKey(color, on_delete=models.CASCADE)
    slug = models.SlugField(null=True, blank=True, unique=True)

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(f'{self.color.color}-{self.title}- {self.code}' )
    #     super(product_version, self ).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Image(models.Model):
    img = models.ImageField(upload_to = 'product_images')
    product = models.ForeignKey(product_version, related_name='images',  on_delete=models.CASCADE )


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

    



