class Card:
    def __init__(self, card_spec):
        self.card_id, rest = card_spec.split(":")
        winning_numbers, selected_numbers = rest.split("|")
        self.winning_numbers = [int(num.strip()) for num in winning_numbers.split()]
        self.selected_numbers = [int(num.strip()) for num in selected_numbers.split()]

    @property
    def value(self):
        match_set = set(self.winning_numbers) & set(self.selected_numbers)
        if len(match_set) == 0:
            return 0
        else:
            return 2 ** (len(match_set) - 1) 