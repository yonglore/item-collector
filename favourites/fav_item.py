from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QApplication
from PyQt6.QtGui import QIcon
import models
from favourites import item_class_fav_alt


class FavouriteItem(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi('favourites/fav_item.ui', self)

        self.initUI()

    def initUI(self):
        self.back.clicked.connect(self.back_func)

        self.alt = models.Alt_db()
        # dead_inside = models.DeadInside_db()
        # old_money = models.OldMoney_db()
        # viperr = models.Viperr_db()
        # y2k = models.Y2k_db()

        self.item_fav_alt = item_class_fav_alt.FavAlt()
        self.item_fav_alt.hide()

        self.item_list = self.alt.get_favourites()
        if not self.item_list:
            self.item.setIcon(QIcon('favourites/nothing.png'))
        else:
            self.item.setIcon(QIcon(f'pictures/alt/pendant/{self.item_list[0]}.png'))
        self.item.clicked.connect(self.goto_item)

        self.refresh_btn.clicked.connect(self.refresh_page)
        self.delete_2.clicked.connect(self.delete_item)

    def refresh_page(self):
        self.item_list = self.alt.get_favourites()
        if self.item_list:
            self.item.setIcon(QIcon(f'pictures/alt/pendant/{self.item_list[0]}.png'))
        else:
            self.item.setIcon(QIcon('favourites/nothing.png'))

    def delete_item(self):
        if self.item_list:
            self.alt.remove_favourites(self.item_list[0])
        else:
            self.item.setIcon(QIcon('favourites/nothing.png'))

    def goto_item(self):
        if self.item_list:
            self.parent().item_fav_alt.show()
            self.parent().change_size(1051, 724)
            self.hide()

    def back_func(self):
        self.parent().intro_window.show()
        self.parent().setGeometry(100, 100, 532, 381)
        self.hide()
