import random, heapq
from .models import Card


def initialize_cards():
    card_values = ["A", "B", "C", "D", "E", "F", "G", "H"]
    deck = card_values * 2
    random.shuffle(deck)

    for value in deck:
        Card.objects.create(value=value)


time_heap = []
def add_time_record(time):
    heapq.heappush(time_heap, (time, f"{time}s"))

def get_top_times(n=3):
    return heapq.nsmallest(n, time_heap)