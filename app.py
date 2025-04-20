import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
import threading
import dvd


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("DVD Screensaver App")
        self.setGeometry(100, 100, 400, 200)

        # Create a label
        self.label = QLabel("Click the button to start the DVD Screensaver", self)
        self.label.setStyleSheet("font-size: 16px;")
        self.label.setWordWrap(True)

        # Create a button
        self.button = QPushButton("Start Screensaver", self)
        self.button.setStyleSheet("font-size: 14px; padding: 10px;")
        self.button.clicked.connect(self.start_screensaver)

        # Set up the layout
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def start_screensaver(self):
        # Run the DVD screensaver in a separate thread
        
        dvd_instance = dvd.DVD()
        dvd_instance.run()




if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())