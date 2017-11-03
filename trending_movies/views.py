from django.shortcuts import render,get_object_or_404
from .models import Category,Post

# Create your views here.


def list_of_category(request):
	category=Category.objects.all()
	template='cartoons/category/list_of_category.html'
	context={'category':category}
	return render(request,template,context)

def post_detail(request,slug):
	post=get_object_or_404(Post,slug=slug)
	categoryid_of_post_selected=post.category_id
	all_posts_of_same_category=Post.objects.filter(category=categoryid_of_post_selected)
	index_of_post_selected=list(all_posts_of_same_category).index(post)
	li=[]
	for j in all_posts_of_same_category:
		li=li+[j.video.url]
	li=li[index_of_post_selected:]
	template='cartoons/posts/post_detail.html'
	context={'post':post,'categoryid_of_post_selected':categoryid_of_post_selected,'all_posts_of_same_category':all_posts_of_same_category,'index_of_post_selected':index_of_post_selected,'li':li,'j':j}
	return render(request,template,context)


def list_of_post_by_category(request,category_slug):
	categories=Category.objects.all()
	post=Post.objects.all()
	if category_slug:
		category=get_object_or_404(Category,slug=category_slug)
		post_by_category=post.filter(category=category)
		li=[]
		for i in post_by_category:
			li=li+[i.video.url]
	template='cartoons/category/list_of_post_by_category.html'
	context={'categories':categories,'post':post,'category':category,'post_by_category':post_by_category,'li':li}
	return render(request,template,context)
