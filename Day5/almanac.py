class Almanac:
    ...

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