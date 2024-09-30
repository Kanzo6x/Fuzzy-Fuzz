from django.shortcuts import render, get_object_or_404, redirect
from .models import Game, Category, Order
import random
from django.contrib.auth.decorators import login_required

def most_recent(request):
    all_games = Game.objects.all()
    random_games = random.sample(list(all_games), min(4, all_games.count()))
    return render(request, 'store/most_recent.html', {'random_games': random_games})

def all_products(request):
    all_games = Game.objects.all()
    return render(request, 'store/all_products.html', {'all_games': all_games})

def all_categories(request):
    all_categories = Category.objects.all()
    return render(request, 'store/all_categories.html', {'all_categories': all_categories})

def game_detail(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    return render(request, 'store/game_detail.html', {'game': game})

@login_required
def order_game(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    if request.method == 'POST':
        phone = request.POST['phone']
        address = request.POST['address']
        Order.objects.create(game=game, user=request.user, phone=phone, address=address)
        return redirect('most_recent')
    return render(request, 'store/order_game.html', {'game': game})
