from dataclasses import dataclass
from math import prod

@dataclass
class Race:
    time: int
    dist: int

class BoatRace:
    def __init__(self, spec):
        lines = spec.splitlines()
        _, time_line = lines[0].split(":")
        _, dist_line = lines[1].split(":")
        times = [*map(int, time_line.split())]
        dists = [*map(int, dist_line.split())]
        self.races = [Race(time, dist) for time, dist in zip(times, dists)]
    
    def current_best_dist(self, race_no):
        return self.races[race_no - 1].dist
    
    def possible_distances(self, race_no):
        race_time = self.races[race_no - 1].time
        return [
            (race_time - time) * time 
            for time in range(1, race_time)
        ]
    
    def wins_for_race_no(self, race_no):
        return sum([d > self.current_best_dist(race_no) for d in self.possible_distances(race_no)])

    def calculate_best(self):
        wins = [
            self.wins_for_race_no(race_no) 
            for race_no in range(1, len(self.races) + 1)
        ]
        return prod(wins)

