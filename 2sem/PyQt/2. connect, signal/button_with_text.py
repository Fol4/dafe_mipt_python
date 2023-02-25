"""
Cоздание oneHot приложения
Происходит создание кнопки при нажатии на которую кнопка удаляется и изменяется название кнопки.
"""


from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        self.button = QPushButton("Press Me!")
        self.button.clicked.connect(self.the_button_was_clicked)  # Привязка сигнала, который инициализируется
        # кнопкой button, к функции the_button_was_clicked

        self.setCentralWidget(self.button)

    def the_button_was_clicked(self):
        self.button.setText("You already clicked me.")  # Метод класс QPushButton, который изменяет его название
        self.button.setEnabled(False)   # Метод класса QPushButton, который делает кнопку неактивной

        self.setWindowTitle("My Oneshot App")

app = QApplication([])

window = MainWindow()
window.show()

app.exec()