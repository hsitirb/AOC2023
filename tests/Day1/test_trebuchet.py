import pytest
from trebuchet import line_value, lines_result


@pytest.mark.parametrize(
    "input_line,expected",
    (
        ("1abc2", 12),
        ("pqr3stu8vwx", 38),
        ("a1b2c3d4e5f", 15),
        ("treb7uchet", 77),
    ),
)
def test_line_value(input_line, expected):
    assert line_value(input_line) == expected


@pytest.mark.parametrize(
    "input_lines,expected", (("1abc2" "pqr3stu8vwx" "a1b2c3d4e5f" "treb7uchet", 142),)
)
def test_total_value(input_lines, expected):
    assert lines_result(input_lines) == expected
