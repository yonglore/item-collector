from PyQt6 import uic
from PyQt6.QtWidgets import QWidget
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtCore import QUrl
import models


class ItemBuyOM(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi('item/itembuy.ui', self)
        self.InitUI()

    def InitUI(self):
        self.om_db = models.OldMoney_db()
        self.item_back.clicked.connect(self.back)
        self.refresh.clicked.connect(self.refresh_page)

    def refresh_page(self):
        url = self.parent().old_money.get_item()
        url = self.om_db.get_item_url(url)
        self.browser.setUrl(QUrl(url))

    def back(self):
        self.parent().old_money.show()
        self.parent().setGeometry(100, 100, 784, 813)
        self.hide()
