import random
from .models import Card


def initialize_cards():
    card_values = ["A", "B", "C", "D", "E", "F", "G", "H"]
    deck = card_values * 2
    random.shuffle(deck)

    for value in deck:
        Card.objects.create(value=value)


stack = []
def push_to_stack(card):
    stack.append(card)

def pop_from_stack():
    if stack:
        return stack.pop()
    else:
        return None
