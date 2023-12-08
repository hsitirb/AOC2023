import pytest
from Day7.camel_cards import CamelCards

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
