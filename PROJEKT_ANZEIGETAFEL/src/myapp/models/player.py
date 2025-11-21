from pydantic import BaseModel


class Player(BaseModel):
    id: int
    team_id: int
    vorname: str
    nachname: str
    nummer: int
    bild_url: str