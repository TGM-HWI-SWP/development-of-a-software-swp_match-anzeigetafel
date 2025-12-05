from typing import List
from contracts.ports import DatabasePort, ViewPort
from models.team import Team
from models.player import Player


class AnzeigetafelController:
    """Geschäftslogik der Stadionanzeigetafel."""

    def _init_(self, db: DatabasePort, view: ViewPort):
        self.db = db
        self.view = view
        self.score_home = 0
        self.score_away = 0

    # --- Use Cases ---

    def show_all_teams(self) -> None:
        teams = self.db.get_teams()
        self.view.show_teams(teams)

    def show_players_of_team(self, team_id: int) -> None:
        players = self.db.get_players(team_id)
        self.view.show_players(players)

    def goal_home(self) -> None:
        self.score_home += 1
        self.view.show_score(self.score_home, self.score_away)

    def goal_away(self) -> None:
        self.score_away += 1
        self.view.show_score(self.score_home, self.score_away)