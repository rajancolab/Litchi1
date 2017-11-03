from django.shortcuts import render
from cartoons.models import Category as cartoons_category
from news_and_politics.models import Category as news_category
from shows.models import Category as shows_category
from stand_up.models import Category as stand_up_category
from sports.models import Category as sports_category
from trending_movies.models import Category as trending_movies_category
from punjabi_movies.models import Category as punjabi_movies_category
from .models import Post

# Create your views here.
def index(request):
	return render(request,'personal/home.html')

def list_of_posts(request):
	post1=Post.objects.filter(slug='cartoons')
	post2=Post.objects.filter(slug='shows')
	post3=Post.objects.filter(slug='trending_movies')
	post4=Post.objects.filter(slug='news_and_politics')
	post5=Post.objects.filter(slug='stand_up')
	post6=Post.objects.filter(slug='sports')
	post7=Post.objects.filter(slug='punjabi_movies')
	news_cat=news_category.objects.all()
	cartoon_cat=cartoons_category.objects.all()
	shows_cat=shows_category.objects.all()
	stand_up_cat=stand_up_category.objects.all()
	sports_cat=sports_category.objects.all()
	trending_movies_cat=trending_movies_category.objects.all()
	punjabi_movies_cat=punjabi_movies_category.objects.all()
	template='personal/allcategories.html'
	context={'post1':post1,'post2':post2,'post3':post3,'post4':post4,'post5':post5,'post6':post6,'post7':post7,'news_cat':news_cat,'cartoon_cat':cartoon_cat,'shows_cat':shows_cat,'stand_up_cat':stand_up_cat,'sports_cat':sports_cat,'trending_movies_cat':trending_movies_cat,'punjabi_movies_cat':punjabi_movies_cat}
	return render(request,template,context)
