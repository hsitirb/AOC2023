from dataclasses import dataclass


class Round:
    def __init__(self, round_spec: str):
        self.red = 0
        self.green = 0
        self.blue = 0

        for section in round_spec.split(","):
            num, colour = section.strip().split()
            assert colour in ("red", "green", "blue")
            setattr(self, colour, int(num))


class Game:
    def __init__(self, game_spec: str):
        self.rounds = []
        game_info, round_info = game_spec.split(":")
        _, self.id = game_info.strip().split()
        self.rounds = [Round(round_spec) for round_spec in round_info.split(";")]
        self.min_red = max([round.red for round in self.rounds])
        self.min_green = max([round.green for round in self.rounds])
        self.min_blue = max([round.blue for round in self.rounds])


@dataclass
class Bag:
    red: int
    green: int
    blue: int

    def satisfies(self, game: Game) -> bool:
        return (
            self.red >= game.min_red
            and self.blue >= game.min_blue
            and self.green >= game.min_green
        )


if __name__ == "__main__":
    with open("Day2/puzzle_input.txt") as f:
        game_input = f.read()
    ids = []
    bag = Bag(12, 13, 14)  # Bag to test against - 12 red, 13 green, 14 blue
    for line in game_input.splitlines():
        game = Game(line)
        if bag.satisfies(game):
            ids.append(int(game.id))
    print(sum(ids))
