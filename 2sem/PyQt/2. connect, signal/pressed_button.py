"""
Реализация двух состояний кнопки :
1. Pressed
2. Released
"""

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        button = QPushButton("Press Me!")
        button.setCheckable(True)  # Метод QPushButton, который добавляет кнопке состояния
        button.clicked.connect(self.the_button_was_clicked)
        button.clicked.connect(self.the_button_was_toggled)

        self.setCentralWidget(button)

    def the_button_was_clicked(self):
        print("Clicked!")

    def the_button_was_toggled(self, checked):  # Чтобы отслеживать состояние кнопки, нужно в функцию, которую мы
        # привязываем к кнопке, добавить параметр checked(название может быть любым)
        print("Checked?", checked)

app = QApplication([])

window = MainWindow()
window.show()

app.exec()