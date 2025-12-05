from adapter.db_dummy import DummyDB # type: ignore
from adapter.view_dummy import DummyView # type: ignore
from controller.controller import AnzeigetafelController # type: ignore


def main():
    db = DummyDB()           # später: SQLiteDB("stadion.db")
    view = DummyView()       # später: echte GUI view_ctk.py
    controller = AnzeigetafelController(db, view)

    # MVP Demo
    controller.show_all_teams()
    controller.show_players_of_team(1)
    controller.goal_home()
    controller.goal_away()


if __name__ == "_main_":
    main()