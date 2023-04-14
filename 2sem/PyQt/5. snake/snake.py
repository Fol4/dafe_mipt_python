from PyQt5 import QtGui, QtCore, QtWidgets
import random


class Snake:

    def __init__(self, width, height):
        self.body = [[5, 10], [5, 11]]
        self.head = self.body[0]

        self.direction = 'left'
        self.grow = False
        self.color = QtGui.QImage('food/body.jpg')
        self.color_head = QtGui.QImage('food/head.jpg')
        self.color_ass = QtGui.QImage('food/ass.jpg')

        self.width = width
        self.height = height

    def is_dead(self):
        pass

    def move(self):

        if self.direction == 'left':
            self.head = [self.head[0] - 1, self.head[1]]

            if self.head[0] == -1:
                self.head[0] = self.width - 1

        if self.direction == 'right':
            self.head = [self.head[0] + 1, self.head[1]]

            if self.head[0] == self.width:
                self.head[0] = 0

        if self.direction == 'up':
            self.head = [self.head[0], self.head[1] - 1]

            if self.head[1] == -1:
                self.head[1] = self.height - 1

        if self.direction == 'down':
            self.head = [self.head[0], self.head[1] + 1]

            if self.head[1] == self.height:
                self.head[1] = 0

        self.body.insert(0, self.head)

        if not self.grow:
            self.body.pop()
        else:
            self.grow = False


class Food:
    COLOR = [QtGui.QImage('food/chich.png'), QtGui.QImage('food/bour_smiling.png')]

    def __init__(self, width, height):
        self.bag = []

        self.width = width
        self.height = height

    def drop(self):
        random.seed(random.randint(10, 40))

        x = random.randint(0, self.width - 1)
        y = random.randint(0, self.height - 1)
        color = random.randint(0, len(Food.COLOR) - 1)

        self.bag.append({'cord': [x, y], 'color': Food.COLOR[color]})


class Board(QtWidgets.QFrame):
    SPEED = 80

    HEIGHTINBLOCKS = 10
    WIDTHINBLOCKS = 15

    def __init__(self, parent):
        super(Board, self).__init__(parent)

        self.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)

        self.timer = QtCore.QBasicTimer()

        self.snake = Snake(Board.WIDTHINBLOCKS, Board.HEIGHTINBLOCKS)
        self.food = Food(Board.WIDTHINBLOCKS, Board.HEIGHTINBLOCKS)

    def block_width(self):
        return self.frameGeometry().width() / Board.WIDTHINBLOCKS

    def block_height(self):
        return self.frameGeometry().height() / Board.HEIGHTINBLOCKS

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:

        painter = QtGui.QPainter(self)

        rect = self.contentsRect()

        boardtop = rect.bottom() - self.frameGeometry().height()
        self.drawrect(painter, rect.left() + self.snake.body[0][0] * self.block_width(),
                      boardtop + self.snake.body[0][1] * self.block_height(), self.snake.color_head)
        self.drawrect(painter, rect.left() + self.snake.body[-1][0] * self.block_width(),
                      boardtop + self.snake.body[-1][1] * self.block_height(), self.snake.color_ass)

        for cord in self.snake.body:
            self.drawrect(painter, rect.left() + cord[0] * self.block_width(),
                          boardtop + cord[1] * self.block_height(), self.snake.color)

        for fruit in self.food.bag:
            cord = fruit['cord']
            self.drawrect(painter, rect.left() + cord[0] * self.block_width(),
                          boardtop + cord[1] * self.block_height(), fruit['color'])

    def drawrect(self, painter, x, y, color):
        rect = QtCore.QRect(x, y, self.block_width() - 2, self.block_height() - 2)
        painter.drawImage(rect, color)

    def timerEvent(self, a0: QtCore.QTimerEvent) -> None:

        if a0.timerId() == self.timer.timerId():
            self.snake.move()
            self.collision()
            self.drop()
            self.update()

    def collision(self):
        for fruit in self.food.bag:
            if fruit['cord'] == self.snake.head:
                print(1)
                self.snake.grow = True
                print(2)
                self.food.bag.remove(fruit)
                print(3)
                break

    def drop(self):
        if len(self.food.bag) == 0:
            self.food.drop()

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

