from django.contrib import admin
from . import models

@admin.register(models.ArticleType)
class ArticleTypeAdmin(admin.ModelAdmin):
    list_play = ('id','author','name')


@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    list_play = ('id','author','type','create_time','update_time')