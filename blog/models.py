from email.policy import default
from statistics import mode
from django.db import models
# from django.contrib.auth.models import User
from accounts.models import customer
from core.models import TimeStampedModel
from django.contrib.auth import get_user_model
User = get_user_model()
from django.utils.text import slugify
from datetime import datetime
class tag (models.Model):
    tag_title = models.TextField()
    
    def __str__(self) -> str:
        return f'Tag:  {self.tag_title}'


class BlogCategory(TimeStampedModel, models.Model):
    title = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'BlogCategories'


class blog (TimeStampedModel, models.Model):
    blog_title = models.CharField(max_length=255)
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    desc = models.TextField()
    history = models.TextField()
    blogTag = models.ManyToManyField(tag, blank=True)
    slug = models.SlugField(null=True, blank=True, unique=True)
    category = models.ForeignKey(BlogCategory, on_delete = models.CASCADE, null=True)


    def soft_delete(self):
        self.is_deleted = True
        self.deleted_at = datetime.now()
        self.save() 
    
    def hard_delete(self):
        super(blog, self).delete()

    def __str__(self) -> str:
        # print(blog.objects.filter(tag_blog__id = self.id))
        return f' Blog by {self.blog_title}'
        
    def save(self, *args, **kwargs):
        self.slug = slugify(self.blog_title)
        super(blog, self ).save(*args, **kwargs)

class image (models.Model):
    img = models.ImageField(upload_to = 'blog_images')
    blog =  models.ForeignKey(blog, on_delete=models.CASCADE, default=True, null=True)


# class blog_tag_relation (models.Model):
#     blog_id = models.ForeignKey(blogs, on_delete=models.CASCADE)
#     tag_id = models.ForeignKey(tags, on_delete=models.CASCADE)


class comment (TimeStampedModel, models.Model):
    subject = models.TextField()
    desc = models.TextField()
    customer = models.ForeignKey(customer, on_delete=models.CASCADE, null=True)
    blog= models.ForeignKey(blog, related_name='comments',  on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return f' Comment by  {self.customer_id}'
# comments.objects.create(subject = "I read the blog...", desc="It's amazing", customer_id=customer.objects.get(id=1), blog_id=blog.objects.get(id=1))

class BlogStatistic(models.Model):
    blog = models.ForeignKey(blog, on_delete=models.CASCADE, null=True)
    comment_count =  models.PositiveIntegerField(default=0)


    def __str__(self) -> str:
        return f'{self.blog} - stats'











