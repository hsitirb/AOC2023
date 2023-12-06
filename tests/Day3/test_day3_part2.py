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

def test_gear_ratio():
    assert sum(Schematic(test_input).gear_ratios) == 467835
