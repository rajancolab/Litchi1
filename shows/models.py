from django.db import models
from django.core.urlresolvers import reverse



class Category(models.Model):
    name = models.CharField(max_length = 250)
    slug=models.SlugField(max_length = 250,unique=True)
    thumbnail=models.ImageField(upload_to='shows/images')
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
        return reverse("shows:list_of_post_by_category", args=[self.slug])
    


class Post(models.Model):
    title = models.CharField(max_length = 140)
    category=models.ForeignKey(Category)
    slug=models.SlugField(max_length = 140)
    thumbnail=models.ImageField(upload_to='shows/images')
    date=models.DateField()
    video=models.FileField(upload_to='shows/videos')
    class Meta:
        ordering=('title',)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("shows:post_detail", args=[self.slug])
    
    

