"""
Концепт приложения меню
"""

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(413, 306)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.checkBoxPizza = QtWidgets.QCheckBox(Dialog)
        self.checkBoxPizza.setObjectName("checkBoxPizza")
        self.checkBoxPizza.stateChanged.connect(self.checked_item)

        self.verticalLayout_2.addWidget(self.checkBoxPizza)
        self.checkBoxSalad = QtWidgets.QCheckBox(Dialog)
        self.checkBoxSalad.setObjectName("checkBoxSalad")
        self.verticalLayout_2.addWidget(self.checkBoxSalad)
        self.checkBoxSalad.stateChanged.connect(self.checked_item)

        self.checkBoxSausage = QtWidgets.QCheckBox(Dialog)
        self.checkBoxSausage.setObjectName("checkBoxSausage")
        self.verticalLayout_2.addWidget(self.checkBoxSausage)
        self.horizontalLayout.addLayout(self.verticalLayout_2)

        # added newly after conversion for connecting signal to slot
        self.checkBoxSausage.stateChanged.connect(self.checked_item)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.labelResult = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labelResult.setFont(font)
        self.labelResult.setText("")
        self.labelResult.setObjectName("labelResult")
        self.verticalLayout.addWidget(self.labelResult)
        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "PyQt5 QCheckBoxes"))
        self.label.setText(_translate("Dialog", "Regular Tuna Price : 20"))
        self.label_2.setText(_translate("Dialog", "Select Extra"))
        self.checkBoxPizza.setText(_translate("Dialog", "Pizza : 3"))
        self.checkBoxSalad.setText(_translate("Dialog", "Salad : 4"))
        self.checkBoxSausage.setText(_translate("Dialog", "Sausage : 5"))

    # this is method is added after conversion
    def checked_item(self):
        price = 20

        if self.checkBoxPizza.isChecked():
            price = price + 3

        if self.checkBoxSalad.isChecked():
            price = price + 4

        if self.checkBoxSausage.isChecked():
            price = price + 5

        self.labelResult.setText("Total Price Is : {} ".format(price))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())