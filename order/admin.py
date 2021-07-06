from django.contrib import admin
from django.contrib.admin import filters

from .models import Menu,MenuCategory
@admin.register(MenuCategory)
class MenuCategoryAdmin(admin.ModelAdmin):
    list_display=('categoryname',)

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display=('dish','ingredient','price','category')
    list_filter=('category',)
    search_fields=('dish',)
