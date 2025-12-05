from myapp.contracts.ports import DBControllerPort

class UserController:
    """Beispiel-Controller, der mit der Datenbank interagiert."""

    def __init__(self, db: DBControllerPort):
        self.db = db

    def add_user(self, user_data):
        self.db.write_data(user_data)

    def list_users(self):
        return self.db.read_all()
    