from contracts.ports import ViewPort
from typing import List
from models.team import Team
from models.player import Player


class DummyView(ViewPort):
    """CLI-Version der GUI zum Testen."""

    def show_teams(self, teams: List[Team]) -> None:
        print("TEAMS:")
        for t in teams:
            print(f"- {t.name}")

    def show_players(self, players: List[Player]) -> None:
        print("SPIELER:")
        for p in players:
            print(f"{p.vorname} {p.nachname} (#{p.nummer})")

    def show_score(self, home: int, away: int) -> None:
        print(f"Spielstand: {home} : {away}")