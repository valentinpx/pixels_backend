import sqlite3
from pixel import Pixel

TABLE = "pixel"

# Class to interact with database
class Database:
    def __init__(self, path):
        self.con = sqlite3.connect(path)
    
    def __dek__(self):
        self.con.close()

    def get_pixels(self):
        dest = []
        cur = self.con.cursor()

        for el in cur.execute(f"SELECT * FROM {TABLE} ORDER BY id"):
            dest.append(Pixel(el))
        return dest
    
    def get_pixel(self, id):
        cur = self.con.cursor()
        res = cur.execute(f"SELECT * FROM {TABLE} WHERE id=:id", {"id": id}).fetchone()

        if (res == None):
            return None
        return Pixel(res)
    
    def set_pixel(self, id, color):
        cur = self.con.cursor()

        if (self.get_pixel(id) == None):
            return False
        cur.execute(f"UPDATE {TABLE} SET color=:color WHERE ID=:id", {"color": color, "id": id})
        self.con.commit()
        return True
