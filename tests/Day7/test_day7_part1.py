import pytest
from Day7.camel_cards import CamelCards, Type, Hand

test_input = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""

@pytest.mark.parametrize(
        "hand_spec, expected",
        (
            (test_input, 6440),
        ),
)
def test_total_winnings(hand_spec, expected):
    assert CamelCards(hand_spec).total_winnings() == expected

@pytest.mark.parametrize(
    "hand, hand_type",
    (
        ("A2345", Type.HIGH_CARD),
        ("AA345", Type.ONE_PAIR),
        ("AAA45", Type.THREE_OF_A_KIND),
        ("AAAA5", Type.FOUR_OF_A_KIND),
        ("AAAAA", Type.FIVE_OF_A_KIND),
        ("AAA44", Type.FULL_HOUSE),
        ("32T3K", Type.ONE_PAIR),
        ("T55J5", Type.THREE_OF_A_KIND),
        ("KK677", Type.TWO_PAIR),
        ("KTJJT", Type.TWO_PAIR),
        ("QQQJA", Type.THREE_OF_A_KIND),
    )
)
def test_hand_type(hand, hand_type):
    assert Hand(hand, 1).type == hand_type