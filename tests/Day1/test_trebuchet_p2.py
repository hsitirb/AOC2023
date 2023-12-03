import pytest
from Day1.trebuchet import line_value, lines_result

lines = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""

lines_vals = (
    ("two1nine", 29),
    ("eightwothree", 83),
    ("abcone2threexyz", 13),
    ("xtwone3four", 24),
    ("4nineeightseven2", 42),
    ("zoneight234", 14),
    ("7pqrstsixteen", 76),
    ("oneight", 18),
)

@pytest.mark.parametrize(
    "input_line,expected",
    lines_vals
)
def test_line_value(input_line, expected):
    assert line_value(input_line) == expected

@pytest.mark.parametrize(
    "input_lines,expected",
    (
        (lines, 281),
    )
)
def test_total_value(input_lines, expected):
    assert lines_result(input_lines) == expected