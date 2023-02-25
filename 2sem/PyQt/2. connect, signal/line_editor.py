"""
Работа с вводом и выводом.
"""


from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget

import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        self.label = QLabel()  # Виждет, который позволяет выводить текст на экран

        self.input = QLineEdit()  # Виждет, который позволяет вводить инофрмацию информицю для приложения
        self.input.textChanged.connect(self.label.setText)  # На сигнал изменения текста textChanged вызывается метод
        # QLabel setText, который изменяет значение label
        """
        Аналогично:
        
                .....
        def __init__(self):
                .....
            self.input.textChanged.connect(self.some_func)
                .....
                
        def some_func(self, text):
            self.lable.setText(text)
            
                .....
        """

        layout = QVBoxLayout()  # Позволяет распологать виджеты параллельно друг-другу
        layout.addWidget(self.input)  # Доболяет виджет а layout
        layout.addWidget(self.label)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()