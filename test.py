import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtCore import QUrl

class WebViewApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Web View Widget")
        self.setGeometry(100, 100, 800, 600)

        # Создание виджета для браузера
        self.browser = QWebEngineView()

        # Кнопка для загрузки URL
        self.load_button = QPushButton("Открыть ссылку")
        self.load_button.clicked.connect(self.load_link)

        # Установка макета
        layout = QVBoxLayout()
        layout.addWidget(self.load_button)
        layout.addWidget(self.browser)

        self.btn = QPushButton()
        self.btn.isChecked()

    def load_link(self):
        # Определённая ссылка
        url = QUrl("https://www.wildberries.ru/")
        self.browser.setUrl(url)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WebViewApp()
    window.show()
    sys.exit(app.exec())