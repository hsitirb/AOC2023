class Almanac:
    def __init__(self, spec):
        state = None
        self.tables = {}
        self.seeds = []
        for line in spec.splitlines():
            if state is None:
                if line.startswith("seeds"):
                    _, seed_spec = line.split(":")
                    seeds_entry = [*map(int, seed_spec.split())]
                    for seed, rng in zip(seeds_entry[0::2], seeds_entry[1::2]):
                        for offset in range(rng):
                            self.seeds.append(seed + offset)
                    state = "table_search"
            elif state == "table_search":
                if line == "":
                    state = "table"
                    table_lines = ""
            elif state == "table":
                if line == "":
                    table = AlmanacTable(table_lines)
                    self.tables[table.source_name] = table                    
                    table_lines = ""
                else:
                    table_lines += line + "\n"
        table = AlmanacTable(table_lines)
        self.tables[table.source_name] = table
        print()

    def get_table(self, src_name):
        return self.tables[src_name]

    def get_location(self, seed):
        table_name = "seed"
        dest_val = seed 
        while table_name != "location":
            table = self.get_table(table_name)
            dest_val = table.get(dest_val)
            table_name = table.dest_name
        return dest_val

    def get_closest_location(self):
        locations = [self.get_location(seed) for seed in self.seeds]
        locations.sort()
        return locations[0]


class AlmanacTable:
    def __init__(self, spec):
        state = None
        self.map = []
        for line in spec.splitlines():
            if state is None:
                srcdst, _ = line.split()
                self.source_name, _, self.dest_name = srcdst.split("-")
                state = "map"
            elif state == "map":
                dest, src, rng = line.split()
                dest, src, rng = int(dest), int(src), int(rng)
                self.map.append((range(src, src + rng), range(dest, dest + rng)))
    
    def get(self, src_val):
        dst_val = src_val
        for src_rng, dst_rng in self.map:
            if src_val in src_rng:
                dst_val = dst_rng[0] + (src_val - src_rng[0])
                break
        return dst_val

if __name__ == "__main__":
    with open("Day5/puzzle_input.txt") as f:
        test_input = f.read()
    almanac = Almanac(test_input)
    print(f"{almanac.get_closest_location() = }")