from dataclasses import dataclass
from operator import mul

@dataclass
class Loc:
    x: int
    y: int

    def __add__(self, other):
        return Loc(self.x + other.x, self.y + other.y)

    def __hash__(self):
        return self.x * 10000 + self.y

@dataclass
class Symbol:
    symbol: str
    loc: Loc

    def __hash__(self):
        return hash(self.loc)

class Schematic:
    def __init__(self, schematic: str):
        schematic_part_nos = {}
        schematic_part_no_locs = {}
        partno_id = 0
        self.schematic_symbols = {}
        valid_partno_ids = set()
        valid_schematic_symbols = {}
        for row, line in enumerate(schematic.splitlines()):
            state = None
            start_col, partno = None, None
            for col, symbol in enumerate(line):
                if state == "partno":
                    if not symbol.isnumeric():
                        for loc_col in range(start_col, col):
                            schematic_part_no_locs[Loc(row, loc_col)] = partno_id
                        schematic_part_nos[partno_id] = partno
                        partno_id += 1
                        state = None
                        partno = None
                        start_col = None
                    else:
                        partno += symbol
                if state is None:
                    if symbol != "." and not symbol.isnumeric():
                        valid_schematic_symbols[Symbol(symbol, Loc(row, col))] = set()
                    elif symbol.isnumeric():
                        state = "partno"
                        partno = symbol
                        start_col = col
            if state == "partno":
                for loc_col in range(start_col, start_col + len(partno)):
                    schematic_part_no_locs[Loc(row, loc_col)] = partno_id
                schematic_part_nos[partno_id] = partno
                partno_id += 1
                state = None
                partno = None
                start_col = None
        for symbol in valid_schematic_symbols:
            for offset in (
                # fmt: off
                Loc(-1, -1), Loc( 0, -1), Loc( 1, -1),
                Loc(-1,  0),              Loc( 1,  0),
                Loc(-1,  1), Loc( 0,  1), Loc( 1,  1)
                # fmt: on
            ):
                offset_symbol_loc = symbol.loc + offset
                if offset_symbol_loc in schematic_part_no_locs:
                    valid_partno_ids.add(schematic_part_no_locs[offset_symbol_loc])
                    valid_schematic_symbols[symbol].add(schematic_part_no_locs[offset_symbol_loc])
        self.valid_partnos = [int(schematic_part_nos[entry]) for entry in valid_partno_ids]
        for symbol in valid_schematic_symbols:
            self.schematic_symbols[symbol] = [int(schematic_part_nos[entry]) for entry in valid_schematic_symbols[symbol]]

    @property
    def parts_list(self):
        return list(self.valid_partnos)

    @property
    def gear_ratios(self):
        gears = []
        gear_symbols = [symbol for symbol in self.schematic_symbols if symbol.symbol == "*"]
        for symbol in gear_symbols:
            if len(self.schematic_symbols[symbol]) == 2:
                gears.append(symbol)
        gear_ratios = [mul(*self.schematic_symbols[gear]) for gear in gears]
        return gear_ratios

if __name__ == "__main__":
    with open("Day3/puzzle_input.txt") as f:
        test_input = f.read()
    parts_list = Schematic(test_input).parts_list
    print(parts_list)
    print(sum(Schematic(test_input).parts_list))