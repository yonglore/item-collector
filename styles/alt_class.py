from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QApplication
from PyQt6.QtGui import QIcon
import models
from item import item_class_alt


class Alt(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi('styles_ui/alt.ui', self)

        self.item_category = 0

        db = models.Alt_db()

        self.pendants = db.add_pendants()
        self.pend_index = 0
        self.pend_icon = self.pendants[self.pend_index]

        self.tops = db.add_tops()
        self.top_index = 0
        self.top_icon = self.tops[self.top_index]

        self.bots = db.add_bots()
        self.bot_index = 0
        self.bot_icon = self.bots[self.bot_index]

        self.socks = db.add_socks()
        self.sock_index = 0
        self.socks_icon = self.socks[self.sock_index]

        self.shoes = db.add_shoes()
        self.shoes_index = 0
        self.shoes_icon = self.shoes[self.shoes_index]

        self.initUI()

    def initUI(self):
        self.alt_back.clicked.connect(self.back_func)

        self.alt_pendant.setIcon(QIcon('pictures/alt/pendant/drain pendant.png'))
        self.alt_top.setIcon(QIcon('pictures/alt/top/faith t-shirt.png'))
        self.alt_bot.setIcon(QIcon('pictures/alt/bot/baggy jeans.png'))
        self.alt_socks.setIcon(QIcon('pictures/alt/socks/hello kitty socks.png'))
        self.alt_shoes.setIcon(QIcon('pictures/alt/shoes/highest boots.png'))

        self.alt_pendant_next.clicked.connect(self.pend_next_func)
        self.alt_pendant_prev.clicked.connect(self.pend_prev_func)

        self.alt_top_next.clicked.connect(self.top_next_func)
        self.alt_top_prev.clicked.connect(self.top_prev_func)

        self.alt_bot_next.clicked.connect(self.bot_next_func)
        self.alt_bot_prev.clicked.connect(self.bot_prev_func)

        self.alt_socks_next.clicked.connect(self.socks_next_func)
        self.alt_socks_prev.clicked.connect(self.socks_prev_func)

        self.alt_shoes_next.clicked.connect(self.shoes_next_func)
        self.alt_shoes_prev.clicked.connect(self.shoes_prev_func)

        self.item = item_class_alt.ItemBuyAlt(self)
        self.item.hide()

        self.alt_pendant.clicked.connect(self.pend_check)
        self.alt_pendant.clicked.connect(self.item_change)

        self.alt_top.clicked.connect(self.top_check)
        self.alt_top.clicked.connect(self.item_change)

        self.alt_bot.clicked.connect(self.bot_check)
        self.alt_bot.clicked.connect(self.item_change)

        self.alt_socks.clicked.connect(self.socks_check)
        self.alt_socks.clicked.connect(self.item_change)

        self.alt_shoes.clicked.connect(self.shoes_check)
        self.alt_shoes.clicked.connect(self.item_change)

    def pend_check(self):
        self.item_category = 0

    def top_check(self):
        self.item_category = 1

    def bot_check(self):
        self.item_category = 2

    def socks_check(self):
        self.item_category = 3

    def shoes_check(self):
        self.item_category = 4

    def get_item(self):
        if self.item_category == 0:
            return self.pend_icon
        elif self.item_category == 1:
            return self.top_icon
        elif self.item_category == 2:
            return self.bot_icon
        elif self.item_category == 3:
            return self.socks_icon
        else:
            return self.shoes_icon

    def item_change(self):
        self.parent().item_alt.show()
        self.parent().change_size(1051, 724)
        self.hide()

    def pend_next_func(self):
        if self.pend_index == len(self.pendants) - 1:
            self.pend_index = -1
        self.pend_index += 1
        self.alt_pendant.setIcon(QIcon(f'pictures/alt/pendant/{self.pendants[self.pend_index]}.png'))
        self.pend_icon = self.pendants[self.pend_index]

    def pend_prev_func(self):
        if self.pend_index == 0:
            self.pend_index = len(self.pendants)
        self.pend_index -= 1
        self.alt_pendant.setIcon(QIcon(f'pictures/alt/pendant/{self.pendants[self.pend_index]}.png'))
        self.pend_icon = self.pendants[self.pend_index]

    def top_next_func(self):
        if self.top_index == len(self.tops) - 1:
            self.top_index = -1
        self.top_index += 1
        self.alt_top.setIcon(QIcon(f'pictures/alt/top/{self.tops[self.top_index]}.png'))
        self.top_icon = self.tops[self.top_index]

    def top_prev_func(self):
        if self.top_index == 0:
            self.top_index = len(self.tops)
        self.top_index -= 1
        self.alt_top.setIcon(QIcon(f'pictures/alt/top/{self.tops[self.top_index]}.png'))
        self.top_icon = self.tops[self.top_index]

    def bot_next_func(self):
        if self.bot_index == len(self.bots) - 1:
            self.bot_index = -1
        self.bot_index += 1
        self.alt_bot.setIcon(QIcon(f'pictures/alt/bot/{self.bots[self.bot_index]}.png'))
        self.bot_icon = self.bots[self.bot_index]

    def bot_prev_func(self):
        if self.bot_index == 0:
            self.bot_index = len(self.bots)
        self.bot_index -= 1
        self.alt_bot.setIcon(QIcon(f'pictures/alt/bot/{self.bots[self.bot_index]}.png'))
        self.bot_icon = self.bots[self.bot_index]

    def socks_next_func(self):
        if self.sock_index == len(self.socks) - 1:
            self.sock_index = -1
        self.sock_index += 1
        self.alt_socks.setIcon(QIcon(f'pictures/alt/socks/{self.socks[self.sock_index]}.png'))
        self.socks_icon = self.socks[self.sock_index]

    def socks_prev_func(self):
        if self.sock_index == 0:
            self.sock_index = len(self.socks)
        self.sock_index -= 1
        self.alt_socks.setIcon(QIcon(f'pictures/alt/socks/{self.socks[self.sock_index]}.png'))
        self.socks_icon = self.socks[self.sock_index]

    def shoes_next_func(self):
        if self.shoes_index == len(self.shoes) - 1:
            self.shoes_index = -1
        self.shoes_index += 1
        self.alt_shoes.setIcon(QIcon(f'pictures/alt/shoes/{self.shoes[self.shoes_index]}.png'))
        self.shoes_icon = self.shoes[self.shoes_index]

    def shoes_prev_func(self):
        if self.shoes_index == 0:
            self.shoes_index = len(self.shoes)
        self.shoes_index -= 1
        self.alt_shoes.setIcon(QIcon(f'pictures/alt/shoes/{self.shoes[self.shoes_index]}.png'))
        self.shoes_icon = self.shoes[self.shoes_index]

    def back_func(self):
        self.parent().intro_window.show()
        self.parent().setGeometry(100, 100, 532, 381)
        self.hide()
