from functools import total_ordering
import unittest
from typing import Self

class CardsBase:

    suits = ['spades', 'diamonds', 'clubs', 'hearts']

    @property
    def cards_pool(self) -> list:
        """Return a list of card ranks."""
        cards = ['a']
        for rank in range(2,11):
            cards.append(str(rank))
        for rank in ['j', 'q', 'k']:
            cards.append(rank)
        return cards
    

@total_ordering
class PlayingCard(CardsBase):
    def __init__(self, rank: str, suit: str) -> None:
        self.suit = suit.lower()
        self.rank = rank.lower()

    def __eq__(self, other: Self) -> bool:
        return self.rank == other.rank
    
    def __gt__(self, other: Self) -> bool:
        return self.cards_pool.index(self.rank) > self.cards_pool.index(other.rank)
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(suit='{self.suit}', rank='{self.rank}')"



class CardDeck(CardsBase):

    def __init__(self, cards = []):
        cards = [card for card in cards if type(card) is PlayingCard]
        if not len(cards):
            self._cards = self.full_deck()
        else:
            self._cards = cards

    def add(self, item: PlayingCard) -> None:
        if type(item) is PlayingCard:
            self._cards.append(item)

    def __len__(self) -> int:
        return len(self._cards)
    
    def __getitem__(self, item: int | slice) -> Self | PlayingCard:
        if type(item) is slice:
            return CardDeck(self._cards[item])
        return self._cards[item]
        
    def __add__(self, other: Self | PlayingCard) -> None:
        if type(other) is PlayingCard:
            self.add(other)
        elif type(other) is type(self):
            for other_card in other:
                self.add(other_card)

    def full_deck(self) -> list:
        cards = []
        for suit in self.suits:
            for rank in self.cards_pool:
                cards.append(PlayingCard(rank, suit))
        return cards
        
    def __repr__(self) -> str:
        repr = f"{self.__class__.__name__} collection:"
        collection = "".join([f"\n{str(card)}" for card in self._cards])
        return f"{repr}{collection}"


class TestCards(unittest.TestCase):
    def test_cards(self):
        cd = CardDeck()
        cd2 = CardDeck(cards=[PlayingCard('diamonds', '2')])
        cd3 = CardDeck(cards=["Andrew", PlayingCard('clubs', '7')])
        cd4 = CardDeck(cards=["Andrew", "Lisa"])
        assert(len(cd) == 52)
        assert(len(cd2) == 1)
        assert(len(cd3) == 1)
        assert(len(cd4) == 52)
        print(cd[-10:])

if __name__ == '__main__':
    unittest.main()