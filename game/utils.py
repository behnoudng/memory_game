import random, heapq
from .models import Card

time_heaps = {
    'easy': [],
    'normal': [],
    'hard': []
}

def initialize_cards(mode):
    if mode == 'easy':
        card_values = ["A","B","C","D"]  # 4 pairs
    elif mode == 'hard':
        card_values = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N"]  # 14 pairs
    else:
        card_values = ["A","B","C","D","E","F","G","H"]  # normal (8 pairs)

    deck = card_values * 2
    random.shuffle(deck)
    for value in deck:
        Card.objects.create(value=value)

def add_time_record(time, mode):
    heapq.heappush(time_heaps[mode], (time, f"{time}s"))

def get_top_times(mode='normal', n=3):
    return heapq.nsmallest(n, time_heaps[mode])