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

min_input_TL = """.123...
....*..
"""
min_input_T = """...123...
....&....
"""
min_input_TR = """......123
.....%...
"""
min_input_L = """123+...
"""
min_input_R = """...+123
"""
min_input_BL = """...@.....
123......
"""
min_input_B = """....@....
...123...
"""
min_input_BR = """.....@...
......123
"""


med_input_1 = (
    """123..456.
....*....
.789.....""",
    set([456, 789])
)
med_input_2 = (""".123.456.
....*....
......789""",
    set([123, 456])
)

@pytest.mark.parametrize(
        "test_input, expected",
        (
            (test_input, set([467, 35, 633, 617, 592, 755, 664, 598])),
            ("617*......", set([617])),
            (min_input_TL, set([123])),
            (min_input_T, set([123])),
            (min_input_TR, set([123])),
            (min_input_L, set([123])),
            (min_input_R, set([123])),
            (min_input_BL, set([123])),
            (min_input_B, set([123])),
            (min_input_BR, set([123])),
            med_input_1,
            med_input_2
        )
)
def test_part_number_list(test_input, expected):
    assert set(Schematic(test_input).parts_list) == expected

def test_part_number_sum():
    assert sum(Schematic(test_input).parts_list) == 4361