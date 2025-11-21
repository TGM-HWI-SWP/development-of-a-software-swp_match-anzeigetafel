from models.team import Team
from models.player import Player

TEAMS = [
    Team(id=1, name="FC Lions"),
    Team(id=2, name="Raptors United")
]

PLAYERS = [
    Player(id=1, team_id=1, vorname="Lukas", nachname="Meier", nummer=1, bild_url="https://picsum.photos/100?1"),
    Player(id=2, team_id=1, vorname="Jonas", nachname="Keller", nummer=2, bild_url="https://picsum.photos/100?2"),
    # … bis 40 Spieler
]