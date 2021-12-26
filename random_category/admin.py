from django.contrib import admin
from .models import Random_Category, Random_Detail, Quote


@admin.register(Random_Category)
class Random_CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name')


@admin.register(Random_Detail)
class Random_DetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category')

@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'quote')
