from django.conf.urls import url, include
from .models import Category,Post
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [ 
              url(r'^$',login_required(views.list_of_category),name='list_of_category'),
              url(r'^(?P<slug>[-\w]+)$',login_required(views.post_detail),name='post_detail'),
              url(r'^category/(?P<category_slug>[-\w]+)/$',login_required(views.list_of_post_by_category),name='list_of_post_by_category'),

            ]