from django.db import models
from django.core.urlresolvers import reverse
from personal.models import Post as Productpost


class Category(models.Model):
    name = models.CharField(max_length = 250)
    product=models.ForeignKey(Productpost)
    slug=models.SlugField(max_length = 250,unique=True)
    thumbnail=models.ImageField(upload_to='cartoons/images')
    date=models.DateField()
    seo_title = models.CharField(max_length = 250)
    seo_description = models.CharField(max_length = 160)
    class Meta:
        ordering=('-date',)
        verbose_name='category'
        verbose_name_plural='categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("cartoons:list_of_post_by_category", args=[self.slug])
    


class Post(models.Model):
    title = models.CharField(max_length = 140)
    category=models.ForeignKey(Category)
    slug=models.SlugField(max_length = 140)
    thumbnail=models.ImageField(upload_to='cartoons/images')
    date=models.DateField()
    video=models.FileField(upload_to='cartoons/videos')
    class Meta:
        ordering=('title',)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("cartoons:post_detail", args=[self.slug])
    
    

