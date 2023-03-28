from PyQt5 import QtGui, QtCore, QtWidgets


class Snake:

    def __init__(self, width, height):
        self.body = [[5, 10], [5, 11]]
        self.head = self.body[0]

        self.direction = 'left'
        self.grow = False
        self.color = QtGui.QColor(0x538846)

        self.width = width
        self.height = height

    def is_dead(self):
        pass

    def move(self):

        if self.direction == 'left':
            self.head = [self.head[0] - 1, self.head[1]]

            if self.head[0] == 0:
                self.head[0] = self.width - 1

        if self.direction == 'right':
            self.head = [self.head[0] + 1, self.head[1]]

            if self.head[0] == self.width:
                self.head[0] = 0

        if self.direction == 'up':
            self.head = [self.head[0], self.head[1] - 1]

            if self.head[1] == 0:
                self.head[1] = self.height - 1

        if self.direction == 'down':
            self.head = [self.head[0], self.head[1] + 1]

            if self.head[1] == self.height:
                self.head[1] = 0

        self.body.insert(0, self.head)

        if not self.grow:
            self.body.pop()

class Food:
    COLOR = [QtGui.QColor(0xcb3333), QtGui.QColor(0xf30a66), QtGui.QColor(0x5188c4)]

    def __init__(self, width, height):
        self.bag = []

        self.width = width
        self.height = height

    def drop(self):
        pass


class Board(QtWidgets.QFrame):
    SPEED = 80

    HEIGHTINBLOCKS = 40
    WIDTHINBLOCKS = 60

    def __init__(self, parent):
        super(Board, self).__init__(parent)

        self.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)

        self.timer = QtCore.QBasicTimer()

        self.snake = Snake(Board.WIDTHINBLOCKS, Board.HEIGHTINBLOCKS)

    def block_width(self):
        return self.frameGeometry().width() / Board.WIDTHINBLOCKS

    def block_height(self):
        return self.frameGeometry().height() / Board.HEIGHTINBLOCKS

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:

        painter = QtGui.QPainter(self)

        rect = self.contentsRect()

        boardtop = rect.bottom() - self.frameGeometry().height()

        for cord in self.snake.body:
            self.drawrect(painter, rect.left() + cord[0] * self.block_width(),
                          boardtop + cord[1] * self.block_height(), self.snake.color)

    def drawrect(self, painter, x, y, color):
        painter.fillRect(x, y, self.block_width() - 2, self.block_height() - 2, color)

    def timerEvent(self, a0: QtCore.QTimerEvent) -> None:

        if a0.timerId() == self.timer.timerId():
            self.snake.move()
            self.update()

    def keyPressEvent(self, a0: QtGui.QKeyEvent) -> None:

        key = a0.key()

        if key == QtCore.Qt.Key.Key_Left:
            if self.snake.direction != 'right':
                self.snake.direction = 'left'

        if key == QtCore.Qt.Key.Key_Right:
            if self.snake.direction != 'left':
                self.snake.direction = 'right'

        if key == QtCore.Qt.Key.Key_Up:
            if self.snake.direction != 'down':
                self.snake.direction = 'up'

        if key == QtCore.Qt.Key.Key_Down:
            if self.snake.direction != 'up':
                self.snake.direction = 'down'


    def is_dead(self):
        pass

    def start(self):
        self.timer.start(Board.SPEED, self)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.board = Board(self)
        self.setCentralWidget(self.board)
        self.setGeometry(100, 100, 600, 400)
        self.board.start()

        self.show()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())

