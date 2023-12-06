import pytest
from Day4.cards import Card, CardSet

test_input = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""

@pytest.mark.parametrize(
        "test_input, expected",
        (
            (test_input, 30),
        )
)
def test_card_total(test_input, expected):
    cardset = CardSet(test_input)
    cardset.process_cards()
    assert cardset.total_cards() == expected

@pytest.mark.parametrize(
    "test_input, card, expected",
    (
        (test_input, 1, 1),
        (test_input, 2, 2),
        (test_input, 3, 4),
        (test_input, 4, 8),
        (test_input, 5, 14),
        (test_input, 6, 1),
    )
)
def test_card_counts(test_input, card, expected):
    cardset = CardSet(test_input)
    cardset.process_cards()
    assert cardset.get_card(card).copies == expected