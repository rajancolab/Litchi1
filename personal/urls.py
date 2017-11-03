from django.conf.urls import url 
from . import views
from .models import Post
from django.contrib.auth.decorators import login_required

urlpatterns =[
	url(r'^$',views.index,name='index'),
	url(r'^allcategories',login_required(views.list_of_posts),name='list_of_posts'),

]