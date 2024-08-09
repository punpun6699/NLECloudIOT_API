from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(759, 539)

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setStyleSheet("QLabel { color: lightgreen; background-color: black; }")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignTop)
        self.label.setGeometry(QtCore.QRect(330, 70, 391, 441))
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(320, 20, 91, 31))
        self.label_2.setObjectName("label_2")

        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(50, 220, 111, 61))
        self.pushButton.setObjectName("pushButton")

        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(50, 290, 111, 61))
        self.pushButton_4.setObjectName("pushButton_2")

        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(50, 360, 111, 61))
        self.pushButton_2.setObjectName("pushButton_3")

        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(50, 430, 111, 61))
        self.pushButton_3.setObjectName("pushButton_3")

        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(30, 60, 201, 41))
        self.textEdit.setObjectName("textEdit")

        self.textEdit_2 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_2.setGeometry(QtCore.QRect(30, 160, 201, 41))
        self.textEdit_2.setObjectName("textEdit_2")

        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(40, 20, 91, 31))
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(40, 110, 91, 31))
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        # Overriding resizeEvent
        Dialog.resizeEvent = self.resizeEvent

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "NLECloud APL Calling BATA 2"))
        self.label.setText(_translate("Dialog", ""))
        self.label_2.setText(_translate("Dialog", "Log"))
        self.pushButton.setText(_translate("Dialog", "call"))
        self.pushButton_4.setText(_translate("Dialog", "call and save"))
        self.pushButton_2.setText(_translate("Dialog", "cls"))
        self.pushButton_3.setText(_translate("Dialog", "AccessToken"))
        self.label_3.setText(_translate("Dialog", "DeviceId"))
        self.label_4.setText(_translate("Dialog", "APItag"))

    def resizeEvent(self, event):
        dialog_width = event.size().width()
        dialog_height = event.size().height()
        self.label.setGeometry(QtCore.QRect(240, 70, dialog_width - 270, dialog_height - 100))
        self.label_2.setGeometry(QtCore.QRect(240, 20, 91, 31))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())