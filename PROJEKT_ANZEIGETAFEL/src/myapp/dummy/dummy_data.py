from models.team import Team
from models.player import Player

TEAMS = [
    Team(id=1, name="Austria Wien"),
    Team(id=2, name="Rapid Wien")
]

PLAYERS = [
    Player(id=1, team_id=1, vorname="Dejan", nachname="Radonjic", nummer=60, bild_url="https://picsum.photos/100?1"),
    Player(id=2, team_id=1, vorname="Nikolas", nachname="Wurmbrand", nummer=40, bild_url="https://picsum.photos/100?2"),
    # … bis 40 Spieler

]


