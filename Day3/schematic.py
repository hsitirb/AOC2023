from dataclasses import dataclass

@dataclass
class Loc:
    x: int
    y: int

    def __add__(self, other):
        return Loc(self.x + other.x, self.y + other.y)

    def __hash__(self):
        return self.x * 10000 + self.y

class Schematic:
    def __init__(self, schematic: str):
        schematic_part_nos = {}
        schematic_symbols = []
        self.valid_partnos = set()
        for row, line in enumerate(schematic.splitlines()):
            state = None
            for col, symbol in enumerate(line):
                if state == "partno":
                    if not symbol.isnumeric():
                        for loc_col in range(start_col, col):
                            schematic_part_nos[Loc(row, loc_col)] = partno
                        state = None
                        partno = None
                        start_col = None
                    else:
                        partno += symbol
                if state is None:
                    if symbol != "." and not symbol.isnumeric():
                        schematic_symbols.append(Loc(row, col))
                    elif symbol.isnumeric():
                        state = "partno"
                        partno = symbol
                        start_col = col
            for symbol_loc in schematic_symbols:
                for offset in (
                    # fmt: off
                    Loc(-1, -1), Loc( 0, -1), Loc( 1, -1),
                    Loc(-1,  0),              Loc( 1,  0),
                    Loc(-1,  1), Loc( 0,  1), Loc( 1,  1)
                    # fmt: on
                ):
                    offset_symbol_loc = symbol_loc + offset
                    if offset_symbol_loc in schematic_part_nos:
                        self.valid_partnos.add(int(schematic_part_nos[offset_symbol_loc]))

    @property
    def parts_list(self):
        return list(self.valid_partnos)