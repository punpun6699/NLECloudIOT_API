import requests
import urllib3
import subprocess
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from BATA_CODE.UI_Bata import API_Main_UI_Bata
import pandas as pd

def callapi(excelcom):
    file_path = 'data.xlsx'

    # อ่าน DataFrame จากไฟล์ Excel ที่มีอยู่
    try:
        df = pd.read_excel(file_path, engine='openpyxl')
    except FileNotFoundError:
        # หากไฟล์ไม่พบ ให้สร้าง DataFrame ว่าง ๆ
        df = pd.DataFrame(columns=['Column1', 'Column2'])

    urllib3.disable_warnings(urllib3.exceptions.NotOpenSSLWarning)
    urlin = ui.textEdit.document().toPlainText()
    print(urlin)
    url = urlin

    with open('AccessToken.txt', 'r') as file:
        content = file.read()
        print(content)

    headers = {
        "AccessToken": content
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        print(data)
        datanew = str(data)
        substrings = datanew.split(',')


        if excelcom==1:
            nameindex1 = 0
            nameindex2 = 0
            datalo = []
            for substring in substrings:
                parts = substring.split("'")
                if len(parts) > 1:
                    datalo.append(parts[1])
            if "Name" in datalo:
                nameindex1 = datalo.index("Name")
                print(datalo[nameindex1], "=", substrings[nameindex1])
            if "Value" in datalo:
                nameindex2 = datalo.index("Value")
                print(datalo[nameindex2], "=", substrings[nameindex2])

            # สร้าง DataFrame ใหม่ที่มีข้อมูลใหม่
            new_row = {'Column1': substrings[nameindex1], 'Column2': substrings[nameindex2]}
            new_df = pd.DataFrame([new_row])

            # รวม DataFrame ใหม่กับ DataFrame ที่มีอยู่
            df = pd.concat([df, new_df], ignore_index=True)

            # บันทึก DataFrame ที่อัปเดตกลับไปที่ไฟล์ Excel
            df.to_excel(file_path, index=False, engine='openpyxl')
            print(f"\033[1;32;40mExcel Update\033[0m")
        else:
            print(f"\033[1;31;40mExcel not Update\033[0m")

        result_str = "\n".join(substrings)
        ui.label.setText(result_str)
    else:
        logtxt = f"Error: {response.status_code}, \n {response.text}"
        print(logtxt)
        ui.label.setText(logtxt)

def btncallClick():
    callapi(0)

def btncall_updatCelick():
    callapi(1)

def btnclsClick():
    ui.label.setText("")

def apisetClick():
    try:
        result = subprocess.run(["python", "AccessToken_Code.py"], capture_output=True, text=True)
        print("Script Output:", result.stdout)
        print("Script Errors:", result.stderr)
    except Exception as e:
        print(f"Error running script: {e}")

if __name__ == '__main__':
    app = QApplication(sys.argv)  # Create the main application object
    win = QMainWindow()  # Create the main window
    ui = API_Main_UI_Bata.Ui_Dialog()  # Initialize the UI from .ui file
    ui.setupUi(win)  # Set up the UI elements in the main window
    win.show()  # Show the main window

    # Connect button clicks to functions
    ui.pushButton.clicked.connect(btncallClick)
    ui.pushButton_2.clicked.connect(btnclsClick)
    ui.pushButton_3.clicked.connect(apisetClick)
    ui.pushButton_4.clicked.connect(btncall_updatCelick)

    sys.exit(app.exec_())  # Start the event loop and exit the application when done