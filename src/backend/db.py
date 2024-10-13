import sqlite3

from ._pathes import local_share_dir
from ._dish import Dish


class HandleDB:
    def __init__(self) -> None:
        self.conn = sqlite3.connect("calories.db")
        self.cursor = self.conn.cursor()
        self._create_tables()

    def execute(self, cmd: str, parameters=()):
        self.cursor.execute(cmd, parameters)
        self.conn.commit()

    def _create_tables(self):
        self.execute('''
        CREATE TABLE IF NOT EXISTS dishes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE,
            calories REAL NOT NULL,
            protein REAL NOT NULL,
            fats REAL NOT NULL,
            carbohydrates REAL NOT NULL
        )
    ''')

        self.execute('''
        CREATE TABLE IF NOT EXISTS consumption (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            dish_id INTEGER NOT NULL,
            date TEXT NOT NULL,
            FOREIGN KEY (dish_id) REFERENCES dishes (id)
        )
    ''')

    def add_dish(self, dish: Dish):
        try:

            self.execute('''
            INSERT INTO dishes (name, calories, protein, fats, carbohydrates)
            VALUES (?, ?, ?, ?, ?)
        ''', (dish["name"], dish["calories"], dish["protein"], dish["fats"], dish["carbohydrates"]))
        except sqlite3.IntegrityError:
            print("Ошибка: Блюдо с таким именем уже существует.")

    def close(self):
        self.conn.close()
