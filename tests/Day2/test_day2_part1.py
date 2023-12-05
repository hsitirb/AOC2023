import pytest
from Day2.game import Game, Bag

game_input = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""


@pytest.mark.parametrize(
    "line, bag, expected",
    (
        (
            "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
            Bag(12, 13, 14),
            True,
        ),
        (
            "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
            Bag(12, 13, 14),
            True,
        ),
        (
            "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
            Bag(12, 13, 14),
            False,
        ),
        (
            "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
            Bag(12, 13, 14),
            False,
        ),
        (
            "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
            Bag(12, 13, 14),
            True,
        ),
    ),
)
def test_day2_line_is_possible(line, bag, expected):
    assert bag.satisfies(Game(line)) is expected

@pytest.mark.parametrize(
        "game_input, bag, expected", (
            (game_input, Bag(12, 13, 14), 8),
        )
)
def test_day2_id_sum(game_input, bag, expected):
    ids = []
    for line in game_input.splitlines():
        game = Game(line)
        if bag.satisfies(game):
            ids.append(int(game.id))
    assert sum(ids) == expected