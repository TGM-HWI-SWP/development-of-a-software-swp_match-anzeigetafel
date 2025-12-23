from adapter.db_dummy import DummyDB
from adapter.view_ctk import CTkView
from controller.controller import AnzeigetafelController

def main():
    db = DummyDB()  # Dummy-Datenbank
    controller = AnzeigetafelController(db)
    view = CTkView(controller)
    controller.set_view(view)

    # Optional: Dummy Teams laden
    controller.show_all_teams()

    view.mainloop()

if __name__ == "__main__":
    main()
