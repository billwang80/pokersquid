class Card:
  RANKS = {
    2: "2",
    3: "3",
    4: "4",
    5: "5",
    6: "6",
    7: "7",
    8: "8",
    9: "9",
    10: "10",
    11: "J",
    12: "Q",
    13: "K",
    14: "A",
  }
  SUITS = {
    3: "h",
    2: "d",
    1: "c",
    0: "s",
  }

  def __init__(self, rank: int, suit: int):
    if rank not in Card.RANKS:
      raise ValueError("Invalid rank")
    if suit not in Card.SUITS:
      raise ValueError("Invalid suit")
    self._value: int = (rank * 4) + suit
    
  @property
  def rank(self) -> int: # return rank
    return self._value // 4
  
  @property
  def suit(self) -> int: # return suit
    return self._value % 4

  def __lt__(self, other): # less than
    return int(self) < int(other)
  
  def __eq__(self, other): # equal
    return int(self) == int(other)

  def dto(self): # rank and suit
    return self.rank, self.suit
