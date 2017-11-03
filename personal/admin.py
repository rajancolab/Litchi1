from django.contrib import admin

# Register your models here.
from .models import Post

class PostAdmin(admin.ModelAdmin):
	list_display=('product','slug')
	list_filter=('product','slug')
	prepopulated_fields={'slug':('product',)}

admin.site.register(Post,PostAdmin)