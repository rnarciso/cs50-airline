from django.contrib import admin
from .models import Post, Category, Author


class PostAdmin(admin.ModelAdmin):
	list_display = ('subject', 'author', 'publish_date', 'last_modify', 'category')


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Author)