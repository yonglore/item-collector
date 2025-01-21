from PyQt6 import uic
from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QIcon
import models
from item import item_class_viperr


class Viperr(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi('styles_ui/viperr.ui', self)

        self.item_category = 0

        db = models.Viperr_db()

        self.glasses_list = db.add_glasses()
        self.glasses_index = 0
        self.glasses_icon = self.glasses_list[self.glasses_index]

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

        self.glasses.setIcon(QIcon('pictures/viperr/glasses/balenciaga big glasses.png'))
        self.top.setIcon(QIcon('pictures/viperr/top/vultures hoodie.png'))
        self.belt.setIcon(QIcon('pictures/viperr/belt/gucci belt.png'))
        self.bot.setIcon(QIcon('pictures/viperr/bot/ripped jeans.png'))
        self.shoes.setIcon(QIcon('pictures/viperr/shoes/balenciaga defender.png'))

        self.glasses_next.setIcon(QIcon('styles/right arrow.png'))
        self.top_next.setIcon(QIcon('styles/right arrow.png'))
        self.bot_next.setIcon(QIcon('styles/right arrow.png'))
        self.belt_next.setIcon(QIcon('styles/right arrow.png'))
        self.shoes_next.setIcon(QIcon('styles/right arrow.png'))

        self.glasses_prev.setIcon(QIcon('styles/left arrow.png'))
        self.top_prev.setIcon(QIcon('styles/left arrow.png'))
        self.bot_prev.setIcon(QIcon('styles/left arrow.png'))
        self.belt_prev.setIcon(QIcon('styles/left arrow.png'))
        self.shoes_prev.setIcon(QIcon('styles/left arrow.png'))

        self.glasses_next.clicked.connect(self.glasses_next_func)
        self.glasses_prev.clicked.connect(self.glasses_prev_func)

        self.top_next.clicked.connect(self.top_next_func)
        self.top_prev.clicked.connect(self.top_prev_func)

        self.belt_next.clicked.connect(self.belt_next_func)
        self.belt_prev.clicked.connect(self.belt_prev_func)

        self.bot_next.clicked.connect(self.bot_next_func)
        self.bot_prev.clicked.connect(self.bot_prev_func)

        self.shoes_next.clicked.connect(self.shoes_next_func)
        self.shoes_prev.clicked.connect(self.shoes_prev_func)

        self.item = item_class_viperr.ItemBuyViperr(self)
        self.item.hide()

        self.glasses.clicked.connect(self.glasses_check)
        self.glasses.clicked.connect(self.item_change)

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
        outfits.add_outfit(self.glasses_icon, self.top_icon, self.belt_icon, self.bot_icon, self.shoes_icon,
                           'viperr')

    def glasses_check(self):
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
            return self.glasses_icon
        elif self.item_category == 1:
            return self.top_icon
        elif self.item_category == 2:
            return self.belt_icon
        elif self.item_category == 3:
            return self.bot_icon
        else:
            return self.shoes_icon

    def item_change(self):
        self.parent().item_viperr.show()
        self.parent().change_size(1051, 724)
        self.hide()

    def glasses_next_func(self):
        if self.glasses_index == len(self.glasses_list) - 1:
            self.glasses_index = -1
        self.glasses_index += 1
        self.glasses.setIcon(QIcon(f'pictures/viperr/glasses/{self.glasses_list[self.glasses_index]}.png'))
        self.glasses_icon = self.glasses_list[self.glasses_index]

    def glasses_prev_func(self):
        if self.glasses_index == 0:
            self.glasses_index = len(self.glasses_list)
        self.glasses_index -= 1
        self.glasses.setIcon(
            QIcon(f'pictures/viperr/glasses/{self.glasses_list[self.glasses_index]}.png'))
        self.glasses_icon = self.glasses_list[self.glasses_index]

    def top_next_func(self):
        if self.top_index == len(self.tops) - 1:
            self.top_index = -1
        self.top_index += 1
        self.top.setIcon(QIcon(f'pictures/viperr/top/{self.tops[self.top_index]}.png'))
        self.top_icon = self.tops[self.top_index]

    def top_prev_func(self):
        if self.top_index == 0:
            self.top_index = len(self.tops)
        self.top_index -= 1
        self.top.setIcon(
            QIcon(f'pictures/viperr/top/{self.tops[self.top_index]}.png'))
        self.top_icon = self.tops[self.top_index]

    def belt_next_func(self):
        if self.belt_index == len(self.belts) - 1:
            self.belt_index = -1
        self.belt_index += 1
        self.belt.setIcon(QIcon(f'pictures/viperr/belt/{self.belts[self.belt_index]}.png'))
        self.belt_icon = self.belts[self.belt_index]

    def belt_prev_func(self):
        if self.belt_index == 0:
            self.belt_index = len(self.belts)
        self.belt_index -= 1
        self.belt.setIcon(
            QIcon(f'pictures/viperr/belt/{self.belts[self.belt_index]}.png'))
        self.belt_icon = self.belts[self.belt_index]

    def bot_next_func(self):
        if self.bot_index == len(self.bots) - 1:
            self.bot_index = -1
        self.bot_index += 1
        self.bot.setIcon(QIcon(f'pictures/viperr/bot/{self.bots[self.bot_index]}.png'))
        self.bot_icon = self.bots[self.bot_index]

    def bot_prev_func(self):
        if self.bot_index == 0:
            self.bot_index = len(self.bots)
        self.bot_index -= 1
        self.bot.setIcon(
            QIcon(f'pictures/viperr/bot/{self.bots[self.bot_index]}.png'))
        self.bot_icon = self.bots[self.bot_index]

    def shoes_next_func(self):
        if self.shoes_index == len(self.shoes_list) - 1:
            self.shoes_index = -1
        self.shoes_index += 1
        self.shoes.setIcon(QIcon(f'pictures/viperr/shoes/{self.shoes_list[self.shoes_index]}.png'))
        self.shoes_icon = self.shoes_list[self.shoes_index]

    def shoes_prev_func(self):
        if self.shoes_index == 0:
            self.shoes_index = len(self.shoes_list)
        self.shoes_index -= 1
        self.shoes.setIcon(
            QIcon(f'pictures/viperr/shoes/{self.shoes_list[self.shoes_index]}.png'))
        self.shoes_icon = self.shoes_list[self.shoes_index]

    def back_func(self):
        self.parent().intro_window.show()
        self.parent().setGeometry(100, 100, 532, 381)
        self.hide()
