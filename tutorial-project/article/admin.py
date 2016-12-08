from django.contrib import admin

from .models import Article


class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('article_name', 'article_desc', 'image_name', 'image')
    search_fields = ['article_name']

admin.site.register(Article, ArticlesAdmin)
