from PyQt5 import QtWidgets, Qt
# from PyQt5.uic import loadUi
from text_editor.ui import Ui_MainWindow

import pathlib


class Editor(QtWidgets.QMainWindow):
    def __init__(self):
        super(Editor, self).__init__()

        self.default_name = 'Untitled.txt'
        self.path = pathlib.Path.cwd() / self.default_name

        # import ui
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle(self.path.name)

        # QColorDialog and QFontDialog
        self.ui.color_pushButton_2.clicked.connect(self.change_color)
        self.ui.font_pushButton_2.clicked.connect(self.change_font)

        # Set align with radioButton
        self.ui.left_radioButton.toggled.connect(self.change_align)
        self.ui.right_radioButton.toggled.connect(self.change_align)
        self.ui.center_radioButton.toggled.connect(self.change_align)
        self.ui.justify_radioButton.toggled.connect(self.change_align)

        # Connect menu option
        self.ui.actionOpen.triggered.connect(self.get_filename)
        self.ui.actionOpen.setShortcut('CTRL+O')
        self.ui.actionSave_as.triggered.connect(self.get_save_filename)
        self.ui.actionSave_as.setShortcut('CTRL+SHIFT+S')
        self.ui.actionNew.triggered.connect(self.update_text)
        self.ui.actionNew.setShortcut('CTRL+N')
        self.ui.actionSave.triggered.connect(self.save_file)
        self.ui.actionSave.setShortcut('CTRL+S')

    def closeEvent(self, event) -> None:
        if (self.path.exists() is not True and self.ui.textEdit.toPlainText() != '') \
                or open(self.path, 'r').read() != self.ui.textEdit.toPlainText():
            message = QtWidgets.QMessageBox.question(self, "Choice Message",
                                                     f"Do you want save changes in file {self.path}?",
                                                     QtWidgets.QMessageBox.Yes |
                                                     QtWidgets.QMessageBox.No |
                                                     QtWidgets.QMessageBox.Cancel)

            if message == QtWidgets.QMessageBox.Yes:
                self.save_file()
                event.accept()
            elif message == QtWidgets.QMessageBox.No:
                event.accept()
            else:
                event.ignore()
        else:
            event.accept()

    def change_color(self):
        color = QtWidgets.QColorDialog.getColor()
        self.ui.textEdit.setTextColor(color)

    def change_font(self):
        font, status = QtWidgets.QFontDialog.getFont()

        if status:
            self.ui.textEdit.setFont(font)

    def change_align(self):
        radio_button = self.sender()

        if radio_button.text() == 'Left':
            self.ui.textEdit.setAlignment(Qt.Qt.AlignLeft)
        if radio_button.text() == 'Right':
            self.ui.textEdit.setAlignment(Qt.Qt.AlignRight)
        if radio_button.text() == 'Center':
            self.ui.textEdit.setAlignment(Qt.Qt.AlignCenter)
        if radio_button.text() == 'Justify':
            self.ui.textEdit.setAlignment(Qt.Qt.AlignJustify)

    def get_filename(self):
        file_filter = 'Data File (*.txt);; Word File (*.doc, *.docx)'
        response = QtWidgets.QFileDialog.getOpenFileName(
            parent=self,
            caption='Select a data file',
            directory=str(pathlib.Path.cwd()),
            filter=file_filter,
            initialFilter='Data File (*.txt)'
        )

        self.path = pathlib.Path(response[0])
        text = open(response[0]).read()
        self.ui.textEdit.setPlainText(text)

        self.setWindowTitle(response[0][response[0].rfind('/') + 1:])

    def get_save_filename(self):
        file_filter = 'Data File (*.txt);; Word File (*.doc *.docx)'
        response = QtWidgets.QFileDialog.getSaveFileName(
            parent=self,
            caption='Select a data file',
            directory='File.txt',
            filter=file_filter,
            initialFilter='Data File (*.txt)'
        )
        self.path = pathlib.Path(response[0])

        self.save_file()

        self.setWindowTitle(response[0][response[0].rfind('/') + 1:])

    def update_text(self):
        self.ui.textEdit.clear()

    def save_file(self):
        with open(self.path, 'w') as f:
            f.write(str(self.ui.textEdit.toPlainText()))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = Editor()
    window.show()
    sys.exit(app.exec_())
