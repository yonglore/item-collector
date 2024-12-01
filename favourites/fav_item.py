from PyQt6 import uic
from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QIcon
import models
from favourites import item_class_fav_alt, item_class_fav_di, item_class_fav_om, item_class_fav_viperr, \
    item_class_fav_y2k
import os


class FavouriteItem(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi('favourites/fav_item.ui', self)

        self.initUI()

    def initUI(self):
        self.back.clicked.connect(self.back_func)

        self.item_next.setIcon(QIcon('styles/right arrow.png'))
        self.item_prev.setIcon(QIcon('styles/left arrow.png'))

        self.alt = models.Alt_db()
        self.alt_names = self.alt.get_names()

        self.dead_inside = models.DeadInside_db()
        self.di_names = self.dead_inside.get_names()

        self.old_money = models.OldMoney_db()
        self.om_names = self.old_money.get_names()

        self.viperr = models.Viperr_db()
        self.viperr_names = self.viperr.get_names()

        self.y2k = models.Y2k_db()
        self.y2k_names = self.y2k.get_names()

        self.item_fav_alt = item_class_fav_alt.FavAlt()
        self.item_fav_alt.hide()

        self.item_fav_di = item_class_fav_di.FavDI()
        self.item_fav_di.hide()

        self.item_fav_om = item_class_fav_om.FavOM()
        self.item_fav_om.hide()

        self.item_fav_viperr = item_class_fav_viperr.FavViperr()
        self.item_fav_viperr.hide()

        self.item_fav_y2k = item_class_fav_y2k.FavY2k(self)
        self.item_fav_y2k.hide()

        alt_item_list = self.alt.get_favourites()
        di_item_list = self.dead_inside.get_favourites()
        om_item_list = self.old_money.get_favourites()
        viperr_list = self.viperr.get_favourites()
        y2k_item_list = self.y2k.get_favourites()

        self.item_list = alt_item_list + di_item_list + om_item_list + viperr_list + y2k_item_list

        self.item.setIcon(QIcon('favourites/nothing.png'))
        self.item.clicked.connect(self.goto_item)

        self.item_index = 0

        self.refresh_btn.clicked.connect(self.refresh_page)
        self.delete_2.clicked.connect(self.delete_item)
        self.item_next.clicked.connect(self.next_item)
        self.item_prev.clicked.connect(self.prev_item)

    def next_item(self):
        if len(self.item_list) > 1:
            if self.item_index == len(self.item_list) - 1:
                self.item_index = -1
            self.item_index += 1
            self.item.setIcon(QIcon(f'favourites/pics/{self.item_list[self.item_index]}.png'))
            self.item_icon = self.item_list[self.item_index]

    def prev_item(self):
        if len(self.item_list) > 1:
            if self.item_list:
                if self.item_index == 0:
                    self.item_index = len(self.item_list)
                self.item_index -= 1
                self.item.setIcon(QIcon(f'favourites/pics/{self.item_list[self.item_index]}.png'))
                self.item_icon = self.item_list[self.item_index]

    def refresh_page(self):
        self.item_index = 0
        alt_item_list = self.alt.get_favourites()
        di_item_list = self.dead_inside.get_favourites()
        om_item_list = self.old_money.get_favourites()
        viperr_item_list = self.viperr.get_favourites()
        y2k_item_list = self.y2k.get_favourites()

        self.item_list = alt_item_list + di_item_list + om_item_list + viperr_item_list + y2k_item_list
        if self.item_list:
            self.item.setIcon(QIcon(f'favourites/pics/{self.item_list[0]}.png'))
        else:
            self.item.setIcon(QIcon('favourites/nothing.png'))

    def delete_item(self):
        if self.item_list:
            if self.item_list[self.item_index] in self.alt_names:
                self.alt.remove_favourites(self.item_list[self.item_index])
            elif self.item_list[self.item_index] in self.di_names:
                self.dead_inside.remove_favourites(self.item_list[self.item_index])
            elif self.item_list[self.item_index] in self.om_names:
                self.old_money.remove_favourites(self.item_list[self.item_index])
            elif self.item_list[self.item_index] in self.viperr_names:
                self.viperr.remove_favourites(self.item_list[self.item_index])
            else:
                self.y2k.remove_favourites(self.item_list[self.item_index])
            os.remove(f'favourites/pics/{self.item_list[self.item_index]}.png')
        else:
            self.item.setIcon(QIcon('favourites/nothing.png'))

    def get_item_alt(self):
        return self.item_list[self.item_index]

    def get_item_di(self):
        return self.item_list[self.item_index]

    def get_item_om(self):
        return self.item_list[self.item_index]

    def get_item_viperr(self):
        return self.item_list[self.item_index]

    def get_item_y2k(self):
        return self.item_list[self.item_index]

    def goto_item(self):
        if self.item_list:
            if self.item_list[self.item_index] in self.alt_names:
                self.parent().item_fav_alt.show()
                self.parent().change_size(1051, 724)
                self.hide()
            elif self.item_list[self.item_index] in self.di_names:
                self.parent().item_fav_di.show()
                self.parent().change_size(1051, 724)
                self.hide()
            elif self.item_list[self.item_index] in self.om_names:
                self.parent().item_fav_om.show()
                self.parent().change_size(1051, 724)
                self.hide()
            elif self.item_list[self.item_index] in self.viperr_names:
                self.parent().item_fav_viperr.show()
                self.parent().change_size(1051, 724)
                self.hide()
            else:
                self.parent().item_fav_y2k.show()
                self.parent().change_size(1051, 724)
                self.hide()

    def back_func(self):
        self.parent().intro_window.show()
        self.parent().setGeometry(100, 100, 532, 381)
        self.hide()
