from django.contrib import admin

from .models import Game, Category


class GameAdmin(admin.ModelAdmin):
    """Настройки отображения таблицы игр в Админке"""
    list_display = ('id', 'name', 'category', 'created_at', 'updated_at', 'is_published')

    list_display_links = ('id', 'name')

    search_fields = ('name', 'description')

    list_editable = ('is_published',)

    list_filter = ('is_published', 'category')


class CategoryAdmin(admin.ModelAdmin):
    """Настройки отображения таблицы категорий в Админке"""
    list_display = ('id', 'name')

    list_display_links = ('id', 'name')

    search_fields = ('name',)


# Регистрация в Админке
admin.site.register(Game, GameAdmin)

admin.site.register(Category, CategoryAdmin)
