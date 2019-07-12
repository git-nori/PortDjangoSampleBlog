from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Article

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')

admin.site.register(CustomUser, UserAdmin)
admin.site.register(Article, ArticleAdmin)