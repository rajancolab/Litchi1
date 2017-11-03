from django.contrib import admin
from .models import Category,Post

class CategoryAdmin(admin.ModelAdmin):
	list_display=('name','slug')
	list_filter=('name','seo_title')
	prepopulated_fields={'slug':('name',)}


class PostAdmin(admin.ModelAdmin):
	list_display=('title','category')
	list_filter=('title','category')
	prepopulated_fields={'slug':('title',)}

# Register your models here.

admin.site.register(Category,CategoryAdmin)
admin.site.register(Post,PostAdmin)
