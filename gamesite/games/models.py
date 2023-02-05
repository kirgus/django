from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    """Категории игр"""
    name = models.CharField(max_length=100, db_index=True, verbose_name='Название категории',
                            default='Название категории')

    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='Владелец')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']


class Game(models.Model):
    """Игры"""
    name = models.CharField(max_length=200, verbose_name='Название', default='Название игры')  # название игры

    description = models.TextField(blank=True, verbose_name='Описание')  # описание игры

    img = models.ImageField(upload_to='images/%Y/%m/%d/', blank=True, verbose_name='Картинка')  # картинка игры

    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')  # время обновления записи

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')  # время создания записи

    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')  # опубликована ли запись

    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True, blank=True, verbose_name='Категории')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Игра'  # название в единственном числе
        verbose_name_plural = 'Игры'  # название во множественном числе
        ordering = ['-created_at']  # порядок сортировки
