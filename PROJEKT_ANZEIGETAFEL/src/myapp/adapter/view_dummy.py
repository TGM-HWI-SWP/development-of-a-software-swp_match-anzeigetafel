class Team:
    def __init__(self, name):
        self.name = name



class DummyDB:
    def get_teams(self):
        return []  # Leer, damit die View nur zeigt, was der Benutzer eingibt
