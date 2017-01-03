from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = ('id', 'title', 'date_created')


admin.site.register(Post, PostAdmin)
