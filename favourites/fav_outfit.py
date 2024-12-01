from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QApplication
from PyQt6.QtGui import QIcon
import models


class FavouriteOutfit(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi('favourites/fav_outfit.ui', self)

        self.initUI()

    def initUI(self):
        self.outfit_next.setIcon(QIcon('styles/right arrow.png'))
        self.outfit_prev.setIcon(QIcon('styles/left arrow.png'))

        self.back.clicked.connect(self.back_func)

        self.db = models.FavouriteOutfits_db()

        self.items = self.db.get_items()

        self.item_list = self.db.get_index()
        self.item_index = 0

        self.item_3.setIcon(QIcon('favourites/cross.png'))

        self.refresh.clicked.connect(self.refresh_page)
        self.outfit_next.clicked.connect(self.next_item)
        self.outfit_prev.clicked.connect(self.prev_item)
        self.delete_2.clicked.connect(self.remove_outfit)

    def remove_outfit(self):
        if self.item_list:
            self.db.delete_outfit(self.item_list[self.item_index])

    def next_item(self):
        if len(self.item_list) > 1:
            if self.item_index == len(self.item_list) - 1:
                self.item_index = -1
            self.item_index += 1
            icons = self.db.index_to_outfit(self.item_list[self.item_index])
            try:
                if icons[6] == 'alt':
                    self.item_1.setIcon(QIcon(f'pictures/alt/pendant/{icons[1]}.png'))
                    self.item_2.setIcon(QIcon(f'pictures/alt/top/{icons[2]}.png'))
                    self.item_3.setIcon(QIcon(f'pictures/alt/bot/{icons[3]}.png'))
                    self.item_4.setIcon(QIcon(f'pictures/alt/socks/{icons[4]}.png'))
                    self.item_5.setIcon(QIcon(f'pictures/alt/shoes/{icons[5]}.png'))
                elif icons[6] == 'dead_inside':
                    self.item_1.setIcon(QIcon(f'pictures/dead_inside/accessories/{icons[1]}.png'))
                    self.item_2.setIcon(QIcon(f'pictures/dead_inside/top/{icons[2]}.png'))
                    self.item_3.setIcon(QIcon(f'pictures/dead_inside/bot/{icons[3]}.png'))
                    self.item_4.setIcon(QIcon(f'pictures/dead_inside/socks/{icons[4]}.png'))
                    self.item_5.setIcon(QIcon(f'pictures/dead_inside/shoes/{icons[5]}.png'))
                elif icons[6] == 'old_money':
                    self.item_1.setIcon(QIcon(f'pictures/old_money/top/{icons[1]}.png'))
                    self.item_2.setIcon(QIcon(f'pictures/old_money/watch/{icons[2]}.png'))
                    self.item_3.setIcon(QIcon(f'pictures/old_money/bag/{icons[3]}.png'))
                    self.item_4.setIcon(QIcon(f'pictures/old_money/bot/{icons[4]}.png'))
                    self.item_5.setIcon(QIcon(f'pictures/old_money/shoes/{icons[5]}.png'))
                elif icons[6] == 'viperr':
                    self.item_1.setIcon(QIcon(f'pictures/viperr/glasses/{icons[1]}.png'))
                    self.item_2.setIcon(QIcon(f'pictures/viperr/top/{icons[2]}.png'))
                    self.item_3.setIcon(QIcon(f'pictures/viperr/belt/{icons[3]}.png'))
                    self.item_4.setIcon(QIcon(f'pictures/viperr/bot/{icons[4]}.png'))
                    self.item_5.setIcon(QIcon(f'pictures/viperr/shoes/{icons[5]}.png'))
                else:
                    self.item_1.setIcon(QIcon(f'pictures/y2k/hat/{icons[1]}.png'))
                    self.item_2.setIcon(QIcon(f'pictures/y2k/top/{icons[2]}.png'))
                    self.item_3.setIcon(QIcon(f'pictures/y2k/belt/{icons[3]}.png'))
                    self.item_4.setIcon(QIcon(f'pictures/y2k/bot/{icons[4]}.png'))
                    self.item_5.setIcon(QIcon(f'pictures/y2k/shoes/{icons[5]}.png'))
            except Exception:
                pass

    def prev_item(self):
        if len(self.item_list) > 1:
            if self.item_list:
                if self.item_index == 0:
                    self.item_index = len(self.item_list)
                self.item_index -= 1
                icons = self.db.index_to_outfit(self.item_list[self.item_index])
                try:
                    if icons[6] == 'alt':
                        self.item_1.setIcon(QIcon(f'pictures/alt/pendant/{icons[1]}.png'))
                        self.item_2.setIcon(QIcon(f'pictures/alt/top/{icons[2]}.png'))
                        self.item_3.setIcon(QIcon(f'pictures/alt/bot/{icons[3]}.png'))
                        self.item_4.setIcon(QIcon(f'pictures/alt/socks/{icons[4]}.png'))
                        self.item_5.setIcon(QIcon(f'pictures/alt/shoes/{icons[5]}.png'))
                    elif icons[6] == 'dead_inside':
                        self.item_1.setIcon(QIcon(f'pictures/dead_inside/accessories/{icons[1]}.png'))
                        self.item_2.setIcon(QIcon(f'pictures/dead_inside/top/{icons[2]}.png'))
                        self.item_3.setIcon(QIcon(f'pictures/dead_inside/bot/{icons[3]}.png'))
                        self.item_4.setIcon(QIcon(f'pictures/dead_inside/socks/{icons[4]}.png'))
                        self.item_5.setIcon(QIcon(f'pictures/dead_inside/shoes/{icons[5]}.png'))
                    elif icons[6] == 'old_money':
                        self.item_1.setIcon(QIcon(f'pictures/old_money/top/{icons[1]}.png'))
                        self.item_2.setIcon(QIcon(f'pictures/old_money/watch/{icons[2]}.png'))
                        self.item_3.setIcon(QIcon(f'pictures/old_money/bag/{icons[3]}.png'))
                        self.item_4.setIcon(QIcon(f'pictures/old_money/bot/{icons[4]}.png'))
                        self.item_5.setIcon(QIcon(f'pictures/old_money/shoes/{icons[5]}.png'))
                    elif icons[6] == 'viperr':
                        self.item_1.setIcon(QIcon(f'pictures/viperr/glasses/{icons[1]}.png'))
                        self.item_2.setIcon(QIcon(f'pictures/viperr/top/{icons[2]}.png'))
                        self.item_3.setIcon(QIcon(f'pictures/viperr/belt/{icons[3]}.png'))
                        self.item_4.setIcon(QIcon(f'pictures/viperr/bot/{icons[4]}.png'))
                        self.item_5.setIcon(QIcon(f'pictures/viperr/shoes/{icons[5]}.png'))
                    else:
                        self.item_1.setIcon(QIcon(f'pictures/y2k/hat/{icons[1]}.png'))
                        self.item_2.setIcon(QIcon(f'pictures/y2k/top/{icons[2]}.png'))
                        self.item_3.setIcon(QIcon(f'pictures/y2k/belt/{icons[3]}.png'))
                        self.item_4.setIcon(QIcon(f'pictures/y2k/bot/{icons[4]}.png'))
                        self.item_5.setIcon(QIcon(f'pictures/y2k/shoes/{icons[5]}.png'))
                except Exception:
                    pass

    def refresh_page(self):
        self.items = self.db.get_items()
        self.item_list = self.db.get_index()
        if self.items:
            if self.items[6] == 'alt':
                self.item_1.setIcon(QIcon(f'pictures/alt/pendant/{self.items[1]}.png'))
                self.item_2.setIcon(QIcon(f'pictures/alt/top/{self.items[2]}.png'))
                self.item_3.setIcon(QIcon(f'pictures/alt/bot/{self.items[3]}.png'))
                self.item_4.setIcon(QIcon(f'pictures/alt/socks/{self.items[4]}.png'))
                self.item_5.setIcon(QIcon(f'pictures/alt/shoes/{self.items[5]}.png'))
            elif self.items[6] == 'dead_inside':
                self.item_1.setIcon(QIcon(f'pictures/dead_inside/accessories/{self.items[1]}.png'))
                self.item_2.setIcon(QIcon(f'pictures/dead_inside/top/{self.items[2]}.png'))
                self.item_3.setIcon(QIcon(f'pictures/dead_inside/bot/{self.items[3]}.png'))
                self.item_4.setIcon(QIcon(f'pictures/dead_inside/socks/{self.items[4]}.png'))
                self.item_5.setIcon(QIcon(f'pictures/dead_inside/shoes/{self.items[5]}.png'))
            elif self.items[6] == 'old_money':
                self.item_1.setIcon(QIcon(f'pictures/old_money/top/{self.items[1]}.png'))
                self.item_2.setIcon(QIcon(f'pictures/old_money/watch/{self.items[2]}.png'))
                self.item_3.setIcon(QIcon(f'pictures/old_money/bag/{self.items[3]}.png'))
                self.item_4.setIcon(QIcon(f'pictures/old_money/bot/{self.items[4]}.png'))
                self.item_5.setIcon(QIcon(f'pictures/old_money/shoes/{self.items[5]}.png'))
            elif self.items[6] == 'viperr':
                self.item_1.setIcon(QIcon(f'pictures/viperr/glasses/{self.items[1]}.png'))
                self.item_2.setIcon(QIcon(f'pictures/viperr/top/{self.items[2]}.png'))
                self.item_3.setIcon(QIcon(f'pictures/viperr/belt/{self.items[3]}.png'))
                self.item_4.setIcon(QIcon(f'pictures/viperr/bot/{self.items[4]}.png'))
                self.item_5.setIcon(QIcon(f'pictures/viperr/shoes/{self.items[5]}.png'))
            else:
                self.item_1.setIcon(QIcon(f'pictures/y2k/hat/{self.items[1]}.png'))
                self.item_2.setIcon(QIcon(f'pictures/y2k/top/{self.items[2]}.png'))
                self.item_3.setIcon(QIcon(f'pictures/y2k/belt/{self.items[3]}.png'))
                self.item_4.setIcon(QIcon(f'pictures/y2k/bot/{self.items[4]}.png'))
                self.item_5.setIcon(QIcon(f'pictures/y2k/shoes/{self.items[5]}.png'))
        else:
            self.item_1.setIcon(QIcon())
            self.item_2.setIcon(QIcon())
            self.item_3.setIcon(QIcon('favourites/cross.png'))
            self.item_4.setIcon(QIcon())
            self.item_5.setIcon(QIcon())
        self.item_index = 0

    def back_func(self):
        self.parent().intro_window.show()
        self.parent().setGeometry(100, 100, 532, 381)
        self.hide()
