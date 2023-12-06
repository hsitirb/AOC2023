import pytest
from Day3.schematic import Schematic

test_input = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""

@pytest.mark.parametrize(
        "test_input, expected",
        (
            (test_input, set([467, 35, 633, 617, 592, 755, 664, 598])),
            ("617*......", set([617])),
        )
)
def test_part_number_list(test_input, expected):
    assert set(Schematic(test_input).parts_list) == expected

def test_part_number_sum():
    assert sum(Schematic(test_input).parts_list) == 4361