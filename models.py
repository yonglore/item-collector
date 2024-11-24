import sqlite3
from PIL import Image


class Database:
    def __init__(self):
        self.con = sqlite3.connect('outfit.sqlite')
        self.cur = self.con.cursor()


class Alt_db(Database):
    def __init__(self):
        super().__init__()

    def get_favourites(self):
        favs = self.cur.execute("""
        SELECT Name FROM Alt
        WHERE favourite = 1
        """).fetchall()

        res = []
        for elem in favs:
            res.append(*elem)
        return res

    def add_favourites(self, item):
        self.cur.execute(f"""
        UPDATE Alt
        SET favourite = 1
        WHERE Name ='{item}'
        """)
        self.con.commit()

        # image = Image.open()

    def remove_favourites(self, item):
        self.cur.execute(f"""
        UPDATE Alt
        SET favourite = 0
        WHERE Name = '{item}'
        """)
        self.con.commit()

    def get_item_url(self, item):
        con = sqlite3.connect('outfit.sqlite')
        cur = con.cursor()
        a = cur.execute(f"""
        
        SELECT Link FROM Alt
        WHERE Name = '{item}'
        """).fetchall()

        res = a[0][0]
        return res

    def add_pendants(self):
        pendants = self.cur.execute("""
        SELECT Name FROM Alt
        WHERE Type = 'pendant'
        """).fetchall()

        res = []
        for elem in pendants:
            res.append(*elem)
        return res

    def add_tops(self):
        tops = self.cur.execute("""
                SELECT Name FROM Alt
                WHERE Type = 'top'
                """).fetchall()

        res = []
        for elem in tops:
            res.append(*elem)
        return res

    def add_bots(self):
        bots = self.cur.execute("""
                        SELECT Name FROM Alt
                        WHERE Type = 'bot'
                        """).fetchall()

        res = []
        for elem in bots:
            res.append(*elem)
        return res

    def add_socks(self):
        socks = self.cur.execute("""
                        SELECT Name FROM Alt
                        WHERE Type = 'socks'
                        """).fetchall()

        res = []
        for elem in socks:
            res.append(*elem)
        return res

    def add_shoes(self):
        shoes = self.cur.execute("""
                        SELECT Name FROM Alt
                        WHERE Type = 'shoes'
                        """).fetchall()

        res = []
        for elem in shoes:
            res.append(*elem)
        return res

    def end(self):
        self.con.close()


class DeadInside_db(Database):
    def __init__(self):
        super().__init__()

    def get_favourites(self):
        favs = self.cur.execute("""
        SELECT Name FROM Dead_inside
        WHERE favourite = 1
        """).fetchall()

        res = []
        for elem in favs:
            res.append(*elem)
        return res

    def get_item_url(self, item):
        con = sqlite3.connect('outfit.sqlite')
        cur = con.cursor()
        a = cur.execute(f"""

        SELECT Link FROM Dead_inside
        WHERE Name = '{item}'
        """).fetchall()

        res = a[0][0]
        return res

    def add_accessories(self):
        accessories = self.cur.execute("""
        SELECT Name FROM Dead_inside
        WHERE Type = 'accessories'
        """).fetchall()

        res = []
        for elem in accessories:
            res.append(*elem)
        return res

    def add_top(self):
        tops = self.cur.execute("""
        SELECT Name FROM Dead_inside
        WHERE Type = 'top'
        """).fetchall()

        res = []
        for elem in tops:
            res.append(*elem)
        return res

    def add_bot(self):
        bots = self.cur.execute("""
        SELECT Name FROM Dead_inside
        WHERE Type = 'bot'
        """).fetchall()

        res = []
        for elem in bots:
            res.append(*elem)
        return res

    def add_socks(self):
        socks = self.cur.execute("""
        SELECT Name FROM Dead_inside
        WHERE Type = 'socks'
        """).fetchall()

        res = []
        for elem in socks:
            res.append(*elem)
        return res

    def add_shoes(self):
        shoes = self.cur.execute("""
        SELECT Name FROM Dead_inside
        WHERE Type = 'shoes'
        """).fetchall()

        res = []
        for elem in shoes:
            res.append(*elem)
        return res

    def end(self):
        self.con.close()


class OldMoney_db(Database):
    def __init__(self):
        super().__init__()

    def get_favourites(self):
        favs = self.cur.execute("""
        SELECT Name FROM Old_money
        WHERE favourite = 1
        """).fetchall()

        res = []
        for elem in favs:
            res.append(*elem)
        return res

    def get_item_url(self, item):
        con = sqlite3.connect('outfit.sqlite')
        cur = con.cursor()
        a = cur.execute(f"""

        SELECT Link FROM Old_money
        WHERE Name = '{item}'
        """).fetchall()

        res = a[0][0]
        return res

    def add_top(self):
        a = self.cur.execute("""
        SELECT Name FROM Old_money
        WHERE Type = 'top'
        """).fetchall()

        res = []
        for elem in a:
            res.append(*elem)
        return res

    def add_watch(self):
        a = self.cur.execute("""
        SELECT Name FROM Old_money
        WHERE Type = 'watch'
        """).fetchall()

        res = []
        for elem in a:
            res.append(*elem)
        return res

    def add_bag(self):
        a = self.cur.execute("""
        SELECT Name FROM Old_money
        WHERE Type = 'bag'
        """).fetchall()

        res = []
        for elem in a:
            res.append(*elem)
        return res

    def add_bot(self):
        a = self.cur.execute("""
        SELECT Name FROM Old_money
        WHERE Type = 'bot'
        """).fetchall()

        res = []
        for elem in a:
            res.append(*elem)
        return res

    def add_shoes(self):
        a = self.cur.execute("""
        SELECT Name FROM Old_money
        WHERE Type = 'shoes'
        """).fetchall()

        res = []
        for elem in a:
            res.append(*elem)
        return res

    def end(self):
        self.con.close()


class Viperr_db(Database):
    def __init__(self):
        super().__init__()

    def get_favourites(self):
        favs = self.cur.execute("""
        SELECT Name FROM Viperr
        WHERE favourite = 1
        """).fetchall()

        res = []
        for elem in favs:
            res.append(*elem)
        return res

    def get_item_url(self, item):
        con = sqlite3.connect('outfit.sqlite')
        cur = con.cursor()
        a = cur.execute(f"""
        SELECT Link FROM Viperr
        WHERE Name = '{item}'
        """).fetchall()

        res = a[0][0]
        return res

    def add_glasses(self):
        a = self.cur.execute("""
        SELECT Name FROM Viperr
        WHERE Type = 'glasses'
        """).fetchall()

        res = []
        for elem in a:
            res.append(*elem)
        return res

    def add_top(self):
        a = self.cur.execute("""
        SELECT Name FROM Viperr
        WHERE Type = 'top'
        """).fetchall()

        res = []
        for elem in a:
            res.append(*elem)
        return res

    def add_belt(self):
        a = self.cur.execute("""
        SELECT Name FROM Viperr
        WHERE Type = 'belt'
        """).fetchall()

        res = []
        for elem in a:
            res.append(*elem)
        return res

    def add_bot(self):
        a = self.cur.execute("""
        SELECT Name FROM Viperr
        WHERE Type = 'bot'
        """).fetchall()

        res = []
        for elem in a:
            res.append(*elem)
        return res

    def add_shoes(self):
        a = self.cur.execute("""
        SELECT Name FROM Viperr
        WHERE Type = 'shoes'
        """).fetchall()

        res = []
        for elem in a:
            res.append(*elem)
        return res

    def end(self):
        self.con.close()


class Y2k_db(Database):
    def __init__(self):
        super().__init__()

    def get_favourites(self):
        favs = self.cur.execute("""
        SELECT Name FROM Y2k
        WHERE favourite = 1
        """).fetchall()

        res = []
        for elem in favs:
            res.append(*elem)
        return res

    def get_item_url(self, item):
        con = sqlite3.connect('outfit.sqlite')
        cur = con.cursor()
        a = cur.execute(f"""
        SELECT Link FROM Y2k
        WHERE Name = '{item}'
        """).fetchall()

        res = a[0][0]
        return res

    def add_hat(self):
        a = self.cur.execute("""
        SELECT Name FROM Y2k
        WHERE Type = 'hat'
        """).fetchall()

        res = []
        for elem in a:
            res.append(*elem)
        return res

    def add_top(self):
        a = self.cur.execute("""
        SELECT Name FROM Y2k
        WHERE Type = 'top'
        """).fetchall()

        res = []
        for elem in a:
            res.append(*elem)
        return res

    def add_belt(self):
        a = self.cur.execute("""
        SELECT Name FROM Y2k
        WHERE Type = 'belt'
        """).fetchall()

        res = []
        for elem in a:
            res.append(*elem)
        return res

    def add_bot(self):
        a = self.cur.execute("""
        SELECT Name FROM Y2k
        WHERE Type = 'bot'
        """).fetchall()

        res = []
        for elem in a:
            res.append(*elem)
        return res

    def add_shoes(self):
        a = self.cur.execute("""
        SELECT Name FROM Y2k
        WHERE Type = 'shoes'
        """).fetchall()

        res = []
        for elem in a:
            res.append(*elem)
        return res

    def end(self):
        self.con.close()
