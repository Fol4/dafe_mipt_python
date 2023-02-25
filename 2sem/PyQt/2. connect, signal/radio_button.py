"""
Работа с QRadioButton.
"""


from PyQt5.QtWidgets import QApplication, QDialog, QGroupBox, \
    QHBoxLayout, QLabel, QVBoxLayout, QRadioButton
import sys


class Window(QDialog):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 400, 300)
        self.setWindowTitle("PyQt5 QRadioButton")

        self.groupbox = QGroupBox("What is your favorite sport ?")  # Виджет позволяющий групировать другие виджеты)

        hbox = QHBoxLayout()

        self.rad1 = QRadioButton("Football")  # Создание виджета QRadioButton
        self.rad1.toggled.connect(self.on_selected)
        hbox.addWidget(self.rad1)

        self.rad2 = QRadioButton("Cricket")
        self.rad2.toggled.connect(self.on_selected)
        hbox.addWidget(self.rad2)

        self.rad3 = QRadioButton("Tennis")
        self.rad3.toggled.connect(self.on_selected)
        hbox.addWidget(self.rad3)

        self.groupbox.setLayout(hbox)

        vbox = QVBoxLayout()
        vbox.addWidget(self.groupbox)

        self.label = QLabel("")

        vbox.addWidget(self.label)

        self.setLayout(vbox)


    def on_selected(self):
        radio_button = self.sender()  # Возвращает виджет, который отправляет сигнал

        if radio_button.isChecked():  # Проверка является ли кнопка активной
            self.label.setText("You have selected : " + radio_button.text())


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())
