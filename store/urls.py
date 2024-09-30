from django.urls import path
from .views import most_recent, all_products, all_categories, game_detail, order_game

urlpatterns = [
    path('most-recent/', most_recent, name='most_recent'),
    path('all-products/', all_products, name='all_products'),
    path('all-categories/', all_categories, name='all_categories'),
    path('game/<int:game_id>/', game_detail, name='game_detail'),
    path('order/<int:game_id>/', order_game, name='order_game'),
]
