from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_posted', 'content', 'image_url')
    list_filter = ('title', 'date_posted')
    search_fields = ['title']

admin.site.register(Post, PostAdmin)