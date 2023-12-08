import pytest
from Day6.boatrace import BoatRace

test_input = """Time:      7  15   30
Distance:  9  40  200"""


@pytest.mark.parametrize(
        "test_input, expected",
        (
            (test_input, 288),
        ),
    )
def test_solution(test_input, expected):
    assert BoatRace(test_input).calculate_best() == expected


@pytest.mark.parametrize(
    "race_spec, race_no, expected",
    (
        (test_input, 1, 4),
        (test_input, 2, 8),
        (test_input, 3, 9),
    ),
)
def test_race_wins(race_spec, race_no, expected):
    assert BoatRace(race_spec).wins_for_race_no(race_no) == expected
