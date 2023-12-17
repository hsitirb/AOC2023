from dataclasses import dataclass
from enum import Enum

Card = Enum("Card", ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"])
Type = Enum("Type", ["FIVE_OF_A_KIND", "FOUR_OF_A_KIND", "FULL_HOUSE", "THREE_OF_A_KIND", "TWO_PAIR", "ONE_PAIR", "HIGH_CARD"])


@dataclass
class Hand:
    hand: str
    bid: int

    def is_five_of_a_kind(self):
        return all(Card[self.hand[0]] == Card[card] for card in self.hand)

    def is_four_of_a_kind(self):
        return (
            self.hand.count(self.hand[0]) == 4 or 
            self.hand.count(self.hand[1]) == 4
        )

    def is_full_house(self):
        return sum([self.hand.count(self.hand[idx]) for idx in range(len(self.hand))]) == 13

    def is_three_of_a_kind(self):
        return (
            self.hand.count(self.hand[0]) == 3 or 
            self.hand.count(self.hand[1]) == 3 or 
            self.hand.count(self.hand[2]) == 3
        )

    def is_two_pair(self):
        return sum([self.hand.count(self.hand[idx]) for idx in range(len(self.hand))]) == 9

    def is_one_pair(self):
        return sum([self.hand.count(self.hand[idx]) for idx in range(len(self.hand))]) == 7

    def is_high_card(self):
        return sum([self.hand.count(self.hand[idx]) for idx in range(len(self.hand))]) == 5

    @property
    def type(self):
        typedict = {
            Type.FIVE_OF_A_KIND: Hand.is_five_of_a_kind,
            Type.FOUR_OF_A_KIND: Hand.is_four_of_a_kind,
            Type.FULL_HOUSE: Hand.is_full_house,
            Type.THREE_OF_A_KIND: Hand.is_three_of_a_kind,
            Type.TWO_PAIR: Hand.is_two_pair,
            Type.ONE_PAIR: Hand.is_one_pair,
            Type.HIGH_CARD: Hand.is_high_card,
        }
        for hand_type, determiner in typedict.items():
            if determiner(self):
                return hand_type

class CamelCards:
    def __init__(self, spec):
        self.hands = []
        for line in spec.splitlines():
            hand, bid = line.split()
            self.hands.append(Hand(hand, int(bid)))
            
    def total_winnings(self):
        return 0
