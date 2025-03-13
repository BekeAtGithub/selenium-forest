from PyQt5.QtWidgets import QMainWindow, QTextEdit, QVBoxLayout, QWidget  # Import PyQt5 components for GUI

class ResultsDisplayGUI(QMainWindow):  # Define the results display window
    def __init__(self):  # Constructor to initialize the UI
        super().__init__()
        self.initUI()  # Call function to set up the UI

    def initUI(self):  # Function to initialize the user interface
        self.setWindowTitle("Scan Results - Selenium Forest")  # Set window title
        self.setGeometry(150, 150, 700, 500)  # Set window size

        # Create central widget and layout
        central_widget = QWidget()  # Define central widget
        layout = QVBoxLayout()  # Define a vertical box layout

        # Create a text display area for scan results
        self.results_text = QTextEdit(self)  # Create text edit widget
        self.results_text.setReadOnly(True)  # Set text area to read-only mode
        layout.addWidget(self.results_text)  # Add text area to layout

        # Set the layout to the central widget
        central_widget.setLayout(layout)  # Assign layout to the central widget
        self.setCentralWidget(central_widget)  # Set the central widget for the window

    def update_results(self, results):  # Function to update the results display
        self.results_text.setText(results)  # Set new text content in the results area
