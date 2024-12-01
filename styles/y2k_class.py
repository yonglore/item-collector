from PyQt6 import uic
from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QIcon
import models
from item import item_class_y2k


class Y2k(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi('styles_ui/y2k.ui', self)

        self.item_category = 0

        db = models.Y2k_db()

        self.hats = db.add_hat()
        self.hat_index = 0
        self.hat_icon = self.hats[self.hat_index]

        self.tops = db.add_top()
        self.top_index = 0
        self.top_icon = self.tops[self.top_index]

        self.belts = db.add_belt()
        self.belt_index = 0
        self.belt_icon = self.belts[self.belt_index]

        self.bots = db.add_bot()
        self.bot_index = 0
        self.bot_icon = self.bots[self.bot_index]

        self.shoes_list = db.add_shoes()
        self.shoes_index = 0
        self.shoes_icon = self.shoes_list[self.shoes_index]

        self.initUI()

    def initUI(self):
        self.back.clicked.connect(self.back_func)

        self.hat.setIcon(QIcon('pictures/y2k/hat/star hat.png'))
        self.top.setIcon(QIcon('pictures/y2k/top/mr pickles t-shirt.png'))
        self.belt.setIcon(QIcon('pictures/y2k/belt/sonic belt.png'))
        self.bot.setIcon(QIcon('pictures/y2k/bot/pocket cargo.png'))
        self.shoes.setIcon(QIcon('pictures/y2k/shoes/new balance 1906R.png'))

        self.hat_next.setIcon(QIcon('styles/right arrow.png'))
        self.top_next.setIcon(QIcon('styles/right arrow.png'))
        self.bot_next.setIcon(QIcon('styles/right arrow.png'))
        self.belt_next.setIcon(QIcon('styles/right arrow.png'))
        self.shoes_next.setIcon(QIcon('styles/right arrow.png'))

        self.hat_prev.setIcon(QIcon('styles/left arrow.png'))
        self.top_prev.setIcon(QIcon('styles/left arrow.png'))
        self.bot_prev.setIcon(QIcon('styles/left arrow.png'))
        self.belt_prev.setIcon(QIcon('styles/left arrow.png'))
        self.shoes_prev.setIcon(QIcon('styles/left arrow.png'))

        self.hat_next.clicked.connect(self.hat_next_func)
        self.hat_prev.clicked.connect(self.hat_prev_func)

        self.top_next.clicked.connect(self.top_next_func)
        self.top_prev.clicked.connect(self.top_prev_func)

        self.belt_next.clicked.connect(self.belt_next_func)
        self.belt_prev.clicked.connect(self.belt_prev_func)

        self.bot_next.clicked.connect(self.bot_next_func)
        self.bot_prev.clicked.connect(self.bot_prev_func)

        self.shoes_next.clicked.connect(self.shoes_next_func)
        self.shoes_prev.clicked.connect(self.shoes_prev_func)

        self.item = item_class_y2k.ItemBuyY2k(self)
        self.item.hide()

        self.hat.clicked.connect(self.hat_check)
        self.hat.clicked.connect(self.item_change)

        self.top.clicked.connect(self.top_check)
        self.top.clicked.connect(self.item_change)

        self.belt.clicked.connect(self.belt_check)
        self.belt.clicked.connect(self.item_change)

        self.bot.clicked.connect(self.bot_check)
        self.bot.clicked.connect(self.item_change)

        self.shoes.clicked.connect(self.shoes_check)
        self.shoes.clicked.connect(self.item_change)

        self.favourites.clicked.connect(self.add_fav_outfit)

    def add_fav_outfit(self):
        outfits = models.FavouriteOutfits_db()
        outfits.add_outfit(self.hat_icon, self.top_icon, self.belt_icon, self.bot_icon, self.shoes_icon,
                           'y2k')

    def hat_check(self):
        self.item_category = 0

    def top_check(self):
        self.item_category = 1

    def belt_check(self):
        self.item_category = 2

    def bot_check(self):
        self.item_category = 3

    def shoes_check(self):
        self.item_category = 4

    def get_item(self):
        if self.item_category == 0:
            return self.hat_icon
        elif self.item_category == 1:
            return self.top_icon
        elif self.item_category == 2:
            return self.belt_icon
        elif self.item_category == 3:
            return self.bot_icon
        else:
            return self.shoes_icon

    def item_change(self):
        self.parent().item_y2k.show()
        self.parent().change_size(1051, 724)
        self.hide()

    def hat_next_func(self):
        if self.hat_index == len(self.hats) - 1:
            self.hat_index = -1
        self.hat_index += 1
        self.hat.setIcon(QIcon(f'pictures/y2k/hat/{self.hats[self.hat_index]}.png'))
        self.hat_icon = self.hats[self.hat_index]

    def hat_prev_func(self):
        if self.hat_index == 0:
            self.hat_index = len(self.hats)
        self.hat_index -= 1
        self.hat.setIcon(
            QIcon(f'pictures/y2k/hat/{self.hats[self.hat_index]}.png'))
        self.hat_icon = self.hats[self.hat_index]

    def top_next_func(self):
        if self.top_index == len(self.tops) - 1:
            self.top_index = -1
        self.top_index += 1
        self.top.setIcon(QIcon(f'pictures/y2k/top/{self.tops[self.top_index]}.png'))
        self.top_icon = self.tops[self.top_index]

    def top_prev_func(self):
        if self.top_index == 0:
            self.top_index = len(self.tops)
        self.top_index -= 1
        self.top.setIcon(
            QIcon(f'pictures/y2k/top/{self.tops[self.top_index]}.png'))
        self.top_icon = self.tops[self.top_index]

    def belt_next_func(self):
        if self.belt_index == len(self.belts) - 1:
            self.belt_index = -1
        self.belt_index += 1
        self.belt.setIcon(QIcon(f'pictures/y2k/belt/{self.belts[self.belt_index]}.png'))
        self.belt_icon = self.belts[self.belt_index]

    def belt_prev_func(self):
        if self.belt_index == 0:
            self.belt_index = len(self.belts)
        self.belt_index -= 1
        self.belt.setIcon(
            QIcon(f'pictures/y2k/belt/{self.belts[self.belt_index]}.png'))
        self.belt_icon = self.belts[self.belt_index]

    def bot_next_func(self):
        if self.bot_index == len(self.bots) - 1:
            self.bot_index = -1
        self.bot_index += 1
        self.bot.setIcon(QIcon(f'pictures/y2k/bot/{self.bots[self.bot_index]}.png'))
        self.bot_icon = self.bots[self.bot_index]

    def bot_prev_func(self):
        if self.bot_index == 0:
            self.bot_index = len(self.bots)
        self.bot_index -= 1
        self.bot.setIcon(
            QIcon(f'pictures/y2k/bot/{self.bots[self.bot_index]}.png'))
        self.bot_icon = self.bots[self.bot_index]

    def shoes_next_func(self):
        if self.shoes_index == len(self.shoes_list) - 1:
            self.shoes_index = -1
        self.shoes_index += 1
        self.shoes.setIcon(QIcon(f'pictures/y2k/shoes/{self.shoes_list[self.shoes_index]}.png'))
        self.shoes_icon = self.shoes_list[self.shoes_index]

    def shoes_prev_func(self):
        if self.shoes_index == 0:
            self.shoes_index = len(self.shoes_list)
        self.shoes_index -= 1
        self.shoes.setIcon(
            QIcon(f'pictures/y2k/shoes/{self.shoes_list[self.shoes_index]}.png'))
        self.shoes_icon = self.shoes_list[self.shoes_index]

    def back_func(self):
        self.parent().intro_window.show()
        self.parent().setGeometry(100, 100, 532, 381)
        self.hide()
