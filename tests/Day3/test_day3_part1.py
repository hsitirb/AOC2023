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

def test_part_number_list(test_input):
    assert set(Schematic(test_input).parts_list) == set("467", "35", "633", "617", "592", "755", "664", "598")

def test_part_number_sum(test_input):
    assert sum(Schematic(test_input)) == 4361