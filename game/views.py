from django.shortcuts import render
from .models import Card
from .utils import initialize_cards, pop_from_stack, push_to_stack

def game_view(request):
    if not Card.objects.exists():
        initialize_cards()

    if 'undo' in request.GET:
        pop_from_stack()
    
    cards = Card.objects.all()
    return render(request, 'game/game.html', {'cards': cards})

    
    

