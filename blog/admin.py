from django.contrib import admin

from .models import Comment, Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pub_date', 'update_date')
    list_filter = ('author', 'pub_date', 'update_date')
    search_fields = ('title', 'content')
    ordering = ('-pub_date',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'text', 'pub_date')
    list_filter = ('author', 'post', 'pub_date')
    search_fields = ('text',)
    ordering = ('-pub_date',)
