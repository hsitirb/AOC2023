import pytest
from Day6.boatrace import BoatRace

test_input = """Time:      7  15   30
Distance:  9  40  200"""


@pytest.mark.parametrize(
        "test_input, expected",
        (
            (test_input, 71503),
        ),
    )
def test_solution(test_input, expected):
    assert BoatRace(test_input).calculate_best() == expected
