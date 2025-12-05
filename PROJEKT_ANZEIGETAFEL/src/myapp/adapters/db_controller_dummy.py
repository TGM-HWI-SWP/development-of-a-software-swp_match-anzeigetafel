from myapp.contracts.ports import DBControllerPort
from myapp.dummies.dummy_data import get_dummy_data

class InMemoryDB(DBControllerPort):
    """Einfache In-Memory-Datenbank zum Testen."""

    def __init__(self):
        self._storage = {item["id"]: item for item in get_dummy_data()}

    def write_data(self, data):
        self._storage[data["id"]] = data

    def read_data(self, record_id):
        return self._storage.get(record_id, {})

    def read_all(self):
        return list(self._storage.values())
