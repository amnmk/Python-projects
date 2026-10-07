import sys
from PyQt6.QtCore import QUrl
from PyQt6.QtWidgets import QApplication, QMainWindow, QToolBar, QLineEdit, QPushButton, QVBoxLayout, QWidget
from PyQt6.QtWebEngineWidgets import QWebEngineView

class CustomBrowser(QMainWindow):
    def __init__(self):
        super().__init__()
        # Set the application title and default size (Width: 1024, Height: 768)
        self.setWindowTitle("Custom Python Browser")
        self.setGeometry(100, 100, 1024, 768)

        # 1. Create the web rendering engine (Uses Chromium under the hood)
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://google.com")) # Your homepage

        # 2. Build the top toolbar interface
        self.toolbar = QToolBar()
        self.addToolBar(self.toolbar)

        # Back Button
        self.back_btn = QPushButton("⬅")
        self.back_btn.clicked.connect(self.browser.back)
        self.toolbar.addWidget(self.back_btn)

        # Forward Button
        self.forward_btn = QPushButton("➡")
        self.forward_btn.clicked.connect(self.browser.forward)
        self.toolbar.addWidget(self.forward_btn)

        # Reload Button
        self.reload_btn = QPushButton("🔄")
        self.reload_btn.clicked.connect(self.browser.reload)
        self.toolbar.addWidget(self.reload_btn)

        # Address Bar / URL Bar
        self.address_bar = QLineEdit()
        self.address_bar.returnPressed.connect(self.navigate_to_url)
        self.toolbar.addWidget(self.address_bar)
        
        # Keeps the URL bar text matching whatever page you click on
        self.browser.urlChanged.connect(self.update_address_bar)

        # 3. Stack the pieces together (Toolbar on top, Browser window below)
        layout = QVBoxLayout()
        layout.addWidget(self.browser)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def navigate_to_url(self):
        url = self.address_bar.text()
        # Automatically fix the web address if you forget 'https://'
        if not url.startswith("http://") and not url.startswith("https://"):
            url = "https://" + url
        self.browser.setUrl(QUrl(url))

    def update_address_bar(self, qurl):
        self.address_bar.setText(qurl.toString())

# This physically triggers the window to pop up on your screen
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CustomBrowser()
    window.show()
    sys.exit(app.exec())
# Code is made by @amnmk on GitHub
