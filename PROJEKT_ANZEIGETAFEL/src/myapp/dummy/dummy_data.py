import random

class Player:
    def __init__(self, name, nummer):
        self.name = name
        self.nummer = nummer
        self.tore = 0
        self.yellow_cards = 0

class Team:
    def __init__(self, name):
        self.name = name
        self.players = self.generate_players()

    def generate_players(self):
        # 11 auf Feld + 5 Bank
        players = []
        for i in range(1, 17):
            players.append(Player(f"Spieler {i}", i))
        return players

    def get_field_players(self):
        return self.players[:11]

    def get_bench_players(self):
        return self.players[11:]

    def random_yellow_card(self):
        player = random.choice(self.get_field_players())
        player.yellow_cards += 1
        return player

    def random_substitution(self):
        field = self.get_field_players()
        bench = self.get_bench_players()
        if not bench:
            return None, None
        out_player = random.choice(field)
        in_player = random.choice(bench)
        # Tausch
        idx_out = field.index(out_player)
        idx_in = self.players.index(in_player)
        self.players[idx_out], self.players[idx_in] = self.players[idx_in], self.players[idx_out]
        return out_player, in_player

class DummyDB:
    def __init__(self):
        self.teams = []

    def create_team(self, name):
        team = Team(name)
        self.teams.append(team)
        return team

    def get_team_by_name(self, name):
        for team in self.teams:
            if team.name == name:
                return team
        return None
