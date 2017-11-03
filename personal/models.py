from django.db import models
# Create your models here.
class Post(models.Model):
    product = models.CharField(max_length = 250) 
    slug=models.SlugField(max_length = 250,unique=True)      
    def __str__(self):
        return self.product
