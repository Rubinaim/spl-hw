import sqlite3
import sys
from DAOs import *
from DTOs import *
import atexit


class Repository:

    def __init__(self):
        self.conn = sqlite3.connect(sys.argv[4])
        self.hats = Hats(self.conn)
        self.suppliers = Suppliers(self.conn)
        self.orders = Orders(self.conn)

    def close(self):
        self.conn.commit()
        self.conn.close()

    def create_tables(self,):
        self.conn.executescript("""
        CREATE TABLE suppliers(
            id INT PRIMARY KEY,
            name TEXT NOT NULL
            );
        CREATE TABLE hats(
            id INT PRIMARY KEY,
            topping TEXT NOT NULL,
            supplier INT NOT NULL REFERENCES suppliers(id),
            quantity INT NOT NULL
            );
        CREATE TABLE orders(
            id INT PRIMARY KEY,
            location INT NOT NULL,
            hat INT REFERENCES hats(id)
            );
        """)


repo = Repository()
repo.create_tables()
atexit.register(repo.close)
