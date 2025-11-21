import sqlite3
from typing import List
from contracts.ports import DatabasePort
from models.team import Team
from models.player import Player


class SQLiteDB(DatabasePort):
    """Echter SQLite-Datenbankadapter."""

    def _init_(self, db_path: str):
        self.conn = sqlite3.connect(db_path)
        self.conn.row_factory = sqlite3.Row

    def get_teams(self) -> List[Team]:
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM teams")
        rows = cur.fetchall()
        return [Team(**row) for row in rows]

    def get_team(self, team_id: int) -> Team:
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM teams WHERE id = ?", (team_id,))
        row = cur.fetchone()
        return Team(**row)

    def get_players(self, team_id: int) -> List[Player]:
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM players WHERE team_id = ?", (team_id,))
        rows = cur.fetchall()
        return [Player(**row) for row in rows]

    def get_player(self, player_id: int) -> Player:
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM players WHERE id = ?", (player_id,))
        row = cur.fetchone()
        return Player(**row)