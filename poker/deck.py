import random
from typing import List

from .card import Card

class DeckFactory:
  def __init__(self, lowest_rank: int):
    self._lowest_rank = lowest_rank

  def create_deck(self):
    return Deck(self._lowest_rank)

class Deck:
  def __init__(self, lowest_rank: int):
    self._cards: List[Card] = [Card(rank, suit) for rank in range(lowest_rank, 15) for suit in range(0,4)]
    self._discard: List[Card] = []
    random.shuffle(self._cards)

  def pop_cards(self, num_cards = 1) -> List[Card]: # return list of popped cards
    new_cards = []
    if len(self._cards) < num_cards:
      new_cards = self._cards
      self._cards = self._discard
      self._discard = []
      random.shuffle(self._cards)
    return new_cards + [self._cards.pop() for i in range(num_cards - len(new_cards))]

  def push_cards(self, discard: List[Card]):
    self._discard += discard
