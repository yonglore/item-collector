from PyQt6 import uic
from PyQt6.QtWidgets import QWidget
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtCore import QUrl
import models


class FavAlt(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi('item/itembuy.ui', self)

        self.InitUI()

    def InitUI(self):
        self.alt_db = models.Alt_db()
        self.item_back.clicked.connect(self.back)
        self.refresh.clicked.connect(self.refresh_page)

        self.add_fav_item.clicked.connect(self.add_fav)

    def add_fav(self):
        item = self.parent().alt.get_item()
        self.alt_db.add_favourites(item)

    def refresh_page(self):
        url = self.parent().alt.get_item()
        url = self.alt_db.get_item_url(url)
        self.browser.setUrl(QUrl(url))


    def back(self):
        self.parent().fav_item.show()
        self.parent().setGeometry(100, 100, 764, 504)
        self.hide()
