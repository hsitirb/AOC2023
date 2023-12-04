from dataclasses import dataclass

@dataclass
class Bag:
    red: int
    green: int
    blue: int
    
class Bag:
    def __init__(self, red: int, blue: int, green: int):
        self.red = red
        self.blue = blue
        self.green = green

    def is_possible(self, game: Game) -> bool:
          return (
             red <= game.min_red and
             blue <= game.min_blue and
             green <= game.min_green
         )

class Game:
    def __init__(self, game_spec: str):
        self.rounds = []
        game_info, round_info = line.split(":")
        _, self.id = game_info.strip().split()
        self.rounds = [Round(round_spec) for round_spec in round_info.split(";")

class Round:
    def __init__(self, round_spec: str):
        for section in round_spec.split(","):
            num, colour = section.strip().split()
            assert colour in ("red", "green", "blue")
            set_attr(self, colour, int(num))