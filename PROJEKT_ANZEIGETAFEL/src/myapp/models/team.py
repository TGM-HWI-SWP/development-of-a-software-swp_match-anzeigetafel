from models.player import Player
import random

class Team:
    def __init__(self, name):
        self.name = name
        self.players = self.generate_players()

    def generate_players(self):
        players = []
        for i in range(16):
            name = f"Spieler{i+1}"
            nummer = i + 1
            p = Player(name, nummer)
            if i >= 11:
                p.is_on_field = False
            players.append(p)
        return players

    def get_field_players(self):
        return [p for p in self.players if p.is_on_field]

    def get_bench_players(self):
        return [p for p in self.players if not p.is_on_field]

    def random_substitution(self):
        field = self.get_field_players()
        bench = self.get_bench_players()
        if bench:
            out_player = random.choice(field)
            in_player = random.choice(bench)
            out_player.is_on_field = False
            in_player.is_on_field = True
            return out_player, in_player
        return None, None

    def random_yellow_card(self):
        field = self.get_field_players()
        if field:
            player = random.choice(field)
            player.yellow_cards += 1
            return player
        return None
