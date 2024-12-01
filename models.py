import sqlite3
from PIL import Image


class Database:
    def __init__(self):
        self.con = sqlite3.connect('outfit.sqlite')
        self.cur = self.con.cursor()


class FavouriteOutfits_db(Database):
    def __init__(self):
        super().__init__()

    def get_item1(self):
        pendants = self.cur.execute("""
        SELECT item_1 FROM Favourites_outfits
        """).fetchall()

        res = []
        for elem in pendants:
            res.append(*elem)
        return res

    def get_item2(self):
        pendants = self.cur.execute("""
        SELECT item_2 FROM Favourites_outfits
        """).fetchall()

        res = []
        for elem in pendants:
            res.append(*elem)
        return res

    def get_item3(self):
        pendants = self.cur.execute("""
        SELECT item_3 FROM Favourites_outfits
        """).fetchall()

        res = []
        for elem in pendants:
            res.append(*elem)
        return res

    def get_item4(self):
        pendants = self.cur.execute("""
        SELECT item_4 FROM Favourites_outfits
        """).fetchall()

        res = []
        for elem in pendants:
            res.append(*elem)
        return res

    def get_item5(self):
        pendants = self.cur.execute("""
        SELECT item_5 FROM Favourites_outfits
        """).fetchall()

        res = []
        for elem in pendants:
            res.append(*elem)
        return res

    def index_to_outfit(self, index):
        items = self.cur.execute(f"""
                SELECT * FROM Favourites_outfits
                WHERE id = '{index}'
                """).fetchall()

        res = []
        for elem in items:
            for i in elem:
                res.append(i)
        return res

    def get_index(self):
        items = self.cur.execute("""
                SELECT id FROM Favourites_outfits
                """).fetchall()

        res = []
        for elem in items:
            for i in elem:
                res.append(i)
        return res

    def add_outfit(self, item1, item2, item3, item4, item5, style):
        if (item1 not in self.get_item1() or item2 not in self.get_item2() or item3 not in self.get_item3()
                or item4 not in self.get_item4() or item5 not in self.get_item5()):
            self.cur.execute("""
                INSERT INTO Favourites_outfits(item_1, item_2, item_3, item_4, item_5, style)
                VALUES (?,?,?,?,?,?);
                """, (item1, item2, item3, item4, item5, style))
            self.con.commit()

    def delete_outfit(self, index):
        self.cur.execute(f"""
            DELETE
            FROM Favourites_outfits
            WHERE id = '{index}';
            """)
        self.con.commit()

    def get_items(self):
        items = self.cur.execute("""
        SELECT * FROM Favourites_outfits
        """).fetchall()

        res = []
        for elem in items:
            for i in elem:
                res.append(i)
        return res


class Alt_db(Database):
    def __init__(self):
        super().__init__()

    def get_names(self):
        names = self.cur.execute("""
        SELECT Name FROM Alt
        """).fetchall()

        res = []
        for elem in names:
            res.append(*elem)
        return res

    def get_favourites(self):
        favs = self.cur.execute("""
        SELECT Name FROM Alt
        WHERE favourite = 1
        """).fetchall()

        res = []
        for elem in favs:
            res.append(*elem)
        return res

    def get_category(self, item):
        category = self.cur.execute(f"""
        SELECT Type FROM Alt
        WHERE Name = '{item}'
        """).fetchone()
        return category[0]

    def add_favourites(self, item, category):
        self.cur.execute(f"""
        UPDATE Alt
        SET favourite = 1
        WHERE Name ='{item}'
        """)
        self.con.commit()

        image = Image.open(f'pictures/alt/{category}/{item}.png')
        image.save(f'favourites/pics/{item}.png')

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

    def get_names(self):
        names = self.cur.execute("""
        SELECT Name FROM Dead_inside
        """).fetchall()

        res = []
        for elem in names:
            res.append(*elem)
        return res

    def get_favourites(self):
        favs = self.cur.execute("""
        SELECT Name FROM Dead_inside
        WHERE favourite = 1
        """).fetchall()

        res = []
        for elem in favs:
            res.append(*elem)
        return res

    def get_category(self, item):
        category = self.cur.execute(f"""
        SELECT Type FROM Dead_inside
        WHERE Name = '{item}'
        """).fetchone()
        return category[0]

    def add_favourites(self, item, category):
        self.cur.execute(f"""
        UPDATE Dead_inside
        SET favourite = 1
        WHERE Name ='{item}'
        """)
        self.con.commit()

        image = Image.open(f'pictures/dead_inside/{category}/{item}.png')
        image.save(f'favourites/pics/{item}.png')

    def remove_favourites(self, item):
        self.cur.execute(f"""
        UPDATE Dead_inside
        SET favourite = 0
        WHERE Name = '{item}'
        """)
        self.con.commit()

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

    def get_names(self):
        names = self.cur.execute("""
        SELECT Name FROM Old_money
        """).fetchall()

        res = []
        for elem in names:
            res.append(*elem)
        return res

    def get_favourites(self):
        favs = self.cur.execute("""
        SELECT Name FROM Old_money
        WHERE favourite = 1
        """).fetchall()

        res = []
        for elem in favs:
            res.append(*elem)
        return res

    def get_category(self, item):
        category = self.cur.execute(f"""
        SELECT Type FROM Old_money
        WHERE Name = '{item}'
        """).fetchone()
        return category[0]

    def add_favourites(self, item, category):
        self.cur.execute(f"""
        UPDATE Old_money
        SET favourite = 1
        WHERE Name ='{item}'
        """)
        self.con.commit()

        image = Image.open(f'pictures/old_money/{category}/{item}.png')
        image.save(f'favourites/pics/{item}.png')

    def remove_favourites(self, item):
        self.cur.execute(f"""
        UPDATE Old_money
        SET favourite = 0
        WHERE Name = '{item}'
        """)
        self.con.commit()

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

    def get_names(self):
        names = self.cur.execute("""
        SELECT Name FROM Viperr
        """).fetchall()

        res = []
        for elem in names:
            res.append(*elem)
        return res

    def get_favourites(self):
        favs = self.cur.execute("""
        SELECT Name FROM Viperr
        WHERE favourite = 1
        """).fetchall()

        res = []
        for elem in favs:
            res.append(*elem)
        return res

    def get_category(self, item):
        category = self.cur.execute(f"""
        SELECT Type FROM Viperr
        WHERE Name = '{item}'
        """).fetchone()
        return category[0]

    def add_favourites(self, item, category):
        self.cur.execute(f"""
        UPDATE Viperr
        SET favourite = 1
        WHERE Name ='{item}'
        """)
        self.con.commit()

        image = Image.open(f'pictures/viperr/{category}/{item}.png')
        image.save(f'favourites/pics/{item}.png')

    def remove_favourites(self, item):
        self.cur.execute(f"""
        UPDATE Viperr
        SET favourite = 0
        WHERE Name = '{item}'
        """)
        self.con.commit()

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

    def get_names(self):
        names = self.cur.execute("""
        SELECT Name FROM Y2k
        """).fetchall()

        res = []
        for elem in names:
            res.append(*elem)
        return res

    def get_favourites(self):
        favs = self.cur.execute("""
        SELECT Name FROM Y2k
        WHERE favourite = 1
        """).fetchall()

        res = []
        for elem in favs:
            res.append(*elem)
        return res

    def get_category(self, item):
        category = self.cur.execute(f"""
        SELECT Type FROM Y2k
        WHERE Name = '{item}'
        """).fetchone()
        return category[0]

    def add_favourites(self, item, category):
        self.cur.execute(f"""
        UPDATE Y2k
        SET favourite = 1
        WHERE Name ='{item}'
        """)
        self.con.commit()

        image = Image.open(f'pictures/y2k/{category}/{item}.png')
        image.save(f'favourites/pics/{item}.png')

    def remove_favourites(self, item):
        self.cur.execute(f"""
        UPDATE Y2k
        SET favourite = 0
        WHERE Name = '{item}'
        """)
        self.con.commit()

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
