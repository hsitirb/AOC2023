import pytest
from Day5.almanac import Almanac, AlmanacTable

test_input = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""

seed_soil_spec = """seed-to-soil map:
50 98 2
52 50 48"""

@pytest.mark.parametrize(
    "spec, seed_id, soil_id",
    (
        (seed_soil_spec, 79, 81),
        (seed_soil_spec, 14, 14),
        (seed_soil_spec, 55, 57),
        (seed_soil_spec, 13, 13),
        (seed_soil_spec, 99, 51),
        (seed_soil_spec, 97, 99),
        (seed_soil_spec, 49, 49),
        (seed_soil_spec, 50, 52),
        (seed_soil_spec, 51, 53),
    )
)
def test_seed_soil_map(spec, seed_id, soil_id):
    assert AlmanacTable(spec).get(seed_id) == soil_id

@pytest.mark.parametrize(
    "specs, expected",
    (
        (test_input, 35),
    )
)
def test_closest_location(specs, expected):
    assert Almanac(specs).get_closest_location() == expected