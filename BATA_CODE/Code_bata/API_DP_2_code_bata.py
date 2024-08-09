import requests  # URL HTTP library used for making API calls
import urllib3  # URL HTTP library also used for API calls, with additional capabilities
import subprocess  # Used to call and run external Python scripts or commands
import sys  # System-specific parameters and functions
from PyQt5.QtWidgets import QApplication, QMainWindow # UI components for creating application windows and widgets
from BATA_CODE.UI_Bata import API_DP_2_UI_bata # Import the custom user interface (UI)
import pandas as pd # Library for data manipulation and analysis, particularly working with DataFrames


def callapi(excelcom): # Function to call an API and handle Excel operations based on the argument
    file_path = 'data.xlsx' # Path to the Excel file

    # Try to read the DataFrame from the Excel file
    try:
        df = pd.read_excel(file_path, engine='openpyxl')
    except FileNotFoundError:
        # If the file doesn't exist, create a new DataFrame with specified columns
        df = pd.DataFrame(columns=['Column1', 'Column2'])
    urllib3.disable_warnings(urllib3.exceptions.NotOpenSSLWarning) # Disable SSL/TLS warnings
    # Get user input for DeviceId and APItag from the UI
    in1 = ui.textEdit.document().toPlainText()
    in2=ui.textEdit_2.document().toPlainText()
    # Construct the API URL using the DeviceId and APItag
    urlin="http://api.nlecloud.com/devices/"+in1+"/sensors/"+in2
    print(urlin)
    url = urlin
    # Read the AccessToken from a file named AccessToken.txt
    with open('AccessToken.txt', 'r') as file:
        content = file.read()
        print(content)
    # Set up the headers for the API request, including the AccessToken
    headers = {
        "AccessToken":content
    }

    # Send a GET request to the constructed URL with the headers
    response = requests.get(url, headers=headers)
    # Check the status of the request
    if response.status_code == 200:
        data = response.json()  # Parse the JSON response into a Python dictionary
        print(data)
        print(len(data))  # Print the length of the data
        datanew = str(data)  # Convert the data to a string
        print(len(datanew))  # Print the length of the string data
        q = 0
        substrings = []  # List to store substrings separated by commas
        for i in range(len(datanew)):
            if datanew[i]==",":
                print(datanew[q:i])  # Print each substring
                substrings.append(datanew[q:i])  # Add substring to the list
                q = i + 1  # Update the starting index for the next substring

        #Append the final substring after the last comma
        print(datanew[q:])
        substrings.append(datanew[q:])
        print(substrings)
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
                if substrings[NameIndex] == " 'Name': 'gps'":
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
    callapi(0) # Call the API without updating Excel
def btncallSaveClick():
    callapi(1) # Call the API and update Excel
def btnclsClick():
    data="" # Clear the UI label text
def apisetClick():
    try:
        result = subprocess.run(["python", "AccessToken_Code.py"], capture_output=True, text=True)# Run the external script
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
    ui.pushButton.clicked.connect(btncallClick) # Connect to API call without updating Excel
    ui.pushButton_2.clicked.connect(btnclsClick) # Connect to clear the label
    ui.pushButton_3.clicked.connect(apisetClick) # Connect to run the external script
    ui.pushButton_4.clicked.connect(btncallSaveClick) # Connect to API call and update Excel


    sys.exit(app.exec_())  # Start th  e event loop and exit the application when done