"""This module displays a dialog box that shows a photo of a project. When an image path is provided, it loads and
 displays the image. If the image cannot be loaded, an error message is displayed.

 Author : Chenxin Huang"""

from PyQt5.QtWidgets import QDialog, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class ImageDialog(QDialog):
    def __init__(self, image_path, parent=None):
        """Main class for the Building Consent Tool project."""
        super().__init__(parent) # Call the parent class's constructor.
        self.setWindowTitle("Project Photo")
        self.setGeometry(100, 100, 600, 400)
        self.imageLabel = QLabel(self)
        self.imageLabel.setGeometry(10, 10, 580, 380)
        print(f"Loading image from path: {image_path}")
        pixmap = QPixmap(image_path) # Load the image from the specified path into a QPixmap.
        if pixmap.isNull():
            self.imageLabel.setText("Unable to load image")
            print("Error: Unable to load image") # Set an error message on the QLabel if the image could not be loaded.
        else:
            self.imageLabel.setPixmap(
                pixmap.scaled(self.imageLabel.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)) # Scale the image to fit the QLabel, maintaining aspect ratio and using smooth transformation.