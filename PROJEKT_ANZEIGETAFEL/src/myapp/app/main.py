from myapp.adapters.db_controller_dummy import InMemoryDB
from myapp.business_logic.controller import UserController

if __name__ == "__main__":
    db = InMemoryDB()
    controller = UserController(db)

    # Benutzer anzeigen
    print("Alle Benutzer:")
    for user in controller.list_users():
        print(user)

    # Neuen Benutzer hinzufügen
    controller.add_user({"id": 3, "name": "Lena Neu", "role": "User"})

    print("\nNach dem Hinzufügen:")
    for user in controller.list_users():
        print(user)
