from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .forms import GameForm, CategoryForm

from .models import Game, Category


def landing_page(request):
    """Посадочная страница сайта """

    return render(request, 'games/landing-page.html')


@login_required()
def index(request):
    """Основная страница"""

    # Список игр
    games = Game.objects.all()

    # Список категорий
    # categories = Category.objects.all()
    categories = Category.objects.filter(owner=request.user)

    # Данные для шаблона
    context = {'name': 'Список игр', 'games': games, 'categories': categories}

    # Рендеринг шаблона
    return render(request, 'games/index.html', context)


def games_from_category(request, category_id):
    """Игры категории"""

    games = Game.objects.filter(category_id=category_id)

    categories = Category.objects.all()

    category = Category.objects.get(pk=category_id)

    context = {'games': games, 'category': category, 'categories': categories}

    return render(request, 'games/category.html', context)


@login_required()
def new_game(request):
    """Добавление новой игры"""
    if request.method != 'POST':
        form = GameForm()
    else:
        form = GameForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('games:games'))

    return render(request, 'games/new-game.html', {'form': form})


def new_game_in_category(request, category_id):
    """Добавление новой категории"""
    category = Category.objects.get(id=category_id)

    if request.method != 'POST':
        form = GameForm()
    else:
        form = GameForm(data=request.POST)

        if form.is_valid():
            new_game = form.save(commit=False)
            new_game.category = category
            new_game.save()

            return HttpResponseRedirect(reverse('games:category', args=[category_id]))

    return render(request, 'games/new-game-in-category.html', {'category': category, 'form': form})
