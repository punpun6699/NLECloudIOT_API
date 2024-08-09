import requests
import urllib3
import subprocess
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from bata_2.UI_bata_2 import UI_3_UI

def apicall():
    urllib3.disable_warnings(urllib3.exceptions.NotOpenSSLWarning)
    url = ui.textEdit.document().toPlainText()
    # Read the AccessToken from a file
    with open('AccessToken.txt', 'r') as file:
        content = file.read()
        print(content)

    headers = {
        "AccessToken": content  # Set up the AccessToken in the request headers
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:  # If the request is successful
        data = response.json()  # Parse the JSON response into a Python dictionary
        datanew = str(data)  # Convert the data to a string
        substrings = datanew.split(',')  # Split the string by commas
        # Append the final substring after the last comma

def callbutton():
    ui.label.setText("HI")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = QMainWindow()
    ui = UI_3_UI.Ui_Dialog()
    ui.setupUi(win)
    win.show()

    ui.pushButton.clicked.connect(callbutton)
    sys.exit(app.exec_())
