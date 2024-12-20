from django.shortcuts import render
from django.http import JsonResponse
from .models import Card
from .utils import initialize_cards, get_top_times, add_time_record



def submit_time_view(request):
    time = int(request.GET.get('time'))
    add_time_record(time)
    return JsonResponse({'status': 'success', 'top_records': get_top_times()})  

def game_view(request):
    if not Card.objects.exists():
        initialize_cards()
    
    cards = Card.objects.all()
    top_records = get_top_times()
    
    return render(request, 'game/game.html', {'cards': cards, 'top_records': top_records})



  
    

