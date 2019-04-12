from collections import Counter


class Scoreboard:

    def __init__(self):
        self.players = []
        self.score = Counter()

    def add_player(self, player: "String") -> None:
        self.players.append(player)
        return

    def add_point(self, player: "String") -> None:
        self.score[player] += 1
        if player not in self.players:
            self.add_player(player)
        return

    def get_scoreboard(self) -> "String":
        result = "SCORE:\n" + ("-" * 15) + "\n\n"
        for x in self.score.keys():
            result += "{:10} {}".format(x, self.score[x])
        return result
