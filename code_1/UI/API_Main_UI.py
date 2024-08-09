from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(555, 466)

        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(90, 20, 441, 31))
        self.textEdit.setObjectName("textEdit")

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(190, 85, 321, 351))
        self.label.setStyleSheet("QLabel { color: lightgreen; background-color: black; }")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignTop)
        self.label.setObjectName("label")

        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(30, 60, 131, 61))
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 140, 131, 61))
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 220, 131, 61))
        self.pushButton_3.setObjectName("pushButton_3")

        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 30, 58, 16))
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(190, 58, 58, 16))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        # Override resizeEvent
        Dialog.resizeEvent = self.resizeEvent

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "NLECloud APL Calling"))
        self.label.setText(_translate("Dialog", ""))
        self.pushButton.setText(_translate("Dialog", "call"))
        self.pushButton_2.setText(_translate("Dialog", "cls"))
        self.pushButton_3.setText(_translate("Dialog", "AccessToken"))
        self.label_2.setText(_translate("Dialog", "URL"))
        self.label_3.setText(_translate("Dialog", "Log"))

    def resizeEvent(self, event):
        dialog_width = event.size().width()
        dialog_height = event.size().height()

        # Manually adjust the sizes and positions of widgets here
        self.textEdit.setGeometry(QtCore.QRect(90, 20, dialog_width - 110, 31))
        self.label.setGeometry(QtCore.QRect(190, 85, dialog_width - 210, dialog_height - 100))
        self.label_3.setGeometry(QtCore.QRect(190, 58, 58, 16))

        # Keep other widgets in their original positions and sizes

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())