from PyQt6 import uic
from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QIcon
import models
from item import item_class_di


class DeadInside(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi('styles_ui/dead inside.ui', self)

        self.item_category = 0

        db = models.DeadInside_db()

        self.accessories_list = db.add_accessories()
        self.accs_index = 0
        self.accs_icon = self.accessories_list[self.accs_index]

        self.tops = db.add_top()
        self.top_index = 0
        self.top_icon = self.tops[self.top_index]

        self.bots = db.add_bot()
        self.bot_index = 0
        self.bot_icon = self.bots[self.bot_index]

        self.socks_list = db.add_socks()
        self.socks_index = 0
        self.socks_icon = self.socks_list[self.socks_index]

        self.shoes_list = db.add_shoes()
        self.shoes_index = 0
        self.shoes_icon = self.shoes_list[self.shoes_index]

        self.initUI()

    def initUI(self):
        self.back.clicked.connect(self.back_func)

        self.accessories.setIcon(QIcon('pictures/dead_inside/accessories/zxc keychain.png'))
        self.top_btn.setIcon(QIcon('pictures/dead_inside/top/hikkamori kai t-shirt.png'))
        self.bot.setIcon(QIcon('pictures/dead_inside/bot/adidas juzo trouses.png'))
        self.socks.setIcon(QIcon('pictures/dead_inside/socks/zxc socks.png'))
        self.shoes.setIcon(QIcon('pictures/dead_inside/shoes/new rock.png'))

        self.accessories_next.clicked.connect(self.accs_next_func)
        self.accessories_prev.clicked.connect(self.accs_prev_func)

        self.top_next.clicked.connect(self.top_next_func)
        self.top_prev.clicked.connect(self.top_prev_func)

        self.bot_next.clicked.connect(self.bot_next_func)
        self.bot_prev.clicked.connect(self.bot_prev_func)

        self.socks_next.clicked.connect(self.socks_next_func)
        self.socks_prev.clicked.connect(self.socks_prev_func)

        self.shoes_next.clicked.connect(self.shoes_next_func)
        self.shoes_prev.clicked.connect(self.shoes_prev_func)

        self.item = item_class_di.ItemBuyDI(self)
        self.item.hide()

        self.accessories.clicked.connect(self.accessories_check)
        self.accessories.clicked.connect(self.item_change)

        self.top_btn.clicked.connect(self.top_check)
        self.top_btn.clicked.connect(self.item_change)

        self.bot.clicked.connect(self.bot_check)
        self.bot.clicked.connect(self.item_change)

        self.socks.clicked.connect(self.socks_check)
        self.socks.clicked.connect(self.item_change)

        self.shoes.clicked.connect(self.shoes_check)
        self.shoes.clicked.connect(self.item_change)

    def accessories_check(self):
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
            return self.accs_icon
        elif self.item_category == 1:
            return self.top_icon
        elif self.item_category == 2:
            return self.bot_icon
        elif self.item_category == 3:
            return self.socks_icon
        else:
            return self.shoes_icon

    def item_change(self):
        self.parent().item_di.show()
        self.parent().change_size(1051, 724)
        self.hide()

    def accs_next_func(self):
        if self.accs_index == len(self.accessories_list) - 1:
            self.accs_index = -1
        self.accs_index += 1
        self.accessories.setIcon(
            QIcon(f'pictures/dead_inside/accessories/{self.accessories_list[self.accs_index]}.png'))
        self.accs_icon = self.accessories_list[self.accs_index]

    def accs_prev_func(self):
        if self.accs_index == 0:
            self.accs_index = len(self.accessories_list)
        self.accs_index -= 1
        self.accessories.setIcon(
            QIcon(f'pictures/dead_inside/accessories/{self.accessories_list[self.accs_index]}.png'))
        self.accs_icon = self.accessories_list[self.accs_index]

    def top_next_func(self):
        if self.top_index == len(self.tops) - 1:
            self.top_index = -1
        self.top_index += 1
        self.top_btn.setIcon(QIcon(f'pictures/dead_inside/top/{self.tops[self.top_index]}.png'))
        self.top_icon = self.tops[self.top_index]

    def top_prev_func(self):
        if self.top_index == 0:
            self.top_index = len(self.tops)
        self.top_index -= 1
        self.top_btn.setIcon(
            QIcon(f'pictures/dead_inside/top/{self.tops[self.top_index]}.png'))
        self.top_icon = self.tops[self.top_index]

    def bot_next_func(self):
        if self.bot_index == len(self.bots) - 1:
            self.bot_index = -1
        self.bot_index += 1
        self.bot.setIcon(QIcon(f'pictures/dead_inside/bot/{self.bots[self.bot_index]}.png'))
        self.bot_icon = self.bots[self.bot_index]

    def bot_prev_func(self):
        if self.bot_index == 0:
            self.bot_index = len(self.bots)
        self.bot_index -= 1
        self.bot.setIcon(QIcon(f'pictures/dead_inside/bot/{self.bots[self.bot_index]}.png'))
        self.bot_icon = self.bots[self.bot_index]

    def socks_next_func(self):
        if self.socks_index == len(self.socks_list) - 1:
            self.socks_index = -1
        self.socks_index += 1
        self.socks.setIcon(QIcon(f'pictures/dead_inside/socks/{self.socks_list[self.socks_index]}.png'))
        self.socks_icon = self.socks_list[self.socks_index]

    def socks_prev_func(self):
        if self.socks_index == 0:
            self.socks_index = len(self.socks_list)
        self.socks_index -= 1
        self.socks.setIcon(QIcon(f'pictures/dead_inside/socks/{self.socks_list[self.socks_index]}.png'))
        self.socks_icon = self.socks_list[self.socks_index]

    def shoes_next_func(self):
        if self.shoes_index == len(self.shoes_list) - 1:
            self.shoes_index = -1
        self.shoes_index += 1
        self.shoes.setIcon(QIcon(f'pictures/dead_inside/shoes/{self.shoes_list[self.shoes_index]}.png'))
        self.shoes_icon = self.shoes_list[self.shoes_index]

    def shoes_prev_func(self):
        if self.shoes_index == 0:
            self.shoes_index = len(self.shoes_list)
        self.shoes_index -= 1
        self.shoes.setIcon(QIcon(f'pictures/dead_inside/shoes/{self.shoes_list[self.shoes_index]}.png'))
        self.shoes_icon = self.shoes_list[self.shoes_index]

    def back_func(self):
        self.parent().intro_window.show()
        self.parent().setGeometry(100, 100, 532, 381)
        self.hide()
