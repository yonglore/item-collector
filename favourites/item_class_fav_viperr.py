from PyQt6 import uic
from PyQt6.QtWidgets import QWidget
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtCore import QUrl
import models


class FavViperr(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi('favourites/itembuy_fav.ui', self)

        self.InitUI()

    def InitUI(self):
        self.viperr_db = models.Viperr_db()
        self.item_back.clicked.connect(self.back)
        self.refresh.clicked.connect(self.refresh_page)

    def refresh_page(self):
        url = self.parent().fav_item.get_item_viperr()
        url = self.viperr_db.get_item_url(url)
        self.browser.setUrl(QUrl(url))

    def back(self):
        self.parent().fav_item.show()
        self.parent().setGeometry(100, 100, 764, 504)
        self.hide()
