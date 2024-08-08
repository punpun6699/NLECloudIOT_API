import requests
import urllib3
import subprocess
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from BATA_CODE.UI_Bata import API_DP_2_UI_bata
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
    # URL และโทเค็นการเข้าถึง
    in1 = ui.textEdit.document().toPlainText()
    in2=ui.textEdit_2.document().toPlainText()
    urlin="http://api.nlecloud.com/devices/"+in1+"/sensors/"+in2
    print(urlin)
    url = urlin
    with open('AccessToken.txt', 'r') as file:
        content = file.read()
        print(content)
    headers = { #AccessToken
        "AccessToken":content
    }

    # ส่งคำขอ GET
    response = requests.get(url, headers=headers)
    # ตรวจสอบสถานะของคำขอ
    if response.status_code == 200:
        data = response.json()
        print(data)
        print(len(data))
        datanew=str(data)
        print(len(datanew))
        q=0
        substrings = []
        for i in range(len(datanew)):
            if datanew[i]==",":
                print(datanew[q:i])
                substrings.append(datanew[q:i])  # Collect substring from q to i
                q = i + 1  # Update q to be the position after the comma

            # Append the final substring after the last comma
        print(datanew[q:])
        substrings.append(datanew[q:])
        print(substrings)
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

        # Join substrings with new lines
        result_str = "\n".join(substrings)

        # Set the formatted string to the QLabel
        ui.label.setText(result_str)
     #ui.label.setText(datanew)
    else:
        logtxt = str (f"Error: {response.status_code}, \n {response.text}")
        print(f"Error: {response.status_code}, {response.text}")
        ui.label.setText(logtxt)

def btncallClick():
    callapi(0)
def btncallSaveClick():
    callapi(1)
def btnclsClick():
    data=""
    ui.label.setText(data)
def apisetClick():
    try:
        # ใช้ subprocess.run() เพื่อรันสคริปต์ Python
        result = subprocess.run(["python", "AccessToken_Code.py"], capture_output=True, text=True)
        print("Script Output:", result.stdout)
        print("Script Errors:", result.stderr)
    except Exception as e:
        print(f"Error running script: {e}")


if __name__ == '__main__':
    app = QApplication(sys.argv)  # Create the main application object
    win = QMainWindow()  # Create the main window
    ui = API_DP_2_UI_bata.Ui_Dialog()  # Initialize the UI from .ui file
    ui.setupUi(win)  # Set up the UI elements in the main window
    win.show()  # Show the main window

    # Connect button clicks to functions
    ui.pushButton.clicked.connect(btncallClick)
    ui.pushButton_2.clicked.connect(btnclsClick)
    ui.pushButton_3.clicked.connect(apisetClick)
    ui.pushButton_4.clicked.connect(btncallSaveClick)


    sys.exit(app.exec_())  # Start th  e event loop and exit the application when done