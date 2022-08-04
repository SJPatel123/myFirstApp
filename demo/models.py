from django.db import models
from django.utils.text import slugify
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Category(models.Model):
    category_id=models.AutoField(unique=True,primary_key=True)
    category_name=models.CharField(max_length=100)
    slug=models.SlugField(unique=True,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active=models.BooleanField(default=True)
    def __str__(self) -> str:
        return str(self.category_name)
    
    def save(self,*args,**kwargs):
        self.slug=slugify(self.slug)
        super(Category,self).save(*args,**kwargs)

@receiver(post_save,sender=Category)
def create_slug(sender,instance,created,**kwargs):
    if created:
        instance.slug=instance.category_name
        instance.save()

class Tag(models.Model):
    tag_id=models.AutoField(unique=True,primary_key=True)
    tag_name=models.CharField(max_length=100)
    slug=models.SlugField(unique=True,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active=models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.tag_name
    def save(self,*args,**kwargs):
        self.slug=slugify(self.slug)
        super(Tag,self).save(*args,**kwargs)

@receiver(post_save,sender=Tag)
def create_slug(sender,instance,created,**kwargs):
    if created:
        instance.slug=instance.tag_name
        instance.save()

class Blog(models.Model):
    blog_id = models.AutoField(unique=True, primary_key=True)
    blog_title = models.CharField(max_length=100)
    blog_description=models.CharField(max_length=500)
    blog_image=models.ImageField(upload_to="documents")
    blog_tag=models.ForeignKey(Tag,on_delete=models.CASCADE,default=None)
    blog_category=models.ForeignKey(Category,on_delete=models.CASCADE,default=None)
    def __str__(self) -> str:
        return str(self.blog_title)