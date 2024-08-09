# import libraries
import requests  # HTTP library used for making API calls
import urllib3  # HTTP library also used for handling SSL/TLS connections
import subprocess  # Used to run external Python scripts or commands
import sys  # System-specific parameters and functions
from PyQt5.QtWidgets import QApplication, QMainWindow  # UI components for creating application windows and widgets
from code_1.UI import API_Main_UI  # Import the custom user interface (UI)

def callapi():  # Function to call an API
    urllib3.disable_warnings(urllib3.exceptions.NotOpenSSLWarning)  # Disable warnings related to SSL/TLS not using OpenSSL

    # Get the API URL from user input in the UI
    urlin = ui.textEdit.document().toPlainText()
    print(urlin)
    url = urlin

    # Read the AccessToken from a file named AccessToken.txt
    with open('AccessToken.txt', 'r') as file:
        content = file.read()
        print(content)

    # Set up the headers for the API request, including the AccessToken
    headers = {
        "AccessToken": content
    }

    # Send a GET request to the constructed URL with the headers
    response = requests.get(url, headers=headers)

    # Check the status of the request
    if response.status_code == 200:
        data = response.json()  # Parse the JSON response into a Python dictionary
        datanew = str(data)  # Convert the data to a string
        substrings = datanew.split(',')  # Split the string by commas
        # Append the final substring after the last comma

        # Join the substrings with new lines and set the result to a label in the UI
        result_str = "\n".join(substrings)
        ui.label.setText(result_str)
    else:
        # If the request fails, log and display the error status and message
        logtxt = str(f"Error: {response.status_code}, \n {response.text}")
        print(f"Error: {response.status_code}, {response.text}")
        ui.label.setText(logtxt)

def btncallClick():
    # Function to handle the API call when the button is clicked
    callapi()

def btnclsClick():
    # Function to clear the label text when the button is clicked
    data = ""
    ui.label.setText(data)

def apisetClick():
    try:
        # Use subprocess.run() to run the AccessToken_Code.py script
        result = subprocess.run(["python", "AccessToken_Code.py"], capture_output=True, text=True)
        print("Script Output:", result.stdout)
        print("Script Errors:", result.stderr)
    except Exception as e:
        print(f"Error running script: {e}")


if __name__ == '__main__':
    app = QApplication(sys.argv)  # Create the main application object
    win = QMainWindow()  # Create the main window
    ui = API_Main_UI.Ui_Dialog()  # Initialize the UI from the .ui file
    ui.setupUi(win)  # Set up the UI elements in the main window
    win.show()  # Show the main window

    # Connect button clicks to functions
    ui.pushButton.clicked.connect(btncallClick)
    ui.pushButton_2.clicked.connect(btnclsClick)
    ui.pushButton_3.clicked.connect(apisetClick)

    sys.exit(app.exec_())  # Start the event loop and exit the application when done