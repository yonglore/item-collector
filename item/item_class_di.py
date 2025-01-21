from PyQt6 import uic
from PyQt6.QtWidgets import QWidget
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtCore import QUrl
import models


class ItemBuyDI(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi('item/itembuy.ui', self)
        self.InitUI()

    def InitUI(self):
        self.di_db = models.DeadInside_db()
        self.item_back.clicked.connect(self.back)
        self.refresh.clicked.connect(self.refresh_page)

        self.add_fav_item.clicked.connect(self.add_fav)

    def add_fav(self):
        item = self.parent().dead_inside.get_item()
        category = self.di_db.get_category(item)
        self.di_db.add_favourites(item, category)

    def refresh_page(self):
        url = self.parent().dead_inside.get_item()
        url = self.di_db.get_item_url(url)
        self.browser.setUrl(QUrl(url))

    def back(self):
        self.parent().dead_inside.show()
        self.parent().setGeometry(100, 100, 853, 813)
        self.hide()
