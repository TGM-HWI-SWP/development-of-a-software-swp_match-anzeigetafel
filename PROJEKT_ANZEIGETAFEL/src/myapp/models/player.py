class Player:
    def __init__(self, name, nummer):
        self.name = name
        self.nummer = nummer
        self.tore = 0
        self.yellow_cards = 0
        self.is_on_field = True  # Startspieler = True, Bank = False
