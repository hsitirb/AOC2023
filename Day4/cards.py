class Card:
    def __init__(self, card_spec: str):
        card_id_part, rest = card_spec.split(":")
        _, card_id_str = card_id_part.split()
        self.card_id = int(card_id_str)
        winning_numbers, selected_numbers = rest.split("|")
        self.winning_numbers = [int(num.strip()) for num in winning_numbers.split()]
        self.selected_numbers = [int(num.strip()) for num in selected_numbers.split()]

    @property
    def matches(self):
        return set(self.winning_numbers) & set(self.selected_numbers)

    @property
    def value(self):
        if self.count == 0:
            return 0
        else:
            return 2 ** (self.count - 1) 

    @property
    def count(self):
        return len(self.matches)

class CardSetCard(Card):
    def __init__(self, card):
        self.card = card
        self.copies = 1
        self.processed = False

    @property
    def card_id(self):
        return self.card.card_id

    @property
    def matches(self):
        return self.card.matches

class CardSet:
    def __init__(self, card_specs: str):
        self.cards = {}
        for card_spec in card_specs.splitlines():
            card = CardSetCard(Card(card_spec))
            self.cards[card.card_id] = card
    
    def process_cards(self):
        for card_id in self.cards:
            card = self.get_card(card_id)
            for offset in range(1, len(card.matches) + 1):
                self.get_card(card.card_id + offset).copies += card.copies
                
    def get_card(self, cardid):
        return self.cards.get(cardid)

    def total_cards(self):
        return sum(card.copies for card in self.cards.values())

if __name__ == "__main__":
    with open("Day4/puzzle_input.txt") as f:
        test_input = f.read()
    card_values = [Card(line).value for line in test_input.splitlines()]
    print(f"{sum(card_values) = }")
    cardset = CardSet(test_input)
    cardset.process_cards()
    print(f"{cardset.total_cards() = }")