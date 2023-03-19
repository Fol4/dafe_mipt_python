from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import Qt
from paint_ui import Ui_MainWindow

import pathlib


class Brush:
    """
    Класс кисти для рисования
    """
    def __init__(self):
        self.brush = QtGui.QPen(Qt.black, 1, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)

        self.active = False
        self.last_pos = 0

    def set_color(self, color):
        self.brush.setColor(color)

    def set_size(self, size):
        self.brush.setWidth(size)


class PaintWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(PaintWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.layers = []
        self.layer_width = self.size().width() - 2 * self.ui.listWidget.size().width() - 50
        self.layer_height = self.size().height() - 20

        self.active_layer = QtGui.QImage(self.layer_width, self.layer_height, QtGui.QImage.Format_RGB32)  # создание холста для рисования
        self.active_layer.fill(Qt.white)

        self.left_brush = Brush()
        self.right_brush = Brush()
        self.active_brush = self.left_brush

        self.ui.pushButton.clicked.connect(self.change_color_right)
        self.ui.pushButton_2.clicked.connect(self.change_color_left)

        self.ui.horizontalSlider.valueChanged.connect(self.change_size_right)
        self.ui.horizontalSlider_2.valueChanged.connect(self.change_size_left)

    def mousePressEvent(self, a0: QtGui.QMouseEvent) -> None:
        """
        Метод класса QMainWindow, отвечающий за ивенты нажатия на кнопки мыши
        :param a0: ивент
        :return:
        """
        if a0.button() == Qt.LeftButton:
            self.active_brush = self.left_brush
            self.left_brush.active = True
            self.left_brush.last_pos = a0.pos()

        if a0.button() == Qt.RightButton:
            self.active_brush = self.right_brush
            self.right_brush.active = True
            self.right_brush.last_pos = a0.pos()

    def mouseMoveEvent(self, a0: QtGui.QMouseEvent) -> None:
        """
        Метод класса QMainWindow, отвечающий за ивенты передвежения мыши
        :param a0: ивент
        :return:
        """
        if self.left_brush.active:
            painter = QtGui.QPainter(self.active_layer)   #актвация холста

            painter.setPen(self.active_brush.brush)   #установка кисти на холсте

            painter.drawLine(self.active_brush.last_pos, a0.pos())   #кисть рисует линию с предыдущей позиции мыши до нынешней

            self.active_brush.last_pos = a0.pos()
            self.update()   #обновление хослта

        if self.right_brush.active:
            painter = QtGui.QPainter(self.active_layer)

            painter.setPen(self.active_brush.brush)

            painter.drawLine(self.active_brush.last_pos, a0.pos())

            self.active_brush.last_pos = a0.pos()
            self.update()

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        """
        Метод класса QMainWindow, отвечающий за отрисовку
        :param a0: ивент
        :return:
        """
        canvas = QtGui.QPainter(self)   #создание полотна
        canvas.drawImage(5, 5, self.active_layer)   #отрисовка квадрата

    def change_color_right(self):
        """
        Функция изменения цвета правой кисти
        :return:
        """
        color = QtWidgets.QColorDialog.getColor()

        self.right_brush.set_color(color)
        self.ui.pushButton.setStyleSheet(f'background-color: rgb{color.getRgb()[:-1]}')   #изменеие цвета фона кнопки

    def change_color_left(self):
        """
        Функция изменения цвета левой кисти
        :return:
        """
        color = QtWidgets.QColorDialog.getColor()
        self.left_brush.set_color(color)
        self.ui.pushButton_2.setStyleSheet(f'background-color: rgb{color.getRgb()[:-1]}')

    def change_size_right(self):
        """
        Функция изменения размера правой кисти
        :return:
        """
        size = self.ui.horizontalSlider.value()
        self.right_brush.set_size(size)

    def change_size_left(self):
        """
        Функция изменения размера левой кисти
        :return:
        """
        size = self.ui.horizontalSlider_2.value()
        self.left_brush.set_size(size)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = PaintWindow()
    MainWindow.show()
    sys.exit(app.exec_())
