from PyQt6 import uic
from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QIcon
import models
from item import item_class_om


class OldMoney(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi('styles_ui/old money.ui', self)

        self.item_category = 0

        db = models.OldMoney_db()

        self.tops = db.add_top()
        self.top_index = 0
        self.top_icon = self.tops[self.top_index]

        self.watches = db.add_watch()
        self.watch_index = 0
        self.watch_icon = self.watches[self.watch_index]

        self.bags = db.add_bag()
        self.bag_index = 0
        self.bag_icon = self.bags[self.bag_index]

        self.bots = db.add_bot()
        self.bot_index = 0
        self.bot_icon = self.bots[self.bot_index]

        self.shoes_list = db.add_shoes()
        self.shoes_index = 0
        self.shoes_icon = self.shoes_list[self.shoes_index]

        self.initUI()

    def initUI(self):
        self.back.clicked.connect(self.back_func)

        self.top.setIcon(QIcon('pictures/old_money/top/green shirt.png'))
        self.watch.setIcon(QIcon('pictures/old_money/watch/green casio.png'))
        self.bag.setIcon(QIcon('pictures/old_money/bag/glitter bag.png'))
        self.bot.setIcon(QIcon('pictures/old_money/bot/red classic trouses.png'))
        self.shoes.setIcon(QIcon('pictures/old_money/shoes/adidas campus.png'))

        self.top_next.setIcon(QIcon('styles/right arrow.png'))
        self.watch_next.setIcon(QIcon('styles/right arrow.png'))
        self.bag_next.setIcon(QIcon('styles/right arrow.png'))
        self.bot_next.setIcon(QIcon('styles/right arrow.png'))
        self.shoes_next.setIcon(QIcon('styles/right arrow.png'))

        self.top_prev.setIcon(QIcon('styles/left arrow.png'))
        self.watch_prev.setIcon(QIcon('styles/left arrow.png'))
        self.bag_prev.setIcon(QIcon('styles/left arrow.png'))
        self.bot_prev.setIcon(QIcon('styles/left arrow.png'))
        self.shoes_prev.setIcon(QIcon('styles/left arrow.png'))

        self.top_next.clicked.connect(self.top_next_func)
        self.top_prev.clicked.connect(self.top_prev_func)

        self.watch_next.clicked.connect(self.watch_next_func)
        self.watch_prev.clicked.connect(self.watch_prev_func)

        self.bag_next.clicked.connect(self.bag_next_func)
        self.bag_prev.clicked.connect(self.bag_prev_func)

        self.bot_next.clicked.connect(self.bot_next_func)
        self.bot_prev.clicked.connect(self.bot_prev_func)

        self.shoes_next.clicked.connect(self.shoes_next_func)
        self.shoes_prev.clicked.connect(self.shoes_prev_func)

        self.item = item_class_om.ItemBuyOM(self)
        self.item.hide()

        self.top.clicked.connect(self.top_check)
        self.top.clicked.connect(self.item_change)

        self.watch.clicked.connect(self.watch_check)
        self.watch.clicked.connect(self.item_change)

        self.bag.clicked.connect(self.bag_check)
        self.bag.clicked.connect(self.item_change)

        self.bot.clicked.connect(self.bot_check)
        self.bot.clicked.connect(self.item_change)

        self.shoes.clicked.connect(self.shoes_check)
        self.shoes.clicked.connect(self.item_change)

        self.favourites.clicked.connect(self.add_fav_outfit)

    def add_fav_outfit(self):
        outfits = models.FavouriteOutfits_db()
        outfits.add_outfit(self.top_icon, self.watch_icon, self.bag_icon, self.bot_icon, self.shoes_icon,
                           'old_money')

    def top_check(self):
        self.item_category = 0

    def watch_check(self):
        self.item_category = 1

    def bag_check(self):
        self.item_category = 2

    def bot_check(self):
        self.item_category = 3

    def shoes_check(self):
        self.item_category = 4

    def get_item(self):
        if self.item_category == 0:
            return self.top_icon
        elif self.item_category == 1:
            return self.watch_icon
        elif self.item_category == 2:
            return self.bag_icon
        elif self.item_category == 3:
            return self.bot_icon
        else:
            return self.shoes_icon

    def item_change(self):
        self.parent().item_om.show()
        self.parent().change_size(1051, 724)
        self.hide()

    def top_next_func(self):
        if self.top_index == len(self.tops) - 1:
            self.top_index = -1
        self.top_index += 1
        self.top.setIcon(QIcon(f'pictures/old_money/top/{self.tops[self.top_index]}.png'))
        self.top_icon = self.tops[self.top_index]

    def top_prev_func(self):
        if self.top_index == 0:
            self.top_index = len(self.tops)
        self.top_index -= 1
        self.top.setIcon(
            QIcon(f'pictures/old_money/top/{self.tops[self.top_index]}.png'))
        self.top_icon = self.tops[self.top_index]

    def watch_next_func(self):
        if self.watch_index == len(self.watches) - 1:
            self.watch_index = -1
        self.watch_index += 1
        self.watch.setIcon(QIcon(f'pictures/old_money/watch/{self.watches[self.watch_index]}.png'))
        self.watch_icon = self.watches[self.watch_index]

    def watch_prev_func(self):
        if self.watch_index == 0:
            self.watch_index = len(self.watches)
        self.watch_index -= 1
        self.watch.setIcon(
            QIcon(f'pictures/old_money/watch/{self.watches[self.watch_index]}.png'))
        self.watch_icon = self.watches[self.watch_index]

    def bag_next_func(self):
        if self.bag_index == len(self.bags) - 1:
            self.bag_index = -1
        self.bag_index += 1
        self.bag.setIcon(QIcon(f'pictures/old_money/bag/{self.bags[self.bag_index]}.png'))
        self.bag_icon = self.bags[self.bag_index]

    def bag_prev_func(self):
        if self.bag_index == 0:
            self.bag_index = len(self.bags)
        self.bag_index -= 1
        self.bag.setIcon(
            QIcon(f'pictures/old_money/bag/{self.bags[self.bag_index]}.png'))
        self.bag_icon = self.bags[self.bag_index]

    def bot_next_func(self):
        if self.bot_index == len(self.bots) - 1:
            self.bot_index = -1
        self.bot_index += 1
        self.bot.setIcon(QIcon(f'pictures/old_money/bot/{self.bots[self.bot_index]}.png'))
        self.bot_icon = self.bots[self.bot_index]

    def bot_prev_func(self):
        if self.bot_index == 0:
            self.bot_index = len(self.bots)
        self.bot_index -= 1
        self.bot.setIcon(
            QIcon(f'pictures/old_money/bot/{self.bots[self.bot_index]}.png'))
        self.bot_icon = self.bots[self.bot_index]

    def shoes_next_func(self):
        if self.shoes_index == len(self.shoes_list) - 1:
            self.shoes_index = -1
        self.shoes_index += 1
        self.shoes.setIcon(QIcon(f'pictures/old_money/shoes/{self.shoes_list[self.shoes_index]}.png'))
        self.shoes_icon = self.shoes_list[self.shoes_index]

    def shoes_prev_func(self):
        if self.shoes_index == 0:
            self.shoes_index = len(self.shoes_list)
        self.shoes_index -= 1
        self.shoes.setIcon(
            QIcon(f'pictures/old_money/shoes/{self.shoes_list[self.shoes_index]}.png'))
        self.shoes_icon = self.shoes_list[self.shoes_index]

    def back_func(self):
        self.parent().intro_window.show()
        self.parent().setGeometry(100, 100, 532, 381)
        self.hide()
