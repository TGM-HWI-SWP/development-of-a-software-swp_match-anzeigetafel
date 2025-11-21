from typing import Protocol, List
from models.team import Team
from models.player import Player


class DatabasePort(Protocol):
    """Interface für alle Datenbank-Adapter."""

    def get_teams(self) -> List[Team]:
        ...

    def get_team(self, team_id: int) -> Team:
        ...

    def get_players(self, team_id: int) -> List[Player]:
        ...

    def get_player(self, player_id: int) -> Player:
        ...


class ViewPort(Protocol):
    """Interface für die GUI."""

    def show_teams(self, teams: List[Team]) -> None:
        ...

    def show_players(self, players: List[Player]) -> None:
        ...

    def show_score(self, home: int, away: int) -> None:
        ...
