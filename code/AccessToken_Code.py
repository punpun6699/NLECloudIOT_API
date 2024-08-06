#import library
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from UI import AccessToken_UI

def clscclack():
    ui.textEdit.setText("")
def canclack():
   sys.exit()
def Saveclick():
    # เปิดไฟล์เพื่อเขียนข้อมูล
    with open('AccessToken.txt', 'w') as file:
        file.write(ui.textEdit.document().toPlainText())
    sys.exit()


with open('AccessToken.txt', 'r') as file:
    content = file.read()

print(len(content))
if __name__ == '__main__':
    app = QApplication(sys.argv)  # Create the main application object
    win = QMainWindow()  # Create the main window
    ui = AccessToken_UI.Ui_Dialog()  # Initialize the UI from .ui file
    ui.setupUi(win)  # Set up the UI elements in the main window
    win.show()  # Show the main window
    ui.textEdit.setText(content)

    ui.pushButton.clicked.connect(clscclack)
    ui.pushButton_2.clicked.connect(canclack)
    ui.pushButton_3.clicked.connect(Saveclick)
    sys.exit(app.exec_())  # Start the event loop and exit the application when done