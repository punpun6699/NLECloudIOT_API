# import libraries
import requests  # HTTP library for making API requests
import urllib3  # HTTP library for handling SSL/TLS connections
import subprocess  # Used to run external Python scripts or commands
import sys  # System-specific parameters and functions
from PyQt5.QtWidgets import QApplication, QMainWindow  # UI components for creating application windows and widgets
from BATA_CODE.UI_Bata import API_Main_UI_Bata  # Import the custom user interface (UI)
import pandas as pd  # Library for data manipulation and analysis, particularly working with DataFrames


def callapi(excelcom):  # Function to call an API and handle Excel operations based on the argument
    file_path = 'data.xlsx'  # Path to the Excel file

    # Try to read the DataFrame from the Excel file
    try:
        df = pd.read_excel(file_path, engine='openpyxl')
    except FileNotFoundError:
        # If the file doesn't exist, create a new DataFrame with specified columns
        df = pd.DataFrame(columns=['CreateDate', 'Name', 'Value'])

    urllib3.disable_warnings(urllib3.exceptions.NotOpenSSLWarning)  # Disable SSL/TLS warnings
    urlin = ui.textEdit.document().toPlainText()  # Get the API URL from user input in the UI
    print(urlin)
    url = urlin

    # Read the AccessToken from a file
    with open('AccessToken.txt', 'r') as file:
        content = file.read()
        print(content)

    headers = {
        "AccessToken": content  # Set up the AccessToken in the request headers
    }

    # Send a GET request to the API
    response = requests.get(url, headers=headers)
    if response.status_code == 200:  # If the request is successful
        data = response.json()  # Parse the JSON response into a Python dictionary
        print(data)
        datanew = str(data)  # Convert the data to a string
        substrings = datanew.split(',')  # Split the string by commas

        if excelcom == 1:  # If the function is called with an argument to update Excel
            substrings.append("N/A")  # Add a placeholder for missing data
            CreateDateIndex = len(substrings) - 1
            NameIndex = len(substrings) - 1
            ValueIndex = len(substrings) - 1
            datalo = []  # List to store parts of the data

            # Process each substring to extract relevant information
            for substring in substrings:
                parts = substring.split("'")
                if len(parts) > 1:
                    datalo.append(parts[1])

            # Identify indices of relevant fields
            if "Name" in datalo:
                CreateDateIndex = datalo.index("CreateDate")
            if "Value" in datalo:
                NameIndex = datalo.index("Name")
            if "CreateDate" in datalo:
                ValueIndex = datalo.index("Value")

            print('CreateDateIndex', 'is', CreateDateIndex, "=", substrings[CreateDateIndex])
            print('NameIndex', 'is', NameIndex, "=", substrings[NameIndex])
            print('ValueIndex', 'is', ValueIndex, "=", substrings[ValueIndex])

            # If the necessary data is available, update the Excel file
            if substrings[ValueIndex] != "N/A" or substrings[NameIndex] != "N/A" or substrings[
                CreateDateIndex] != "N/A":
                if substrings[ValueIndex][11] == "{":
                    gpsValue = str(substrings[ValueIndex] + "," + substrings[ValueIndex + 1])
                    print('GPS', 'is', gpsValue)
                    new_row = {'CreateDate': substrings[CreateDateIndex], 'Name': substrings[NameIndex],
                               'Value': gpsValue}
                    new_df = pd.DataFrame([new_row])
                else:
                    new_row = {'CreateDate': substrings[CreateDateIndex], 'Name': substrings[NameIndex],
                               'Value': substrings[ValueIndex]}
                    new_df = pd.DataFrame([new_row])

                # Append the new data to the existing DataFrame and save it back to the Excel file
                df = pd.concat([df, new_df], ignore_index=True)
                df.to_excel(file_path, index=False, engine='openpyxl')
                substrings.pop()
                substrings.append("Excel Update OK")
                print(f"\033[1;32;40mExcel Update\033[0m")  # Log a success message
            else:
                substrings.pop()
                substrings.append("Excel can't Update")
                print(f"\033[1;31;40mExcel can't Update\033[0m")  # Log an error message
        else:
            print(f"\033[1;31;40mExcel not Update\033[0m")  # Log a message indicating no update occurred
        result_str = "\n".join(substrings)  # Join the substrings with new lines
        ui.label.setText(result_str)  # Display the result in the UI label
    else:
        logtxt = f"Error: {response.status_code}, \n {response.text}"  # Log the error
        print(logtxt)
        ui.label.setText(logtxt)  # Display the error in the UI label


def btncallClick():
    callapi(0)  # Call the API without updating Excel


def btncall_updatCelick():
    callapi(1)  # Call the API and update Excel


def btnclsClick():
    ui.label.setText("")  # Clear the UI label text


def apisetClick():
    try:
        result = subprocess.run(["python", "AccessToken_Code.py"], capture_output=True,text=True)  # Run the external script
        print("Script Output:", result.stdout)
        print("Script Errors:", result.stderr)
    except Exception as e:
        print(f"Error running script: {e}")


if __name__ == '__main__':
    app = QApplication(sys.argv)  # Create the main application object
    win = QMainWindow()  # Create the main window
    ui = API_Main_UI_Bata.Ui_Dialog()  # Initialize the UI from the .ui file
    ui.setupUi(win)  # Set up the UI elements in the main window
    win.show()  # Show the main window

    # Connect button clicks to functions
    ui.pushButton.clicked.connect(btncallClick)  # Connect to API call without updating Excel
    ui.pushButton_2.clicked.connect(btnclsClick)  # Connect to clear the label
    ui.pushButton_3.clicked.connect(apisetClick)  # Connect to run the external script
    ui.pushButton_4.clicked.connect(btncall_updatCelick)  # Connect to API call and update Excel

    sys.exit(app.exec_())  # Start the event loop and exit the application when done