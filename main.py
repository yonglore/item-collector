import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow

from styles import alt_class, dead_inside_class, old_money_class, viperr_class, y2k_class
from item import item_class_alt, item_class_di, item_class_om, item_class_viperr, item_class_y2k
from favourites import (fav_item, item_class_fav_alt, item_class_fav_di, item_class_fav_om, item_class_fav_viperr,
                        item_class_fav_y2k, fav_outfit)


class IntroWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi('intro_window.ui', self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('стань вб монстром')
        self.apply.clicked.connect(self.apply_func)
        self.combobox.addItems(['Alt', 'Dead inside', 'Old money', 'Viperr', 'Y2k'])

        self.fav_item_btn.clicked.connect(self.fav_item_show)
        self.fav_item_btn.clicked.connect(self.fav_item_show)
        self.fav_outfit_btn.clicked.connect(self.fav_outfit_show)

    def fav_outfit_show(self):
        self.parent().fav_outfit.show()
        self.parent().change_size(853, 813)
        self.hide()

    def fav_item_show(self):
        self.parent().fav_item.show()
        self.parent().change_size(764, 504)
        self.hide()

    def apply_func(self):
        if self.combobox.currentText() == 'Alt':
            self.parent().alt.show()
            self.parent().change_size(892, 813)
            self.hide()
            self.style_category = 0

        if self.combobox.currentText() == 'Dead inside':
            self.parent().dead_inside.show()
            self.parent().change_size(892, 813)
            self.hide()
            self.style_category = 1

        if self.combobox.currentText() == 'Old money':
            self.parent().old_money.show()
            self.parent().change_size(892, 813)
            self.hide()
            self.style_category = 2

        if self.combobox.currentText() == 'Viperr':
            self.parent().viperr.show()
            self.parent().change_size(892, 813)
            self.hide()
            self.style_category = 3

        if self.combobox.currentText() == 'Y2k':
            self.parent().y2k.show()
            self.parent().change_size(892, 813)
            self.hide()
            self.style_category = 4


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.intro_window.show()

    def initUI(self):
        self.style_category = 0
        self.setGeometry(100, 100, 532, 381)
        self.intro_window = IntroWindow(self)
        self.intro_window.hide()

        self.alt = alt_class.Alt(self)
        self.alt.hide()

        self.dead_inside = dead_inside_class.DeadInside(self)
        self.dead_inside.hide()

        self.old_money = old_money_class.OldMoney(self)
        self.old_money.hide()

        self.viperr = viperr_class.Viperr(self)
        self.viperr.hide()

        self.y2k = y2k_class.Y2k(self)
        self.y2k.hide()

        self.item_alt = item_class_alt.ItemBuyAlt(self)
        self.item_alt.hide()

        self.item_di = item_class_di.ItemBuyDI(self)
        self.item_di.hide()

        self.item_om = item_class_om.ItemBuyOM(self)
        self.item_om.hide()

        self.item_viperr = item_class_viperr.ItemBuyViperr(self)
        self.item_viperr.hide()

        self.item_y2k = item_class_y2k.ItemBuyY2k(self)
        self.item_y2k.hide()

        self.fav_item = fav_item.FavouriteItem(self)
        self.fav_item.hide()

        self.item_fav_alt = item_class_fav_alt.FavAlt(self)
        self.item_fav_alt.hide()

        self.item_fav_di = item_class_fav_di.FavDI(self)
        self.item_fav_di.hide()

        self.item_fav_om = item_class_fav_om.FavOM(self)
        self.item_fav_om.hide()

        self.item_fav_viperr = item_class_fav_viperr.FavViperr(self)
        self.item_fav_viperr.hide()

        self.item_fav_y2k = item_class_fav_y2k.FavY2k(self)
        self.item_fav_y2k.hide()

        self.fav_outfit = fav_outfit.FavouriteOutfit(self)
        self.fav_outfit.hide()

    def change_size(self, w, h):
        self.setGeometry(100, 0, w, h)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec())
