from django.contrib import admin
from .models import Post, Category


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at')
    list_filter = ('category',)
    search_fields = ('title', 'content')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
