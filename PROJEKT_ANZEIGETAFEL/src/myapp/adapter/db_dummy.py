from typing import List
from contracts.ports import DatabasePort
from models.team import Team
from models.player import Player
from dummy.dummy_data import TEAMS, PLAYERS


class DummyDB(DatabasePort):
    """In-Memory Datenbank für Testing und Entwicklung."""

    def get_teams(self) -> List[Team]:
        return TEAMS

    def get_team(self, team_id: int) -> Team:
        return next(t for t in TEAMS if t.id == team_id)

    def get_players(self, team_id: int) -> List[Player]:
        return [p for p in PLAYERS if p.team_id == team_id]

    def get_player(self, player_id: int) -> Player:
        return next(p for p in PLAYERS if p.id == player_id)