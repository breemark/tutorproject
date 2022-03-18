from django.contrib import admin
from .models import Article, Menu


# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'active', 'created')

admin.site.register(Article, ArticleAdmin)


class MenuAdmin(admin.ModelAdmin):
    list_display = ('title', 'active', )

admin.site.register(Menu, MenuAdmin)