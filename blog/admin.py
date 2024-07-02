from django.contrib import admin

from blog.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('id', 'title', 'created_at', 'published', 'count_views',)
    list_filter = ('created_at',)
    search_fields = ('title', 'created_at', 'published',)
