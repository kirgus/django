from django.urls import path

from games.views import index, games_from_category, new_game, new_game_in_category

app_name = 'games'

urlpatterns = [

    path('', index, name='games'),

    # Игры из конкретной категории
    path('category/<int:category_id>/', games_from_category, name='category'),

    # Добавление новой игры
    path('new-game/', new_game, name='new-game'),

    # Добавление новой категории
    path('new-game-in-category/<int:category_id>/', new_game_in_category, name='new-game-in-category'),

]

