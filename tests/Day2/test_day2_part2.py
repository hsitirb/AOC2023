import pytest
from Day2.game import Bag, Game

game_input = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""

@pytest.mark.parametrize(
    "line, bag",
    (
        (
            "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
            Bag(4, 2, 6),
        ),
        (
            "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
            Bag(1, 3, 4),
        ),
        (
            "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
            Bag(20, 13, 6),
        ),
        (
            "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
            Bag(14, 3, 15),
        ),
        (
            "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
            Bag(6, 3, 2),
        ),
    ),
)
def test_min_bag(line, bag):
    assert Game(line).min_bag() == bag

@pytest.mark.parametrize(
    "line, expected",
    (
        (
            "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
            48,
        ),
        (
            "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
            12,
        ),
        (
            "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
            1560,
        ),
        (
            "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
            630,
        ),
        (
            "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
            36,
        ),
    ),
)
def test_power(line, expected):
    assert Game(line).power() == expected

@pytest.mark.parametrize(
    "game_input, expected",
    (
        (game_input, 2286),
    ),
)
def test_result(game_input, expected):
    powers = [Game(line).power() for line in game_input.splitlines()]
    assert sum(powers) == expected
