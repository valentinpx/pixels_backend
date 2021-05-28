import sqlite3
from pixel import Pixel

# Class to interact with database
class Database:
    def __init__(self, path):
        self.con = sqlite3.connect(path)

    def get_pixels(self):
        dest = []
        cur = self.con.cursor()

        for el in cur.execute("SELECT * FROM pixel ORDER BY id"):
            dest.append(Pixel(el))
        return dest
