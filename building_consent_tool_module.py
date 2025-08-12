"""This module is the core part of the building consent tool. Its main functions are creating the main window of the
project, then set the style for the UI elements, including background color, font size, button style. After the user
enters the project name or any other information available and clicks the search button, the program will match projects
in the data sets and display detailed information in the result area and the project location on the map based on the
address in the search results.

Author: Chenxin Huang"""

from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, \
    QGraphicsView, QGraphicsScene, QGraphicsEllipseItem, QGraphicsPixmapItem, QScrollArea, QFrame
from PyQt5.QtGui import QPixmap, QColor, QIcon
from data_module import df, address_to_pixel
from image_dialog_module import ImageDialog

class BuildingConsentTool(QWidget):
    def __init__(self):
        """Defines the main class for the building consent tool, inheriting from QWidget."""
        super().__init__()
        self.initUI()

    def initUI(self):
        """Sets the window title and size for the tool."""
        self.setWindowTitle('Building Consent Tool')
        self.setGeometry(100, 100, 1800, 900)

        # Defines the stylesheet for the application, setting the styles for various widgets.
        self.setStyleSheet("""
            QWidget {
                background-color: #f8f9fa;
            }
            QLabel {
                font-size: 16px;
                font-family: Arial, Helvetica, sans-serif;
            }
            QLineEdit {
                padding: 10px;
                font-size: 14px;
                border: 1px solid #ced4da;
                border-radius: 8px;
                background-color: #ffffff;
            }
            QPushButton {
                background-color: #007bff;
                color: white;
                font-size: 14px;
                padding: 10px 20px;
                border: none;
                border-radius: 8px;
            }
            QPushButton:hover {
                background-color: #0056b3;
            }
            QFrame {
                background-color: #ffffff;
                border: 1px solid #ced4da;
                border-radius: 8px;
                padding: 10px;
            }
        """)

        # Creates the input label, text field, and search button, and connects the search button.
        self.inputLabel = QLabel('Enter Project Name or Any ID:')
        self.inputField = QLineEdit(self)
        self.searchButton = QPushButton('Search', self)
        self.searchButton.setIcon(QIcon('search_icon.png'))
        self.searchButton.clicked.connect(self.searchProject)

        # Sets up the scroll area for displaying search results.
        self.resultArea = QScrollArea()
        self.resultArea.setWidgetResizable(True)
        self.resultWidget = QWidget()
        self.resultLayout = QVBoxLayout(self.resultWidget)
        self.resultArea.setWidget(self.resultWidget)

        # Creates a vertical layout and adds the input label, text field, search button, and result area to it.
        searchLayout = QVBoxLayout()
        searchLayout.addWidget(self.inputLabel)
        searchLayout.addWidget(self.inputField)
        searchLayout.addWidget(self.searchButton)
        searchLayout.addWidget(self.resultArea)
        # Adds the search layout to the left side of the main layout.
        leftLayout = QVBoxLayout()
        leftLayout.addLayout(searchLayout)

        # Creates the main horizontal layout, adds the left layout to it, and sets it as the main layout of the window.
        mainLayout = QHBoxLayout()
        mainLayout.addLayout(leftLayout, 1)
        self.setLayout(mainLayout)

        # Creates the map view and scene, adds the map view to the main layout.
        self.mapView = QGraphicsView()
        self.mapScene = QGraphicsScene()
        self.mapView.setScene(self.mapScene)
        mainLayout.addWidget(self.mapView, 3)

        # Loads the map image and adds it to the map scene, with error handling if the image fails to load. Initializes the marker item to None.
        self.mapPixmap = QPixmap('map.png')
        if self.mapPixmap.isNull():
            print("Error: Unable to load map.png")
        self.mapItem = QGraphicsPixmapItem(self.mapPixmap)
        self.mapScene.addItem(self.mapItem)
        self.markerItem = None

    def searchProject(self):
        """Searches for the project based on the entered identifier and displays the result."""
        identifier = self.inputField.text().strip()
        result = df[(df['Project Name'].str.lower() == identifier.lower()) |
                    (df['City Planning Number'].str.lower() == identifier.lower()) |
                    (df['Land Supply Number'].str.lower() == identifier.lower()) |
                    (df['Building Permit Number'].str.lower() == identifier.lower()) |
                    (df['Cadastral Location'].str.lower() == identifier.lower()) |
                    (df['Real Estate Registration Name'].str.lower() == identifier.lower())]

        # Clears the previous search results from the result layout.
        for i in reversed(range(self.resultLayout.count())):
            widgetToRemove = self.resultLayout.itemAt(i).widget()
            self.resultLayout.removeWidget(widgetToRemove)
            widgetToRemove.setParent(None)

        # Displays the new search results in the result layout.
        for index, row in result.iterrows():
            for col in df.columns:
                label = QLabel(f"{col}: {row[col]}")
                label.setFrameStyle(QFrame.Panel | QFrame.Sunken)
                label.setStyleSheet("background-color: #e9ecef; padding: 8px; border-radius: 4px;")
                self.resultLayout.addWidget(label)

        # If the search result is not empty, retrieves the street address of the first result and prints it.
        if not result.empty:
            address = result.iloc[0]['Street Address']
            print(f"Marker address: {address}")

            # Converts the street address to pixel coordinates if found in the address-to-pixel mapping.
            if address in address_to_pixel:
                x, y = address_to_pixel[address]
                print(f"Using coordinates: x={x}, y={y}")

                # Removes the previous marker (if any) from the map scene and adds a new marker at the specified coordinates.
                if self.markerItem:
                    self.mapScene.removeItem(self.markerItem)
                self.markerItem = self.createMarker(x, y)
                self.mapScene.addItem(self.markerItem)

            # If the address is not found then print an error message and remove any existing marker.
            else:
                print("Error: Address not found in address_to_pixel mapping.")
                if self.markerItem:
                    self.mapScene.removeItem(self.markerItem)
                    self.markerItem = None

            photo_filename = result.iloc[0]['Photo Filename']
            self.showPhoto(photo_filename)
        else:
            if self.markerItem:
                self.mapScene.removeItem(self.markerItem)
                self.markerItem = None

    def createMarker(self, x, y):
        """Creates a marker on the map at the given coordinates."""
        marker = QGraphicsEllipseItem(x - 5, y - 5, 10, 10)
        marker.setBrush(QColor('red'))
        return marker

    def showPhoto(self, photo_filename):
        """Displays the photo of the project in a dialog."""
        photo_path = f'photos/{photo_filename}'
        print(f"Photo path: {photo_path}")
        dialog = ImageDialog(photo_path, self)
        dialog.exec_()