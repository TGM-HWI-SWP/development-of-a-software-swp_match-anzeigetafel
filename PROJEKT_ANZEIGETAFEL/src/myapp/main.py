import controller.controller as cc
import inspect
print(">>> Controller geladen aus:", inspect.getfile(cc))


from adapter.db_dummy import DummyDB
from adapter.view_dummy import DummyView
from controller.controller import AnzeigetafelController


def main():
    db = DummyDB()           # später: SQLiteDB("stadion.db")
    view = DummyView()       # später: echte GUI view_ctk.py
    controller = AnzeigetafelController(db, view)

    # MVP Demo
    controller.show_all_teams()
    controller.show_players_of_team(1)
    controller.goal_home()
    controller.goal_away()


if __name__ == "__main__":
    main()




from adapter.view_ctk import CTkView


def main():
    app = CTkView()
    app.mainloop()


if __name__ == "__main__":
    main()
