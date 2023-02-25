"""
Hello World! app.
"""

import sys

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow):  # Подкласс QMainWindow для настройки главного окна приложения
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")  # Метода класса QMainWindow, который изменяет наименование окна.
        button = QPushButton("Press Me!")  # Создание кнопки с названием "Press Me!"

        self.setCentralWidget(button)  # Распологает кнопку по центру виджета


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()