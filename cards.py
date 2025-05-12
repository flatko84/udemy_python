from functools import total_ordering

class CardsBase:

    suits = ['spades', 'diamonds', 'clubs', 'hearts']

    @property
    def cards_pool(self):
        cards_pool = ['a']
        for rank in range(2,11):
            cards_pool.append(str(rank))
        for rank in ['j', 'q', 'k']:
            cards_pool.append(rank)
        return cards_pool
    
   


@total_ordering
class PlayingCard(CardsBase):
    

    def __init__(self, rank, suit):
        self.suit = suit.lower()
        self.rank = rank.lower()

    def __eq__(self, other):
        return self.rank == other.rank
    
    def __gt__(self, other):
        return self.cards_pool.index(self.rank) > self.cards_pool.index(other.rank)
    
    def __repr__(self):
        return f"{self.__class__.__name__}(suit='{self.suit}', rank='{self.rank}')"



class CardDeck(CardsBase):

    def __init__(self, cards = None):
        if cards is None:
            self._cards = self.full_deck()
        else:
            self._cards = cards

    def add(self, item):
        self._cards.append(item)

    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self, item):
        if type(item) == slice:
            self_class = type(self)
            new_instance = self_class()
            for card in self._cards[item]:
                new_instance.add(card)
            return new_instance
        elif type(item) == int:
            return self._cards[item]
        
    def __add__(self, other):
        new_instance = CardDeck()
        if type(other) == PlayingCard:
            self.add(other)
        elif type(other) == type(self):
            for other_card in other:
                self.add(other_card)

    def full_deck(self):
        cards = []
        for suit in self.suits:
            for rank in self.cards_pool:
                cards.append(PlayingCard(rank, suit))
        return cards
        
    def __repr__(self):
        repr = f"{self.__class__.__name__} collection:"
        collection = "".join([f"\n{str(card)}" for card in self._cards])
        return f"{repr}{collection}"




two_of_spades = PlayingCard('2', 'spades')
queen_of_hearts = PlayingCard('Q', 'hearts')
seven_of_clubs = PlayingCard('7', 'clubs')
print(two_of_spades)
print(queen_of_hearts)
print(queen_of_hearts >= queen_of_hearts)
deck = CardDeck([])
deck.add(two_of_spades)
deck.add(queen_of_hearts)
deck.add(seven_of_clubs)
print(deck[:-1])
print(queen_of_hearts in deck)
print(f"test4e {CardDeck()}")
print(deck + CardDeck([PlayingCard('a', 'spades')]))