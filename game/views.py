from django.shortcuts import render
from django.http import JsonResponse
from .models import Card
from .utils import initialize_cards, get_top_times, add_time_record



def submit_time_view(request):
    time = int(request.GET.get('time'))
    mode = request.GET.get('mode', 'normal')
    add_time_record(time, mode)
    return JsonResponse({'status': 'success', 'top_records': get_top_times(mode)})  

def game_view(request):
    mode = request.GET.get('mode', 'normal')
    last_mode = request.session.get('last_mode')

    if last_mode != mode:
        Card.objects.all().delete()
        initialize_cards(mode)
        request.session['last_mode'] = mode
    
    cards = Card.objects.all()
    top_records = get_top_times(mode)
    
    return render(request, 'game/game.html', {'cards': cards, 'top_records': top_records, 'mode': mode})






