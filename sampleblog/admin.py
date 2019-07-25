from django.contrib import admin
from .models import CustomUser, Article
from django.utils.html import format_html


# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'gender', 'image')
    list_display_links = ('username',)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Article, ArticleAdmin)
