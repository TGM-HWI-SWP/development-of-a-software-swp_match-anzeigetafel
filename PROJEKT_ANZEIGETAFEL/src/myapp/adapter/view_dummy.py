class Team:
    def __init__(self, name):
        self.name = name

class DummyDB:
    def get_teams(self):
        return [Team("Team A"), Team("Team B"), Team("Team C")]
